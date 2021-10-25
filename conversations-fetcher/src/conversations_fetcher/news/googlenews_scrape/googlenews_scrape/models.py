from sqlalchemy import create_engine, MetaData, Column, Integer, String, Text
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base
from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()


def db_connect():
    print(get_project_settings().get("CONNECTION_STRING"))
    return create_engine(get_project_settings().get("CONNECTION_STRING"), encoding='utf-8')


def create_table(engine):
    table_name = "googlenews"
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables.get(table_name)
    if table is None:
            DeclarativeBase.metadata.create_all(engine)
        # DeclarativeBase.metadata.drop_all(engine, [table], checkfirst=True)


class ConversationsBase(DeclarativeBase):
    __tablename__ = "googlenews"
    
    id = Column(Integer)
    title = Column('title', String(128), primary_key=True)
    source = Column('source', String(128), primary_key=True)
    time = Column('time', DateTime(timezone=False), primary_key=True)
    content_url = Column('content_url', String(256))
    content = Column('content', Text())
