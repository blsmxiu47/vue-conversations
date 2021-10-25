from conversations_dagster.graphs.scraping import scrape


def test_say_hello():
    """
    This is an example test for a Dagster graph.

    For hints on how to test your Dagster graphs, see our documentation tutorial on Testing:
    https://docs.dagster.io/concepts/testing
    """
    result = scrape.execute_in_process()

    assert result.success
    # assert result.result_for_node("hello").output_values == {"result": "Hello, Dagster!"}
