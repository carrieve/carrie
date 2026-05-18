# Carrie Setup

Run this skill once after installing the plugin to get everything ready.

## Steps

1. Check that Python 3 is installed
2. Install the `mcp` Python package
3. Create the profiles directories
4. Confirm everything is working

## Instructions for Claude

When the user runs /carrie-setup, do the following steps in order:

### Step 1 — Check Python
Run: `python3 --version`
If it fails, tell the user to install Python from python.org and come back.

### Step 2 — Install the mcp package
Run: `pip3 install mcp`
Tell the user this may take a moment.

### Step 3 — Create profile directories
Create these directories if they don't exist:
- `~/.carrie/profiles/travel/`
- `~/.carrie/profiles/food/`

Run:
```
mkdir -p ~/.carrie/profiles/travel && mkdir -p ~/.carrie/profiles/food && echo "done"
```

### Step 4 — Confirm
Tell the user setup is complete and explain what's next:

- To collect preferences: start the form server with `/carrie` and open the form links in a browser
- To look up profiles: just ask Claude naturally — "get Jamie's travel profile" or "what's Alex's coffee order"
- To add a profile: have the person fill out the form, then save the downloaded JSON to `~/.carrie/profiles/travel/` or `~/.carrie/profiles/food/`

End with:
"Carrie is ready. ✈️☕"
