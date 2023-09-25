import os
import time
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

save_directory = "fetched/Trinity"
base_url = "https://trinityrealestatenicaragua.com/for-sale/"

def main():
    crawl_main_web_page(base_url)
    #crawl_web_page(base_url)
    #print(url)


def crawl_main_web_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        save_web_page(url, html_content)
        
        # Parse the HTML content
        soup = BeautifulSoup(html_content, "html.parser")

        # Find all <a> tags with href attribute
        links = soup.find_all("a", href=True)
        for link in links:
            # Get the absolute URL of the subpage
            subpage_url = urljoin(url, link["href"])
            # Ensure the subpage URL is within the same domain
            if urlparse(subpage_url).netloc == urlparse(url).netloc:
                # Crawl the subpage recursively
                #crawl_web_page(subpage_url)
                print(subpage_url)


# Function to save the web page as an HTML file
def save_web_page(url, content):
    parsed_url = urlparse(url)
    filename = parsed_url.netloc + parsed_url.path
    if parsed_url.query:
        filename += "?" + parsed_url.query
    if parsed_url.fragment:
        filename += "#" + parsed_url.fragment
    filename = filename.strip("/").replace("/", "_") + ".html"
    filepath = os.path.join(save_directory, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


main()
