from flask import Flask, render_template,request
from api import search_art

# create the Flask app
app = Flask(__name__)

# Show the search form so the user can enter an author name.
@app.route("/")
def home():
    return render_template("home.html")

# Handle the submitted search. Show results.html for matches, or home.html
# with a helpful message so the user can try another search.
@app.route("/results")
def results():
    # Trim whitespace so a spaces-only search counts as empty input.
    author = request.args.get("author_search", "").strip()

    # An empty search gets a message before any API request is made.
    if not author:
        return render_template("home.html", message="Please enter an author name and try again.")

    artworks = search_art(author)

    # None means the API request failed, so offer a message and the search form.
    if artworks is None:
        return render_template("home.html", message="We couldn't load the artworks. Please try again later.")

    # An empty list means the request succeeded but returned no artworks.
    if not artworks:
        return render_template("home.html", message="No artworks found. Check the author's spelling or try another author.")

    # Replace missing or empty fields with readable labels so each row is useful.
    for artwork in artworks:
        if not artwork.get("title"):
            artwork["title"] = "Unknown"
        if not artwork.get("artist_title"):
            artwork["artist_title"] = "Unknown artist"
        if not artwork.get("date_display"):
            artwork["date_display"] = "Date Unknown"

    return render_template("results.html", artworks=artworks, author=author)

# run the app in debug mode when this file is run directly
if __name__ == "__main__": app.run(debug=True)
