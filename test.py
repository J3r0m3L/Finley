from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--log-level=OFF") # doesn't work
driver = webdriver.Chrome(options=chrome_options, service_log_path=os.devnull)
start_url = "https://www.marketwatch.com/story/inflation-softens-at-the-end-of-2022-and-clears-path-for-slower-fed-rate-hikes-11673530439?mod=home-page&mod=newsviewer_click"
driver.get(start_url)

test = driver.page_source
soup = BeautifulSoup(test, "html.parser")
for stock in soup.find_all("span", {"class": "symbol"}):
    print(stock.text)

divTag = soup.find_all("div", {"class": "change"})
for tag in divTag:
    tdTags = tag.find("bg-quote")
    print(tdTags.text)
driver.quit()

# span class="symbol"
# div class="change" inner element bg-quote inner text
'''
browser = webdriver.Firefox() # Need to figure out how to keep this minimized

url = "https://www.marketwatch.com/story/inflation-softens-at-the-end-of-2022-and-clears-path-for-slower-fed-rate-hikes-11673530439?mod=home-page&mod=newsviewer_click"
sada = browser.get(url)
time.sleep(10)
source = browser.page_source
soup = BeautifulSoup(source, "html.parser")

# <div class="element element--list referenced-tickers">
for stock in soup.find_all("span"): # interestingly this gets the span correctly
    print(stock)
exit()
# this also bypasses the one article rule
'''
'''
# Doesn't work
url = "https://www.marketwatch.com/story/10-simple-investments-that-can-turn-your-portfolio-into-an-income-dynamo-11673983541?mod=newsviewer_click"
req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(req).read()
print(webpage)
'''