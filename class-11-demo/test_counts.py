# Class 11 code-along. Run: pytest   (or: python3 -m pytest)
# pytest finds files named test_*.py and runs every function named test_*.

from counts import count_by_artist


def test_counts_two_artists():
    art = [{"title": "A", "artist_title": "Monet"},
           {"title": "B", "artist_title": "Monet"},
           {"title": "C", "artist_title": "Cassatt"}]
    assert count_by_artist(art) == {"Monet": 2, "Cassatt": 1}


def test_counts_unknown_artist():
    # The API sends "artist_title": null (None in Python) when it doesn't know the artist
    art = [{"title": "A", "artist_title": None},
           {"title": "B", "artist_title": "Monet"}]
    assert count_by_artist(art) == {"Unknown": 1, "Monet": 1}


# Your turn: write one more test. Ideas:
#   - an empty list
#   - an artwork with no "artist_title" key at all
def test_empty_list():
    art = []
    assert count_by_artist(art) == {}
