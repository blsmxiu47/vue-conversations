from dagster import schedule

from conversations_dagster.graphs.scraping import scrape


@schedule(cron_schedule="0 * * * *", job=scrape, execution_timezone="US/Pacific")
def hourly_schedule(_context):
    run_config = {}
    return run_config
