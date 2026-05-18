# Carrie

Your AI-powered EA preference assistant. 

## What Carrie can do

- Look up anyone's travel preferences (flights, hotels, ground transport)
- Look up anyone's food preferences (coffee order, meals, groceries, delivery address)
- Start the form server so you can collect preferences from new people
- Help you book travel or order food using saved profiles

## Instructions for Claude

When the user runs /carrie, show this menu:

---

**Carrie** ✈️☕

What would you like to do?

1. **Look up a travel profile** — e.g. "get Jamie's travel profile"
2. **Look up a food/coffee profile** — e.g. "what's Alex's coffee order"
3. **Start the form server** — to collect preferences from someone new
4. **List all profiles** — see everyone with saved travel or food profiles
5. **Add a profile** — instructions for saving a new JSON profile

---

Then wait for the user to tell you what they want and help them do it.

### If they want to start the form server:
Run the form server in the background:
```
python3 "${CLAUDE_PLUGIN_ROOT}/server/form_server.py" &
```
Then tell them:
- Travel form: http://localhost:8080
- Food form: http://localhost:8080/food

### If they want to look up a profile:
Use the `carrie` MCP tools:
- `get_traveler_profile(name)` for travel
- `get_food_profile(name)` for food
- `get_coffee_order(name)` for just the coffee order
- `get_delivery_address(name, location)` for a delivery address
- `list_travelers()` to see all travel profiles
- `list_food_profiles()` to see all food profiles

### If they want to add a profile:
Tell them: "Have the person fill out the form at http://localhost:8080 (travel) or http://localhost:8080/food (food). When they submit, a JSON file will download. Save that file to ~/.carrie/profiles/travel/ or ~/.carrie/profiles/food/ and I'll be able to find it."
