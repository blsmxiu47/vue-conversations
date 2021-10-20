# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GooglenewsScrapeItem(scrapy.Item):
    title = scrapy.Field()
    source = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
