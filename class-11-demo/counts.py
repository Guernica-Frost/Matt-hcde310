# Class 11 code-along: count_by_artist from HW2/HW3, in its own file so pytest can import it.

def count_by_artist(artworks):
    """Takes a list of artwork dicts; returns {artist: number of works}."""
    counts = {}
    for art in artworks:
        artist = art.get("artist_title", "Unknown") or "Unknown"
        counts[artist] = counts.get(artist, 0) + 1
    return counts


if __name__ == "__main__":
    # Only runs when you type: python3 counts.py  (not when pytest imports this file)
    sample = [{"title": "Water Lilies", "artist_title": "Claude Monet"},
              {"title": "Untitled", "artist_title": None}]
    print(count_by_artist(sample))
