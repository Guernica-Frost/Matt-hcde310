# HW5 test_app.py: one example test. Add your own below it (step 5).
# Run from this folder:  python3 -m pytest
from app import app


def test_home_shows_search_form():
    client = app.test_client()        # a pretend browser, no server needed
    page = client.get("/")            # like typing "/" in the address bar
    assert page.status_code == 200    # the page loaded
    assert b"Artist name" in page.data  # the form's label is on the page


# ---- My checks ----
# "monkeypatch" swaps get_artworks for a fake function, so these tests
# don't need the internet and we control exactly what the "API" returns.
import app as app_module


def test_empty_search_shows_message(monkeypatch):
    # Check 2: search for nothing -> see a message, and the API is NOT called
    called = []
    monkeypatch.setattr(app_module, "get_artworks", lambda a: called.append(a) or [])
    page = app.test_client().post("/results", data={"artist": "   "})
    assert b"No search term entered." in page.data
    assert called == []


def test_monet_search_shows_title_date_image(monkeypatch):
    # Check 3: a normal search shows title, date and the image URL from prompt.md
    fake = [{"id": 1, "title": "Water Lilies", "artist_title": "Claude Monet",
             "date_display": "1906", "image_id": "abc123"}]
    monkeypatch.setattr(app_module, "get_artworks", lambda a: fake)
    page = app.test_client().post("/results", data={"artist": "Monet"})
    assert b"Water Lilies" in page.data
    assert b"1906" in page.data
    assert b"https://www.artic.edu/iiif/2/abc123/full/843,/0/default.jpg" in page.data


def test_api_error_shows_friendly_message(monkeypatch):
    # Check 4 (HW4 "API failure" state): if the API breaks, the user sees a
    # friendly message, not the raw Python error text
    def broken(artist):
        raise Exception("HTTPSConnectionPool(host='api.artic.edu'): Read timed out")
    monkeypatch.setattr(app_module, "get_artworks", broken)
    page = app.test_client().post("/results", data={"artist": "Monet"})
    assert page.status_code == 200
    assert b"HTTPSConnectionPool" not in page.data


def test_made_up_word_shows_no_results():
    # Check 5 (HW4 "no results" state, uses the REAL API): a word that is not
    # an artist should show "No results found."
    page = app.test_client().get("/results?artist=xyzqwertyblorp")
    assert b"No results found." in page.data
