from dagster import op
from scraping import CrawlSources


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
    CrawlSources()