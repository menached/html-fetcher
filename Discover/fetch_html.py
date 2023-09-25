import requests
import time
import pprint
from bs4 import BeautifulSoup


# Fetch page 1
url = "https://discoversjds.com/property-search/?keyword&location=any&status=any&type=any&bedrooms=any&bathrooms=any&min-price=any&max-price=any&min-area&max-area"
filename = "page1.html"
response = requests.get(url)
with open(f"fetched/Discover/{filename}", "wb") as file:
    file.write(response.content)
    with open(f"fetched/Discover/{filename}", "r") as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
        filtered_articles = soup.find_all('article', class_='property-item')

        urls = []
        for article in filtered_articles:
            url = article.find('a')['href']
            urls.append(url)

        pprint.pprint(urls)
        time.sleep(3)
        # filtered_articles = soup.find_all('article', class_='property-item')

        # for article in filtered_articles:
            # print(article.prettify())  # or do something else with the filtered articles


        #print(result)
        #time.sleep(4)


# Fetch pages 2 to 20
for i in range(2, 21):
    url = f"https://discoversjds.com/property-search/page/{i}/?keyword&location=any&status=any&type=any&bedrooms=any&bathrooms=any&min-price=any&max-price=any&min-area&max-area"
    filename = f"page{i}.html"
    response = requests.get(url)
    with open(f"fetched/Discover/{filename}", "wb") as file:
        file.write(response.content)
        with open(f"fetched/Discover/{filename}", "r") as file:
            soup = BeautifulSoup(file.read(), 'html.parser')
            filtered_articles = soup.find_all('article', class_='property-item')

            urls = []
            for article in filtered_articles:
                url = article.find('a')['href']
                urls.append(url)

            pprint.pprint(urls)
            time.sleep(3)
