import requests
from bs4 import BeautifulSoup
import re

class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited_urls = set()
        self.data = []

    def crawl(self, url):
        if url not in self.visited_urls:
            self.visited_urls.add(url)
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    self.parse_page(response.text)
                    # Find links to crawl next
                    self.find_links(response.text)
            except requests.exceptions.RequestException as e:
                print(f"Error crawling {url}: {e}")

    def parse_page(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        # Extract text from the page
        text = soup.get_text()
        cleaned_text = self.clean_text(text)
        self.data.append(cleaned_text)

    def clean_text(self, text):
        # Remove unwanted characters and whitespace
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s]', '', text)
        return text.strip()

    def find_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a', href=True):
            full_url = link['href']
            if full_url.startswith(self.base_url):
                self.crawl(full_url)

    def get_data(self):
        return self.data

# Example usage:
# crawler = WebCrawler('https://example.com')
# crawler.crawl('https://example.com')
# data = crawler.get_data()