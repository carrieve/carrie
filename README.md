# Carrie ✈️☕

**AI-powered preference management for Executive Assistants.**

Capture travel and food preferences once. Claude looks them up automatically when booking flights, hotels, ordering coffee, or placing DoorDash orders — without you having to ask twice.

Built by an EA, for EAs.

---

## What it does

**Travel preferences** — loyalty numbers, seat preferences, TSA PreCheck/Global Entry, hotel chains, ground transport, dietary needs and more.

**Food & delivery preferences** — exact coffee order, favorite restaurants, dietary restrictions, snack preferences, and delivery addresses for home and office.

Once someone fills out their form, you can say:

> *"Book a flight for Jamie to NYC next Tuesday"*
> *"Order Carrie her usual coffee from Starbucks to the office"*
> *"What hotel chain does Alex prefer?"*

And Claude already knows everything it needs.

---

## Install

```bash
claude plugin install github:carrieve/carrie
```

Then run:

```
/carrie-setup
```

---

## Usage

```
/carrie
```

Opens the main menu — look up profiles, start the form server, or add new people.

---

## Collecting preferences

Start the form server with `/carrie`, then share the links:
- **Travel form:** http://localhost:8080
- **Food form:** http://localhost:8080/food

When someone submits their form, a JSON file downloads. Save it to:
- `~/.carrie/profiles/travel/` for travel profiles
- `~/.carrie/profiles/food/` for food profiles

Claude will find it automatically from there.

---

## Requirements

- [Claude Code](https://claude.ai/code)
- Python 3
- The `mcp` package (installed automatically by `/carrie-setup`)

---

## About

Created by [Carrie Van Epps](https://github.com/carrieve) — a retired Executive Assistant learning to build with AI.

*Questions or ideas? Open an issue on GitHub.*
