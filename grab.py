from bs4 import BeautifulSoup
import requests


req = requests.get("https://www.marketwatch.com/latest-news")
soup = BeautifulSoup(req.text, "lxml")
for link in soup.find_all("a"):
    url = link.get("href")
    if url and "https://www.marketwatch.com/story" in url:
        req = requests.get(url)
        sub_soup = BeautifulSoup(req.text, "lxml")
        #print(sub_soup.prettify())
        #print("________________")
        print(url)
        exit()
        for stock in soup.find_all("span"):
            print(stock)
        exit()
