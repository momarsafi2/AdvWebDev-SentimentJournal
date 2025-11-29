# MoodFit – Sentiment Journal

## Live Deployment

https://advwebdev-sentimentjournal.onrender.com

(Free Render instance – may spin down when inactive)

## Overview

A Flask web app for journaling, mood tracking, sentiment analysis and dashboard visualization.

## How to Run (Locally)

## Step 1

- Clone the repository:

```bash
git clone https://github.com/momarsafi2/AdvWebDev-SentimentJournal.git
cd AdvWebDev-SentimentJournal
```

## Step 2

- Create & activate virtual environment

## For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

## For Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 3

- Install dependencies

```bash
pip install -r requirements.txt
```

## Step 4

- Run the Flask app

```bash
flask --app src run
```

## Step 5

- The app will be available to you at:

```bash
http://127.0.0.1:5000
```

## Running with Docker

## 1. Build image

```bash
docker build -t moodfit-app .
```

## 2. Run container

```bash
docker run -p 5000:5000 moodfit-app
```

## Testing

## Run all tests:

```bash
pytest
```

## Run tests but skip Selenium (CI Mode)

```bash
pytest -k "not test_homepage_e2e"
```

## Run with coverage

```bash
pytest --cov=src
```

## Tests include:

- Unit tests (sentiment, models, CRUD)
- Integration tests (API endpoints)
- Login + authentication tests
- End-to-end Selenium test (homepage loads)

## CI/CD – GitHub Actions

A workflow in: .github/workflows/ci.yml

Automatically runs when you push:

- Installs dependencies
- Runs all pytest tests
- Skips Selenium in CI
- Shows pass/fail badge

## API Endpoints

GET /api/sentiment-summary

- Returns mood statistics for logged-in user.

POST /api/entries

- Create a new journal entry.

GET /api/entries

- Fetch all entries for the authenticated user.

GET /api/quote

- Returns random motivational quote (external API).

## Features

1. User Authentication (Register & Login): Secure account system using Flask-Login with hashed passwords and session-based access control.
2. Create New Journal Entries: Users can write and save mood or reflection entries with automatic timestamps.
3. Edit & Delete Entries: Full CRUD support. Users can update or remove their journal entries anytime.
4. Sentiment Analysis (VADER) Integration: Each entry is automatically analyzed to generate a sentiment score and label (positive, neutral, negative).
5. Dashboard Overview (Analytics Page):The Dashboard summarizes the user’s mood history. Includes: Total number of journal entries, average sentiment score, count of positive, neutral, and negative entries. Also visual chart/graph (via Chart.js) to show sentiment trends over time.
6. External Quote Integration: Fetches a new motivational quote from an external API to inspire the user on the dashboard.

## Performance Optimization (PageSpeed Insights)

## Screenshots

## Group Members

Omar Safi, Roya Salihi
