from dagster import graph

from ops.fetch_data import scrape_googlenews

@graph
def scrape():
    """
    A graph definition. This example graph has a single op.

    For more hints on writing Dagster graphs, see our documentation overview on Graphs:
    https://docs.dagster.io/concepts/ops_graphs/graphs
    """
    scrape_googlenews()

scrape_job = scrape.to_job()
