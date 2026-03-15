import requests
from bs4 import BeautifulSoup


class WebScraper:

    def __init__(self, url):
        self.url = url

    def scrape_quotes(self):

        response = requests.get(self.url)

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("span", class_="text")

        print("\nScraped Quotes:\n")

        for q in quotes[:5]:
            print(q.text)