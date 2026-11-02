from flask import Flask, render_template,request
from api import search_art

# AI-written (pseudocode comments only)

# create the Flask app

# route "/": show home.html with the search form

# route "/results":
# get the search term from the form (request.args)
# strip spaces from the term
# if the term is empty: show results.html with an "enter a search word" message
# call search_art(term) to get the artworks
# if it returned None: show results.html with an "API error, try again later" message
# if the list is empty: show results.html with a "no results for <term>" message
# otherwise: show results.html with the term and the list of artworks

# in results.html: use a default for a missing field (no date, no image, no artist)

# run the app in debug mode when this file is run directly
