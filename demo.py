url = "https://api.artic.edu/api/v1/artworks/search"
import requests
r = requests.get(url, params={"q": "cats"})
if r.status_code == 200:
    data = r.json()