# API Fair Talk: Open Library Search API (~3 min)

## 1. What it is + why designers care (~30s)
- Free book catalog from the Internet Archive
- Search by title, author, or keywords and get JSON back
- No API key, no account

**Say:** "My API is the Open Library Search API. You search for a book and get back the title, the authors, and the year it was first published. It's free and you don't need a key, so it's easy to prototype things like reading lists or book clubs."

## 2. Setup (~20s)
- Show the terminal: `source .venv/bin/activate`, `pip install requests`
- Only one library: `requests`

**Say:** "Setup is simple. You only need the requests library. There's no key and no .env file."

## 3. Live example (~50s)
- Run `python3 app.py` on screen
- Point at the `params`: `q`, `fields`, `limit`
- Point at "Unknown author" in the last line

**Say:** "I search for 'the hobbit'. I use fields and limit so I only get the data I need, and only 10 books. Look at the last line: this book has no author, so my code prints 'Unknown author' instead of crashing."

**If the demo fails:** show a screenshot of the output, or open the code in `guide.md` and explain it.

## 4. Gotchas (~40s)
- **Rate limits:** 1 request/second, 3 with a `User-Agent` header
- **Missing data:** some books have no author or year → use `.get()` with a default
- **Confusing docs:** two separate pages; a misspelled field gives no error

**Say:** "Three gotchas. First, you can only make one request per second, or three if you add a User-Agent header. Second, some books are missing fields, so always use .get(). Third, the docs are split across two pages, and if you spell a field wrong, the API just skips it without an error."

## 5. Design angle (~30s)
- Idea: "Book Club Picker": members type a half-remembered title, the group votes
- Concern: the data is edited by the public, so it can be wrong or spam

**Say:** "One project idea is a book club picker. One concern is that anyone can edit Open Library, so the app might show wrong information. A good design lets users report a bad result and hide it."

## 6. Wrap-up (~10s)
**Say:** "So: free, no key, easy to use, but check for missing data. My guide is posted in #api-fair. Thanks!"
