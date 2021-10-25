import sys
from dagster import repository

from conversations_dagster.graphs.scraping import scrape
from conversations_dagster.schedules.hourly_schedule import hourly_schedule
# from .sensors.sensor import sensor

sys.path.append("C:\\Users\\weswa\\Projects\\vue-conversations\\conversations-dagster")

@repository
def conversations_dagster():
    """
    The repository definition for this conversations_dagster Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [scrape]
    schedules = [hourly_schedule]
    # sensors = [sensor]

    return jobs + schedules
