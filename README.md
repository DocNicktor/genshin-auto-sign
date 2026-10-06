# Genshin Impact Auto Sign-in Script

I wrote this simple Python script to automate my daily HoYoLAB check-ins for Genshin Impact because I always lazy to do it manually. 

## What it does:
* **Runs daily:** Uses GitHub Actions (cron job) to run automatically every day.
* **Human-like behavior:** I added a random sleep timer (0-60 mins) before sending the request so it acts more like a real user and avoids being flagged as a bot.
* **Safe credentials:** My personal HoYoLAB cookie is safely stored in GitHub Secrets, not hardcoded in the code.
* **Manual run:** Can also be triggered manually using `workflow_dispatch` for testing.

## Tools used:
Python, `requests` library, GitHub Actions.
