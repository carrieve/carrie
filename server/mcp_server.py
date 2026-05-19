#!/usr/bin/env python3
"""
Carrie — MCP server for travel and food profiles.
Claude uses this to look up preferences when booking travel or ordering food.

Profiles are stored in ~/.carrie/profiles/travel/ and ~/.carrie/profiles/food/
"""

import json
from pathlib import Path
from mcp.server.fastmcp import FastMCP

CARRIE_HOME     = Path.home() / ".carrie"
TRAVEL_PROFILES = CARRIE_HOME / "profiles" / "travel"
FOOD_PROFILES   = CARRIE_HOME / "profiles" / "food"
CITY_GUIDES     = CARRIE_HOME / "city_guides"

# Create directories if they don't exist
TRAVEL_PROFILES.mkdir(parents=True, exist_ok=True)
FOOD_PROFILES.mkdir(parents=True, exist_ok=True)
CITY_GUIDES.mkdir(parents=True, exist_ok=True)

mcp = FastMCP("carrie")


# ── Shared helpers ────────────────────────────────────────────────────────────

def _load(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def _find(directory: Path, name: str) -> dict | None:
    name_lower = name.lower().strip()
    for p in directory.glob("*.json"):
        try:
            data = _load(p)
            full      = data.get("name", "").lower()
            preferred = data.get("preferred_name", "").lower()
            if name_lower in full or name_lower in preferred or full.startswith(name_lower):
                return data
        except Exception:
            pass
    return None

def _all(directory: Path) -> list[dict]:
    profiles = []
    for p in sorted(directory.glob("*.json")):
        try:
            profiles.append(_load(p))
        except Exception:
            pass
    return profiles


# ── Travel tools ──────────────────────────────────────────────────────────────

@mcp.tool()
def get_traveler_profile(name: str) -> str:
    """
    Look up a traveler's full preferences profile by name.
    Use before booking flights, hotels, or transport to get loyalty numbers,
    seat preferences, dietary needs, and more.
    """
    profile = _find(TRAVEL_PROFILES, name)
    if not profile:
        names = [p.get("preferred_name") or p.get("name", "?") for p in _all(TRAVEL_PROFILES)]
        if names:
            return f"No travel profile found for '{name}'. Known travelers: {', '.join(names)}"
        return f"No travel profiles exist yet."
    return _format_travel(profile)


@mcp.tool()
def list_travelers() -> str:
    """List all travelers who have saved travel profiles."""
    profiles = _all(TRAVEL_PROFILES)
    if not profiles:
        return "No travel profiles saved yet."
    lines = ["Saved travel profiles:\n"]
    for p in profiles:
        name    = p.get("preferred_name") or p.get("name", "Unknown")
        legal   = p.get("name", "")
        updated = p.get("updated_at", "unknown")[:10]
        lines.append(f"  • {name} (legal: {legal}) — last updated {updated}")
    return "\n".join(lines)


@mcp.tool()
def get_traveler_field(name: str, field: str) -> str:
    """
    Get a specific field from a traveler's profile.
    E.g. 'ktn', 'seat_pref', 'preferred_hotels', 'food_allergies'.
    """
    profile = _find(TRAVEL_PROFILES, name)
    if not profile:
        return f"No travel profile found for '{name}'."
    display = profile.get("preferred_name") or profile.get("name", name)
    value   = profile.get(field)
    if value is None:
        return f"{display} has no value saved for '{field}'."
    if isinstance(value, list):
        if not value:
            return f"{display} has no values for '{field}'."
        return f"{display} — {field}: {', '.join(str(v) for v in value)}"
    return f"{display} — {field}: {value}"


# ── Food tools ────────────────────────────────────────────────────────────────

@mcp.tool()
def get_food_profile(name: str) -> str:
    """
    Look up someone's food and delivery preferences by name.
    Use before ordering coffee, meals, or groceries via DoorDash or Instacart.
    Returns their coffee order, dietary restrictions, favorite restaurants,
    snack preferences, delivery addresses, and more.
    """
    profile = _find(FOOD_PROFILES, name)
    if not profile:
        names = [p.get("preferred_name") or p.get("name", "?") for p in _all(FOOD_PROFILES)]
        if names:
            return f"No food profile found for '{name}'. Known profiles: {', '.join(names)}"
        return f"No food profiles exist yet."
    return _format_food(profile)


@mcp.tool()
def list_food_profiles() -> str:
    """List everyone who has saved a food/delivery preferences profile."""
    profiles = _all(FOOD_PROFILES)
    if not profiles:
        return "No food profiles saved yet."
    lines = ["Saved food profiles:\n"]
    for p in profiles:
        name    = p.get("preferred_name") or p.get("name", "Unknown")
        updated = p.get("updated_at", "unknown")[:10]
        lines.append(f"  • {name} — last updated {updated}")
    return "\n".join(lines)


@mcp.tool()
def get_coffee_order(name: str) -> str:
    """
    Quick lookup: get someone's exact coffee order.
    Returns chain preference, usual order, milk, sweetener, and backup order.
    """
    profile = _find(FOOD_PROFILES, name)
    if not profile:
        return f"No food profile found for '{name}'."
    display = profile.get("preferred_name") or profile.get("name", name)
    lines   = [f"Coffee order for {display}:"]
    def add(label, key):
        v = profile.get(key)
        if v: lines.append(f"  {label}: {v}")
    add("Chain",          "coffee_chain")
    add("Backup chain",   "coffee_chain_backup")
    add("Order",          "coffee_order")
    add("Size",           "coffee_size")
    add("Temperature",    "coffee_temp")
    add("Milk",           "milk_pref")
    add("Sweetener",      "sweetener")
    add("Backup order",   "coffee_backup_order")
    add("Other drinks",   "other_drinks")
    add("Avoid",          "drinks_avoid")
    return "\n".join(lines) if len(lines) > 1 else f"{display} has no coffee preferences saved."


@mcp.tool()
def get_delivery_address(name: str, location: str = "office") -> str:
    """
    Get someone's delivery address for DoorDash or Instacart orders.
    location: 'office' (default) or 'home'
    """
    profile = _find(FOOD_PROFILES, name)
    if not profile:
        return f"No food profile found for '{name}'."
    display = profile.get("preferred_name") or profile.get("name", name)
    loc     = location.lower()
    if "home" in loc:
        addr  = profile.get("address_home", "")
        instr = profile.get("instructions_home", "")
        label = "Home"
    else:
        addr  = profile.get("address_office", "")
        instr = profile.get("instructions_office", "")
        label = "Office"
    if not addr:
        return f"{display} has no {label.lower()} address saved."
    result = f"{display} — {label} address: {addr}"
    if instr:
        result += f"\n  Delivery instructions: {instr}"
    return result


# ── City guide tools ──────────────────────────────────────────────────────────

@mcp.tool()
def get_city_recommendations(city: str, category: str = "restaurants") -> str:
    """
    Get EA-vetted recommendations for a city, sourced from r/ExecutiveAssistants.
    Categories: 'restaurants', 'hotels', 'transport'
    Returns top recommendations with scores and Reddit source links.
    If no guide exists for the city, returns instructions to build one.
    """
    city_slug = city.lower().replace(" ", "_").replace(",", "")
    path = CITY_GUIDES / f"{city_slug}.json"

    if not path.exists():
        available = [p.stem.replace("_", " ").title() for p in sorted(CITY_GUIDES.glob("*.json"))]
        if available:
            return (
                f"No city guide found for '{city}'. "
                f"Available cities: {', '.join(available)}. "
                f"To build a guide for {city}, run: "
                f"python ~/.carrie/../'Claude stuff'/carrie/scripts/build_city_guides.py \"{city}\""
            )
        return (
            f"No city guides built yet. To create one, run: "
            f"python '/Users/carrievanepps/Claude stuff/carrie/scripts/build_city_guides.py' \"{city}\""
        )

    with open(path, encoding="utf-8") as f:
        guide = json.load(f)

    cat = category.lower()
    # fuzzy match category
    if cat in ("restaurant", "dining", "food", "eat"):
        cat = "restaurants"
    elif cat in ("hotel", "accommodation", "stay"):
        cat = "hotels"
    elif cat in ("car", "car service", "transportation", "limo", "transit"):
        cat = "transport"

    items = guide.get("categories", {}).get(cat, [])
    updated = guide.get("last_updated", "unknown")[:10]

    if not items:
        return f"No {category} recommendations found for {city} yet. Try rebuilding the guide."

    lines = [
        f"=== EA-Vetted {cat.title()} Recommendations: {city} ===",
        f"Source: r/ExecutiveAssistants | Last updated: {updated}\n",
    ]
    for i, item in enumerate(items, 1):
        lines.append(f"{i}. {item['title']} (↑{item['score']} upvotes, {item['date']})")
        if item.get("summary") and item["summary"] not in ("(link post)", "(link post — no body text)"):
            lines.append(f"   {item['summary'][:200]}")
        comments = item.get("comments", [])
        if comments:
            lines.append("   Top EA responses:")
            for c in comments[:5]:
                lines.append(f"     • {c}")
        lines.append(f"   🔗 {item['url']}\n")

    return "\n".join(lines)


@mcp.tool()
def list_city_guides() -> str:
    """List all cities that have saved EA recommendation guides."""
    guides = sorted(CITY_GUIDES.glob("*.json"))
    if not guides:
        return (
            "No city guides built yet. To create one, run: "
            "python '/Users/carrievanepps/Claude stuff/carrie/scripts/build_city_guides.py' <city>"
        )
    lines = ["Saved city guides (sourced from r/ExecutiveAssistants):\n"]
    for p in guides:
        with open(p, encoding="utf-8") as f:
            g = json.load(f)
        city    = g.get("city", p.stem)
        updated = g.get("last_updated", "unknown")[:10]
        cats    = list(g.get("categories", {}).keys())
        lines.append(f"  • {city} — updated {updated} | categories: {', '.join(cats)}")
    return "\n".join(lines)


# ── Formatters ────────────────────────────────────────────────────────────────

def _format_travel(data: dict) -> str:
    lines = []
    def add(label, value):
        if value: lines.append(f"  {label}: {value}")
    def add_list(label, items):
        if items: lines.append(f"  {label}: {', '.join(str(i) for i in items)}")

    name = data.get("preferred_name") or data.get("name", "Unknown")
    lines.append(f"=== Travel Profile: {name} ===")
    lines.append(f"  Legal name: {data.get('name', '')}")
    add("Email", data.get("email"))
    add("Phone", data.get("phone"))
    add("Emergency contact", f"{data.get('emergency_contact_name','')} {data.get('emergency_contact_phone','')}".strip())
    add("Passport", f"{data.get('passport_country','')} expires {data.get('passport_expiry','')}".strip(" expires"))
    add("Date of birth", data.get("dob"))
    add("Home airports", data.get("home_airports"))

    lines.append("\n--- Air Travel ---")
    add("Preferred airlines", data.get("preferred_airlines"))
    add("Avoided airlines",   data.get("avoided_airlines"))
    add("Seat preference",    data.get("seat_pref"))
    add("Class of service",   data.get("class_pref"))
    add("Class notes",        data.get("class_notes"))
    add("Routing preference", data.get("routing_pref"))
    add("Min connection",     data.get("min_connection"))
    add_list("Trusted traveler programs", data.get("trusted_traveler", []))
    add("KTN",                data.get("ktn"))
    add("CLEAR ID",           data.get("clear_id"))
    add("Meal preference",    data.get("meal_pref"))
    ff = data.get("frequent_flyer", [])
    if ff:
        lines.append("  Frequent flyer:")
        for item in ff:
            lines.append(f"    {item.get('airline','')}: {item.get('number','')}")

    lines.append("\n--- Hotels ---")
    add("Preferred chains",   data.get("preferred_hotels"))
    add("Avoided chains",     data.get("avoided_hotels"))
    add("Bed type",           data.get("bed_pref"))
    add("Floor preference",   data.get("floor_pref"))
    add("Location",           data.get("hotel_location"))
    add("Smoking",            data.get("smoking_pref"))
    add_list("Amenities",     data.get("hotel_amenities", []))
    add("Hotel notes",        data.get("hotel_notes"))
    hl = data.get("hotel_loyalty", [])
    if hl:
        lines.append("  Hotel loyalty:")
        for item in hl:
            lines.append(f"    {item.get('chain','')}: {item.get('number','')}")

    lines.append("\n--- Ground Transport ---")
    add("Preferred mode",     data.get("ground_pref"))
    add("Rental car company", data.get("rental_car_company"))
    add("Rental car loyalty", data.get("rental_car_loyalty"))
    add("Car type",           data.get("car_type_pref"))
    add("Car service",        data.get("car_service_pref"))
    add("Notes",              data.get("ground_notes"))

    lines.append("\n--- Food & Dietary ---")
    add_list("Dietary restrictions", data.get("dietary_restrictions", []))
    add("Food allergies",     data.get("food_allergies"))
    add("Food notes",         data.get("food_notes"))

    add("\nMedical/accessibility", data.get("medical_notes"))
    add("Additional notes",   data.get("additional_notes"))
    add("Last updated",       data.get("updated_at"))
    return "\n".join(line for line in lines)


def _format_food(data: dict) -> str:
    lines = []
    def add(label, value):
        if value: lines.append(f"  {label}: {value}")
    def add_list(label, items):
        if items: lines.append(f"  {label}: {', '.join(str(i) for i in items)}")

    name = data.get("preferred_name") or data.get("name", "Unknown")
    lines.append(f"=== Food Profile: {name} ===")
    add("Email", data.get("email"))
    add("Phone", data.get("phone"))

    lines.append("\n--- Coffee & Drinks ---")
    add("Chain",            data.get("coffee_chain"))
    add("Backup chain",     data.get("coffee_chain_backup"))
    add("Order",            data.get("coffee_order"))
    add("Size",             data.get("coffee_size"))
    add("Temperature",      data.get("coffee_temp"))
    add("Milk",             data.get("milk_pref"))
    add("Sweetener",        data.get("sweetener"))
    add("Backup order",     data.get("coffee_backup_order"))
    add("Other drinks",     data.get("other_drinks"))
    add("Avoid",            data.get("drinks_avoid"))

    lines.append("\n--- Meals ---")
    add_list("Dietary restrictions", data.get("dietary_restrictions", []))
    add("Food allergies",   data.get("food_allergies"))
    add("Favorite cuisines",data.get("fav_cuisines"))
    add("Avoid cuisines",   data.get("avoid_cuisines"))
    add("Spice tolerance",  data.get("spice_level"))
    add("Avoid foods",      data.get("foods_avoid"))
    add("Avoid restaurants",data.get("restaurants_avoid"))
    add("Meal notes",       data.get("meal_notes"))
    favs = data.get("favorite_restaurants", [])
    if favs:
        lines.append("  Favorite restaurants:")
        for r in favs:
            lines.append(f"    {r.get('name','')}: {r.get('usual_order','')}")

    lines.append("\n--- Snacks & Groceries ---")
    add("Salty snacks",     data.get("snacks_salty"))
    add("Sweet snacks",     data.get("snacks_sweet"))
    add("Fav drinks",       data.get("fav_drinks"))
    add("Fav brands",       data.get("fav_brands"))
    add("Staples",          data.get("staples"))
    add("Avoid",            data.get("grocery_avoid"))

    lines.append("\n--- Delivery ---")
    add("Office address",   data.get("address_office"))
    add("Office instructions", data.get("instructions_office"))
    add("Home address",     data.get("address_home"))
    add("Home instructions",data.get("instructions_home"))
    add("DoorDash email",   data.get("doordash_email"))
    add("Instacart email",  data.get("instacart_email"))

    lines.append("\n--- Budget ---")
    add("Meal budget",      data.get("meal_budget"))
    add("Coffee budget",    data.get("coffee_budget"))
    add("Delivery timing",  data.get("delivery_timing"))
    add("Notes",            data.get("additional_notes"))
    add("Last updated",     data.get("updated_at"))
    return "\n".join(line for line in lines)


if __name__ == "__main__":
    mcp.run()
