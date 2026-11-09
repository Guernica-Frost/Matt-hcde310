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
What it found that I missed:
What it got wrong:
Answers to my two questions, in my own words:

## 5. My fix
What was wrong:
What I changed:
How I checked it works:
Commit before: (hash)  Commit after: (hash)

## 6. Can we ship it? (100–150 words)
Yes or no, and why:

One thing my HW4 does better:
One thing the AI's app does better:

AI use goes in `ai_use.md` (the five points on the AI Use Card).
