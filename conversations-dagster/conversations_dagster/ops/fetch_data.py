from dagster import op

# local src directory (reorg soon)
from conversations_fetcher.src.conversations_fetcher.news.googlenews_scrape.crawl_sources import crawl

@op
def hello():
    """
    An op definition. This example op outputs a single string.

    For more hints about writing Dagster ops, see our documentation overview on Ops:
    https://docs.dagster.io/overview/<TODO:INSERT OP URL>
    """
    return "Hello, Dagster!"


@op
def scrape_googlenews():
    crawl('googlenews')