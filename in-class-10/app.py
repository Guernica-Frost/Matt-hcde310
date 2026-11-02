# app.py: the routes for the books app.
# SKELETON: the whole path works (form → /results → results page) with fake data.
# Next: replace one piece at a time, and commit each time something works.
from flask import Flask, render_template, request   # request (Flask), not requests!
from api import get_books_real

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results")
def results():
    # 1. Read the search term from the form
    author = request.args.get("author_search", "")

    # 2. Empty input? → home page + message (check BEFORE calling the API)
    if not author:
        return render_template("home.html", message="Please enter an author name and try again.")

    # 3. Call the API (fake data for now)
    books = get_books_real(author)

    # 4. API error? (get_books returned None) → home page + message
    if books is None:
        return render_template("home.html", message="We couldn't load the books. Please try again later.")

    # 5. No results, or nothing useful to show? → home page + message
    if not books:
        return render_template("home.html", message="No books found. Check the author's spelling or try another author.")

    # Missing fields? Use .get() so a missing key does not raise an error.
    for book in books:
        if not book.get("title") or book.get("first_publish_year") is None:
            return render_template("home.html", message="Some book details are missing. Please try another author or search again later.")


    # 6. Otherwise → results page
    return render_template("results.html", books=books, author=author)
