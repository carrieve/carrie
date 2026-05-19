# Carrie ✈️☕
**AI-powered preference management for Executive Assistants.**

Stop looking up the same information over and over. Carrie connects your travelers' preferences directly to your AI assistant — so booking a flight or ordering coffee is as simple as asking.

Built by an EA, for EAs.

---

## What it does

You ask Claude:
> *"Book Jamie a flight to NYC next Tuesday"*
> *"Order Carrie her usual coffee to the office"*
> *"What hotel chain does Alex prefer?"*

Claude already knows the answer — because Carrie told it.

No more digging through spreadsheets. No more "what's their loyalty number again." No more copy-pasting into booking sites.

---

## How it works

**Step 1 — Someone fills out a form**
Send them a link. They fill it out once — seat preferences, loyalty numbers, TSA PreCheck, exact coffee order, dietary restrictions, delivery address. Everything.

👉 [carrie-ai-forms.netlify.app](https://carrie-ai-forms.netlify.app)

**Step 2 — You save their profile**
Their preferences download as a file. Drop it in a folder. Done.

**Step 3 — Claude knows everything**
Next time you need to book travel or order food, just ask. Claude looks up their profile automatically and uses it.

---

## Get started

**What you need:**
- A Mac or PC
- [Claude Code](https://claude.ai/code) — free from Anthropic
- Python 3 — already installed on most Macs

**Install Carrie:**
```bash
claude plugin install github:carrieve/carrie
```

**Run setup (just once):**
```
/carrie-setup
```

**Open Carrie anytime:**
```
/carrie
```

---

## Collecting preferences

Share these links with your travelers:

- **Travel form** — flights, hotels, loyalty numbers, dietary needs, and more
- **Food & coffee form** — exact coffee order, favorite restaurants, delivery addresses

👉 **[getcarrieai.com](https://getcarrieai.com)**

When they submit, a file downloads. Email it back to you, drop it in your profiles folder, and Claude can find it automatically.

---

## Already have preferences in a Google Doc?

No need to start from scratch. Use the **Import tool** to paste any existing notes — a Google Doc, an email, bullet points — and Carrie will extract and convert them into a profile automatically.

👉 **[getcarrieai.com/import.html](https://getcarrieai.com/import.html)**

Just paste, review, and download. Works for both travel and food profiles.

---

## FAQ

**Do my travelers need Claude or any special software?**
No. They just fill out a web form — like any Google Form. Nothing to install.

**Does this work with any AI?**
Right now it's built for Claude Code. Support for other platforms is coming as the technology matures.

**Is my data private?**
Yes. Profiles are stored locally on your own computer. Nothing is sent to the cloud.

**Can I use this for a whole team of EAs?**
Yes — each EA installs Carrie on their own machine and manages their own travelers' profiles.

---

## Requirements

- [Claude Code](https://claude.ai/code)
- Python 3
- The `mcp` package (installed automatically by `/carrie-setup`)

---

## About

Created by [Carrie Van Epps](https://github.com/carrieve) — an Executive Assistant learning to build with AI.

*Questions, ideas, or feedback? [Open an issue](https://github.com/carrieve/carrie/issues) — I'd love to hear from you.*
