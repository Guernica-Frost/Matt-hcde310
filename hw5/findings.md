# HW5 findings

## 1. Drawing: one search for "Monet"
(photo here)

## 2. Two questions about the code
1. In app route, why using methods=["GET", "POST"], what's its use.
2. Why there's a [:10] at the end of the return statement. What's the use of this.

## 3. Checks (4 or more, at least 2 as pytest tests)
| # | Check | Pass or fail |
|---|---|---|
| 1 | Search with just spaces → should say "No search term entered." and not call the API. (pytest: 'test_empty_search_shows_message') | Pass |
| 2 | Search "Monet" → each result shows the title, the date, and the image using the URL from the prompt. (pytest: 'test_monet_search_shows_title_date_image') | Pass |
| 3 | If the API call breaks (e.g. timeout) → user should get a simple error message, not the raw Python error. (pytest: 'test_api_error_shows_friendly_message') | Fail. The page prints the whole error, like "HTTPSConnectionPool(host='api.artic.edu'): Read timed out". |
| 4 | Search a made-up word like "xyzqwertyblorp" → should show "No results found." (pytest: 'test_made_up_word_shows_no_results') | Fail. It shows 10 random artworks (Nighthawks, American Gothic...). With '_score' added, they score about 0.00003 vs about 130 for Monet, so the API never returns an empty list. |

## 4. AI review
What it found that I missed: `q` searches artwork metadata across multiple fields. Asking for `artist_title` in `fields` only controls what comes back. The app accepts every hit, which is how the made-up artist returned real paintings. Resolve the artist name and filter by artist ID before applying the ten-result limit. 

What it got wrong: It mentioned the last statement of debugging. It's a simple class project and the app runs locally. It's not a big deal for now, but when it comes to my future apps, I'll keep that in mind.

Answers to my two questions, in my own words: 
1. methods=["GET", "POST"] lets /results take both a URL search like ?artist=Monet (GET) and the form’s POST, and without it the form would get a 405 error.
2. [:10] just keeps the first 10 artworks (or fewer if there aren’t 10), as a backup in case the API sends more than limit asked for.

## 5. My fix
What was wrong: The app accepts every hit, which makes made-up artist returned real paintings result.
What I changed: I changed the new query to only search artist_title, match_phrase lets someone type either Monet or Claude Monet.
How I checked it works: I checked the changes by search Monet first, and then tried Claude Monet, which returns right artworks from the artist I searched. After that, I typed a make-up word in search bar and hit search. It returns nothing but error message.
Commit before: 1e2c332772db58c56c24109eec85f4e3b077b1f0  Commit after: (hash)

## 6. Can we ship it? (100–150 words)
Yes or no, and why: No. There are still some problems after my fix stopped made-up words from returning random paintings. The basic search work is fine now. What if the API times out or fails, the page shows the raw Python error, which looks broken and leaks details. The app also runs with debug=True, which shouldn’t go live. Artworks with no title show “None” as the heading. The form uses POST, so users can't bookmark, share or refresh a search. So I'll say there are still a couple days' work from shipping out. We need to fix the error message and debug mode first, rerun the tests, then ship.

One thing my HW4 does better: When API fails, my HW4 shows a message “We couldn’t load the artworks. Please try again later.” instead of the raw error, and it fills missing fields with “Unknown”.
One thing the AI's app does better: It shows the artwork images, with alt text, and "No image available" when there's no image.

AI use goes in `ai_use.md` (the five points on the AI Use Card).
