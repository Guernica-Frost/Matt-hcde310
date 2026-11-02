import requests

FIELDS = "id,title,artist_title,date_display,medium_display,image_id"

def search_art(term):
    """Search the Art Institute API for term; return a list of artworks, or None if the request fails."""
    url = "https://api.artic.edu/api/v1/artworks/search"
    params = {"q": term, "fields": FIELDS, "limit": 10}
    headers = {"AIC-User-Agent": "hcde310-hw4 (chengs35@uw.edu)"}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
    except requests.exceptions.RequestException:
        return None
    if response.status_code != 200:
        return None
    return response.json()["data"]
