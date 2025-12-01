from typing import Optional, Dict
import logging
import requests

# Zenquotes api
QUOTE_API_URL = "https://zenquotes.io/api/random"

def fetch_random_quote() -> Dict[str, Optional[str]]:
    """
    Fetch a random motivational quote from the external API.
    """
    try:
        resp = requests.get(QUOTE_API_URL, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        if isinstance(data, list) and data:
            item = data[0]
        else:
            item = data

        text = (
            item.get("content")  
            or item.get("q")     
        )
        author = (
            item.get("author")   
            or item.get("a")     
        )

        if not text:
            raise ValueError("Quote text missing in API response")

        return {
            "text": text,
            "author": author or "Unknown",
        }

    except Exception as e:
        logging.exception("Error fetching quote from external API: %s", e)
        return {
            "text": "Could not load quote right now.",
            "author": None,
        }
