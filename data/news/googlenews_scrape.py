# import time
import requests, lxml
from bs4 import BeautifulSoup
# from selenium import webdriver

# topics = ['Wildfires']
topic = "wildfires"
date_range = "1d"
# languages = ['en-US']
# geos = ['US']


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
    "q": f'{topic} when:{date_range}',
    "hl": "en-US",
    "gl": "US",
    "ceid": "US%3Aen",
    # "tbm": "nws", # For News Tab of Google Search
}

try:
    response = requests.get("https://news.google.com/search?q=Wildfires%20when%3A1d&hl=en-US&gl=US&ceid=US%3Aen", headers=headers) # , params=params)
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print("Timeout:",errt)
except requests.exceptions.TooManyRedirects as errtmr:
    print("Too Many Redirects:",errtmr)
except requests.exceptions.RequestException as err:
    print("Sorry.. Some request exception occurred",err)


soup = BeautifulSoup(response.text, "lxml")
# print(type(soup))
query_results = soup.select('main > c-wiz > div:nth-of-type(1) > div')
# query_results = soup.select('main > c-wiz > div')
# query_results = soup.select('main > c-wiz > div[data-n-et] > div')
print(type(query_results))
print(len(query_results))

# test = soup.select('main c-wiz article h3 a')[0].get_text() # .find('a').get_text()
# print(len(test))
# print(test)

for result in query_results[:2]:
    # image = a.figure.img
    article = result.select('article')[0]
    # title = result.select('article h3 > a')[0].get_text()
    title = article.select('article h3 > a')[0].get_text()
    link = article.find('a', href=True)['href']
    subheading = article.select('div > div')[0]
    source = subheading.find('a').text
    time = subheading.find('time')['datetime']
    # print(title)
    # print(link)
    print(f'{title}\n{link}\n{source}\n{time}\n')