from flask import Flask, render_template,request
from api import find_books

app = Flask(__name__)

@app.route("/")
def home():
   artworks = [{"title": "Lilies"},
               {"title": "Nighthawks"}]
   return render_template("home.html", artworks=artworks)

@app.route("/books")
def books():
   return render_template("books.html")

@app.route("/results")
def results():
   author = request.args.get("author_search", "")
   return render_template("results.html",
                          books=find_books(author))
