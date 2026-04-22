# not working on mac... test when you get home... if possible
import requests

url = "https://en.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "iiprop": "url",
    "titles": "File:Flag of the United Kingdom.svg"
}

session = requests.Session()
request = session.get(url=url, params=params)
raw_data = request.json()

pages = raw_data["query"]["pages"]

for value in pages.values():
    print(value["imageinfo"][0]["url"])
