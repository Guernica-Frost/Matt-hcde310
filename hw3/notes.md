# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?
data["data"][0]["title"]

## 2. Find 3 more fields you'd want to show a user, and their paths
Artist: data["data"][0]["artist_title"] 
Date: data["data"][0]["date_display"]
Medium: data["data"][0]["medium_display"]

## 3. Which fields are `null` for some works?
The artist_title field is null for the third artwork, "Baroque Pearl Mounted as a Cat Holding a Mouse"

## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*
The file gonna crash because varialbles url and params are empty. There'll be error when response function try to use these two paramters.

## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*
When I run the file, it asked me the search input. It crashed after I type "cat" and press enter. I think the bottom line is trying to remind me that variable url is empty without https://. The line caused the error is line16, where the response function is called.