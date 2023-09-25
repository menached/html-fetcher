import requests

# Fetch page 1
url = "https://discoversjds.com/property-search/?keyword&location=any&status=any&type=any&bedrooms=any&bathrooms=any&min-price=any&max-price=any&min-area&max-area"
filename = "page1.html"
response = requests.get(url)
with open(f"fetched/{filename}", "wb") as file:
    file.write(response.content)

# Fetch pages 2 to 20
for i in range(2, 21):
    url = f"https://discoversjds.com/property-search/page/{i}/?keyword&location=any&status=any&type=any&bedrooms=any&bathrooms=any&min-price=any&max-price=any&min-area&max-area"
    filename = f"page{i}.html"
    response = requests.get(url)
    with open(f"fetched/{filename}", "wb") as file:
        file.write(response.content)
