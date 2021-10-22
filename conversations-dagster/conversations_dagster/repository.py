from dagster import repository

from conversations_dagster.graphs.say_hello import say_hello_job
from conversations_dagster.schedules.my_hourly_schedule import my_hourly_schedule
from conversations_dagster.sensors.my_sensor import my_sensor


@repository
def conversations_dagster():
    """
    The repository definition for this conversations_dagster Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [say_hello_job]
    schedules = [my_hourly_schedule]
    sensors = [my_sensor]

    return jobs + schedules + sensors
