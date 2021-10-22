from sqlalchemy import create_engine
from scrapy.utils.project import get_project_settings
from sqlalchemy.sql.expression import table


def db_connect():
    return create_engine(get_project_settings().get("CONNECTION_STRING"), encoding='utf-8')


# def create_table(engine):
#     table_name = "googlenews"