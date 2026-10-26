# In-class 6: NASA EPIC (photos of the whole Earth from space), with the key kept in .env
#
# 1. Load the key from .env (python-dotenv: load_dotenv(), then os.getenv("NASA_API_KEY"))
# 2. Call https://api.nasa.gov/EPIC/api/natural with your key as the api_key parameter,
#    and timeout=10 so it gives up instead of hanging if the server is slow
# 3. Check r.status_code before you use the data
# 4. The reply is a list of today's photos. Print the caption and the date of the first one

import os
import requests
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("NASA_API_KEY")
params = {"api_key": key}

url = "https://api.nasa.gov/EPIC/api/natural"
response = requests.get(url, params = params, timeout=10)

def newest_photo_date(photos):
    """Takes a list of photo dictionaries and returns the latest 'date' string."""
    newest = photos[0]
    for photo in photos:
        if photo["date"] >  newest["date"]:
            newest = photo
    return newest

# print(response.status_code)

if response.status_code == 200:
    photo = response
    print(response.json())
else:
    print(response.status_code, "error!")
