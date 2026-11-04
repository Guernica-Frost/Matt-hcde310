# Search Open Library for books and print title, author, and first publish year.
import requests

# term = input("Search the Art Institute for: ")
url = "https://openlibrary.org/search.json"
params = {"q": "the hobbit", "fields": "key,title,author_name,first_publish_year", "limit": 10}

headers = {"User-Agent": "hcde310-api-fair (chengs35@uw.edu)"}

response = requests.get(url, params=params, headers=headers, timeout=10)

if response.status_code != 200:
    print("Request failed:", response.status_code, response.reason)
else:
    data = response.json()
    books = data.get("docs", [])
    print("Total matches:", data.get("numFound", 0))
    if not books:
        print("No books found.")
    for book in books:
        title = book.get("title") or "Untitled"
        authors = ", ".join(book.get("author_name", ["Unknown author"]))
        year = book.get("first_publish_year") or "Unknown year"
        print(f"{title} - {authors} ({year})")
