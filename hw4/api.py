import requests

# Request the artwork ID and the details used in the results list.
FIELDS = "id,title,artist_title,date_display"

# Keep API requests separate from the routes that display pages and messages.
def search_art(term):
    """Search the Art Institute API for term; return a list of artworks, or None if the request fails."""
    url = "https://api.artic.edu/api/v1/artworks/search"
    # Pass the user's term through params so requests encodes the query string.
    params = {"q": term, "fields": FIELDS, "limit": 10}
    # This header identifies the application to the API; it is not an API key.
    headers = {"AIC-User-Agent": "hcde310-hw4 (chengs35@uw.edu)"}
    try:
        # Use a timeout so a stalled API request does not wait indefinitely.
        response = requests.get(url, params=params, headers=headers, timeout=10)
    except requests.exceptions.RequestException:
        # Let the route show a friendly message for connection errors or timeouts.
        return None
    # Treat an unsuccessful HTTP response as an API error too.
    if response.status_code != 200:
        return None
    # The data list holds the artworks; an empty list triggers the no-results message.
    return response.json()["data"]
