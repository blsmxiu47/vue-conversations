from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from googlenews_scrape.spiders.googlenews_spider import GooglenewsSpider

if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl('googlenews')
    process.start()