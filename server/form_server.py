#!/usr/bin/env python3
"""
Serves the travel and food preferences forms and saves submitted profiles as JSON.

Routes:
  GET  /              → travel preferences form
  POST /submit        → save travel profile
  GET  /food          → food & delivery preferences form
  POST /food/submit   → save food profile

Run: python form_server.py
Then open:
  http://localhost:8080       — travel form
  http://localhost:8080/food  — food form
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

PORT = 8080
BASE_DIR        = Path(__file__).parent
TRAVEL_FORM     = BASE_DIR.parent / "forms" / "travel_form.html"
FOOD_FORM       = BASE_DIR.parent / "forms" / "food_form.html"
CARRIE_HOME     = Path.home() / ".carrie"
TRAVEL_PROFILES = CARRIE_HOME / "profiles" / "travel"
FOOD_PROFILES   = CARRIE_HOME / "profiles" / "food"
FOOD_PROFILES   = BASE_DIR.parent / "food-profiles" / "profiles"

TRAVEL_PROFILES.mkdir(exist_ok=True)
FOOD_PROFILES.mkdir(exist_ok=True)


class Handler(BaseHTTPRequestHandler):

    # ── GET ──────────────────────────────────────────────
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._serve_file(TRAVEL_FORM)
        elif self.path in ("/food", "/food/", "/food/index.html"):
            self._serve_file(FOOD_FORM)
        else:
            self.send_response(404)
            self.end_headers()

    # ── POST ─────────────────────────────────────────────
    def do_POST(self):
        if self.path == "/submit":
            self._save_profile(TRAVEL_PROFILES, suffix="travel_profile")
        elif self.path == "/food/submit":
            self._save_profile(FOOD_PROFILES, suffix="food_profile")
        else:
            self.send_response(404)
            self.end_headers()

    # ── Helpers ──────────────────────────────────────────
    def _serve_file(self, path: Path):
        if not path.exists():
            self.send_response(404)
            self.end_headers()
            return
        content = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def _save_profile(self, directory: Path, suffix: str):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self._json_response(400, {"error": "Invalid JSON"})
            return

        name = data.get("name", "").strip()
        if not name:
            self._json_response(400, {"error": "Name is required"})
            return

        filename = name.lower().replace(" ", "_").replace("/", "_").replace("\\", "_")
        filename = f"{filename}_{suffix}.json"
        profile_path = directory / filename

        with open(profile_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"  Saved: {profile_path}")
        self._json_response(200, {"success": True, "saved_to": str(profile_path)})

    def _json_response(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(f"[server] {fmt % args}")


if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), Handler)
    print(f"Server running at http://localhost:{PORT}")
    print(f"  Travel form : http://localhost:{PORT}/")
    print(f"  Food form   : http://localhost:{PORT}/food")
    print(f"Travel profiles saved to : {TRAVEL_PROFILES}")
    print(f"Food profiles saved to   : {FOOD_PROFILES}")
    print("Press Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
