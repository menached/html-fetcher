import os
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

def main():
    # Base URL of the webpage to crawl
    base_url = "https://trinityrealestatenicaragua.com/for-sale/"

    # Directory to store the crawled web pages
    save_directory = "web_pages"

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

# Function to crawl the webpage and save subpages
def crawl_web_page(url):
    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code == 200:
        # Extract the HTML content
        html_content = response.text

        # Save the current page
        save_web_page(url, html_content)
        #print("test")

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
                crawl_web_page(subpage_url)

main()