import requests

FIELDS = "id,title,artist_title,artist_display,date_display,medium_display"

def count_by_artist(artworks):
    """The function takes a dictionary of artworks, and return the dictionary counting works per artist."""
    counts = {}

    for artwork in artworks:
        artist = artwork.get('artist_title') or "Unknown"
        counts[artist] = counts.get(artist, 0) + 1

    return counts

def save_results(artworks, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for artwork in artworks:
            title = artwork.get("title") or "Untitled"
            artist = artwork.get("artist_title") or "Unknown artist"
            date = artwork.get("date_display") or "Unknown date"
            medium = artwork.get("medium_display") or "Unknown medium"
            f.write(f"{title}, {artist}, {date}, {medium}\n")
              

term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"
params = {"q" : term, "fields" : FIELDS}
headers = {"AIC-User-Agent": "hcde310-hw3 (chengs35@uw.edu)"}
response = requests.get(url, params=params, headers=headers)

if response.status_code != 200:
    print("Request failed:", response.status_code, response.reason)
else:
    data = response.json()
    artworks = data["data"]
    if not artworks:
        print("No result")
    else:
        for i in range(len(artworks)):
            print(f"{artworks[i].get('title')} - {artworks[i].get('artist_title') or "Unknown"} ({artworks[i].get('date_display') or "Unknown"}) ({artworks[i].get('medium_display') or "Unknown"})")
        counts = count_by_artist(artworks)
        print(counts)
        save_results(artworks, "result.txt")
