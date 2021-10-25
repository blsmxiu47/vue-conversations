import scrapy
from scrapy.selector import Selector
import requests
# import time

import googlenews_scrape.items as items

class GooglenewsSpider(scrapy.Spider):
    name = "googlenews"
    allowed_domains = ['news.google.com']
    # start_urls = ['https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en']
    start_urls = ['https://news.google.com/search?q=Wildfires%20when%3A1d&hl=en-US&gl=US&ceid=US%3Aen']

    def parse(self, response):
        # dev tmp
        print('googlenews - start parse')
        selector = Selector(response)
        item  = items.GooglenewsScrapeItem()

        query_results = selector.css('main > c-wiz > div:nth-of-type(1) > div')
        for result in query_results[:2]:
            article = result.css('article')[0]
            
            item['title'] = article.css('h3 > a::text').get()

            subheading = article.css('div > div')[0]
            item['source'] = subheading.css('a::text').get()
            item['time'] = subheading.css('time').attrib['datetime']

            article_href = article.css('a').attrib['href']

            if article_href:
                try:
                    # content_request = scrapy.Request(
                    #     url=response.urljoin(article_href)
                    # )
                    content_response = requests.get(response.urljoin(article_href))
                    item['content_url'] = content_response.url
                    item['content'] = content_response.content # In Bytes, for String use str()
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
            else:
                item['content_url'] = None
                item['content'] = None

            # dev tmp
            # print(item)
            yield item
                

            # For Google Search | News Tab version
            # yield scrapy.Request(
            #     url=response.urljoin(next_page),
            #     callback=self.parse
            # )
    # def parse_source_content(self, response):
    #     # function to scrape "main content" from source. This is a major task in and of itself, and we may start by using some open source library similar to node_unfluff
    #     # https://github.com/ageitgey/node-unfluff, so this will take place in the data transformation stage post-scrape
    #     yield response.body
