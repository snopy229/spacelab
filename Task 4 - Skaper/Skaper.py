import requests
from bs4 import BeautifulSoup

def parser(url: str):
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text, "lxml")
    titles = soup.find_all("a", class_="title")
    prices = soup.find_all("h4", class_="price") 
    card_texts = soup.find_all("p", class_="description card-text") 

    for title, price, card_text in zip(titles, prices, card_texts):
        print(f"Title: {title.get('title')}; Price: {price.text.strip()}; Card text: {card_text.get_text().strip()}")

if __name__ == "__main__":
    for i in range(20):
        parser(url=f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={i}")