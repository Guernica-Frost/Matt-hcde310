# API Fair Guide: Open Library Search API

## What it is + why a designer might care

[Open Library](https://openlibrary.org) is a free, open catalog of books run by the Internet Archive. Its Search API lets you send a title, an author, or any keywords and get back matching books as JSON, with fields such as title, author names, and first publish year. You don't need an API key or an account. A designer might care because book data is behind many everyday experiences, like reading lists, book clubs, library visits, and gift ideas, and this API lets designers prototype those with real data in a few lines of Python.

Docs: https://openlibrary.org/dev/docs/api/search

## Setup (tested)

From the repo folder, in the venv:

```
source .venv/bin/activate
python3 -m pip install requests
cd R1
python3 example.py
```

No API key and no .env file are needed.


**Two things to point out when presenting:**

1. **`fields` and `limit` keep the response small.** Without them, every book comes back with dozens of fields. Here we ask only for what we print, and only 5 results.
2. **The first result is spam.** Open Library is edited by the public, like a wiki, so someone changed a real record's title to an ad. The API returns it anyway. Don't assume API data is clean just because it came from a "real" source.

## Gotchas

**Rate limits:** Open Library allows 1 request per second, or 3 per second if you send a 'User-Agent' header with your app name and a contact email. Breaking the limit "may result in aggressive rate limiting or blocking", so send the header, don't call the API in a fast loop, and use 'limit' to get many books in one request.

**Missing data:** When I asked for 100 "the hobbit" results, 9 had no 'author_name' and 2 had no 'first_publish_year'. Those keys are simply left out, so 'book["author_name"]' would crash. Use '.get()' with a default instead. Also, 'author_name' is a list even when there is one author, and the data is edited by the public, so records can be wrong.

**Confusing docs:** The rate limits are on a different page from the parameters. The docs don't list which fields come back by default, and if you misspell a field name in 'fields', the API doesn't give an error. It just leaves that field out. The search returns *works* (a book) rather than *editions* (one printing of it), so the year is when the book was first published, not when a particular copy was. Print the real response and check the field names yourself.

## Design angle

**Project idea:** a "Book Club Picker" where each member types a half-remembered title or author, the app finds the full record, and the group votes on a shortlist.

**Ethical/UX consideration:** because the data is crowd-edited, the app could show spam or wrong info as if it were trustworthy, which may confuse users. I think a godd design should leave a place for users reporting a bad or wrong return result and hide them.

## AI use

AI helped me draft this 'guide.md'. I chose the API to use and write 'app.py' to ensure the api query runs correctly.
