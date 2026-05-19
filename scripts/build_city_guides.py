#!/usr/bin/env python3
"""
Carrie — City Guide Builder

Searches r/ExecutiveAssistants for restaurant, hotel, and transportation
recommendations by city and saves them to ~/.carrie/city_guides/{city}.json

Usage:
    python build_city_guides.py "New York City"
    python build_city_guides.py "Chicago"
    python build_city_guides.py --all    # rebuilds all saved cities

Reddit's public JSON API is used — no API key required.
"""

import json
import sys
import time
import urllib.request
import urllib.parse
from pathlib import Path
from datetime import datetime

CARRIE_HOME  = Path.home() / ".carrie"
GUIDES_DIR   = CARRIE_HOME / "city_guides"
GUIDES_DIR.mkdir(parents=True, exist_ok=True)

SUBREDDIT    = "ExecutiveAssistants"
USER_AGENT   = "CarrieAI/1.0 (EA preference management tool; github.com/carrieve/carrie)"
MIN_SCORE    = 3      # ignore posts with fewer upvotes than this
MAX_RESULTS  = 25     # posts to fetch per category

# Search queries are city-specific — the city name is prepended at runtime
CATEGORIES   = {
    "restaurants": [
        "restaurant recommendation",
        "client dinner recommendation",
        "where to eat recommendation",
        "best restaurant suggest",
        "dinner reservation recommend",
    ],
    "hotels": [
        "hotel recommendation",
        "where to stay recommendation",
        "best hotel suggest",
        "hotel suggest executive",
        "hotel book exec",
        "hotel prefer",
    ],
    "transport": [
        "car service recommendation",
        "black car recommend",
        "transportation recommend",
        "limo service suggest",
        "car service prefer",
    ],
}

# Keywords that must appear in title OR body for a post to count as a recommendation
RECOMMENDATION_KEYWORDS = [
    "recommend", "suggestion", "suggest", "best", "favorite", "favourite",
    "go to", "love", "tried", "book", "we use", "always use", "worth it"
]


# ── Reddit helpers ────────────────────────────────────────────────────────────

def reddit_search(subreddit: str, query: str, limit: int = 25) -> list[dict]:
    """Search a subreddit using Reddit's public JSON API."""
    params = urllib.parse.urlencode({
        "q": query,
        "restrict_sr": "1",
        "sort": "top",
        "t": "all",
        "limit": limit,
    })
    url = f"https://www.reddit.com/r/{subreddit}/search.json?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.load(resp)
            return data.get("data", {}).get("children", [])
    except Exception as e:
        print(f"  Warning: search failed for '{query}': {e}")
        return []


def fetch_comments(post_id: str, limit: int = 20) -> list[str]:
    """Fetch top comments for a Reddit post — this is where the real recommendations live."""
    url = f"https://www.reddit.com/comments/{post_id}.json?limit={limit}&sort=top"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.load(resp)
            if len(data) < 2:
                return []
            comments = data[1].get("data", {}).get("children", [])
            texts = []
            for c in comments:
                body = c.get("data", {}).get("body", "").strip()
                score = c.get("data", {}).get("score", 0)
                if body and body != "[deleted]" and body != "[removed]" and score >= 2:
                    texts.append(f"(↑{score}) {body[:300]}")
            return texts[:8]  # top 8 comments
    except Exception as e:
        print(f"    Warning: couldn't fetch comments for {post_id}: {e}")
        return []


def _has_recommendation_signal(title: str, body: str) -> bool:
    """Return True if the post looks like it contains actual recommendations."""
    combined = (title + " " + body).lower()
    return any(kw in combined for kw in RECOMMENDATION_KEYWORDS)


def extract_recommendations(posts: list[dict], city: str, min_score: int = MIN_SCORE) -> list[dict]:
    """Pull useful recommendations out of Reddit posts."""
    seen_titles = set()
    results = []
    city_variants = [city.lower(), city.split(",")[0].lower()]  # "New York City" and "New York"

    for post in posts:
        d = post.get("data", {})
        score    = d.get("score", 0)
        title    = d.get("title", "")
        selftext = d.get("selftext", "")
        url      = f"https://reddit.com{d.get('permalink', '')}"
        created  = datetime.utcfromtimestamp(d.get("created_utc", 0)).strftime("%Y-%m-%d")
        combined = (title + " " + selftext).lower()

        if score < min_score:
            continue
        if title in seen_titles:
            continue

        # Must mention the city
        if not any(cv in combined for cv in city_variants):
            continue

        # Must have recommendation language
        if not _has_recommendation_signal(title, selftext):
            continue

        # Skip job listing posts
        if any(skip in title.lower() for skip in ["jobs from", "job post", "hiring", "position available"]):
            continue

        # Fetch comments — the real recommendations are in here
        post_id  = d.get("id", "")
        comments = []
        if post_id:
            time.sleep(0.5)
            comments = fetch_comments(post_id)

        seen_titles.add(title)
        results.append({
            "title":    title,
            "score":    score,
            "summary":  selftext[:300].strip() if selftext else "(link post)",
            "comments": comments,
            "url":      url,
            "date":     created,
        })

    # Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:10]  # top 10 per category


# ── City guide builder ────────────────────────────────────────────────────────

def build_guide(city: str) -> dict:
    """Build a city guide for a given city by searching Reddit."""
    print(f"\nBuilding city guide for: {city}")
    guide = {
        "city":        city,
        "source":      f"r/{SUBREDDIT}",
        "last_updated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "categories":  {}
    }

    for category, keywords in CATEGORIES.items():
        print(f"  Searching {category}...")
        all_posts = []
        for keyword in keywords[:3]:  # limit to 3 keywords per category
            query = f"{city} {keyword}"
            posts = reddit_search(SUBREDDIT, query, limit=MAX_RESULTS)
            all_posts.extend(posts)
            time.sleep(3)  # be polite to Reddit's API — avoid 429s

        recommendations = extract_recommendations(all_posts, city)
        guide["categories"][category] = recommendations
        print(f"    Found {len(recommendations)} vetted results")

    return guide


def save_guide(guide: dict) -> Path:
    """Save guide to ~/.carrie/city_guides/{city}.json"""
    city_slug = guide["city"].lower().replace(" ", "_").replace(",", "")
    path = GUIDES_DIR / f"{city_slug}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(guide, f, indent=2)
    print(f"  Saved to {path}")
    return path


def load_guide(city: str):
    """Load an existing city guide."""
    city_slug = city.lower().replace(" ", "_").replace(",", "")
    path = GUIDES_DIR / f"{city_slug}.json"
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return None


def list_guides() -> list[str]:
    """List all saved city guides."""
    return [p.stem.replace("_", " ").title() for p in sorted(GUIDES_DIR.glob("*.json"))]


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python build_city_guides.py <city>")
        print("       python build_city_guides.py --all")
        print("       python build_city_guides.py --list")
        sys.exit(1)

    arg = sys.argv[1]

    if arg == "--list":
        guides = list_guides()
        if guides:
            print("Saved city guides:")
            for g in guides:
                print(f"  • {g}")
        else:
            print("No city guides saved yet.")

    elif arg == "--all":
        guides = list_guides()
        if not guides:
            print("No existing guides to rebuild. Run with a city name first.")
        for city in guides:
            guide = build_guide(city)
            save_guide(guide)

    else:
        city  = " ".join(sys.argv[1:])
        guide = build_guide(city)
        save_guide(guide)
        print(f"\nDone! City guide for {city} is ready.")
