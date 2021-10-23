from sqlalchemy.orm import sessionmaker
from googlenews_scrape.models import ConversationsBase, db_connect, create_table

# DEV
# import logging

# logger = logging.getLogger("googlenews_spider")
# logger.setLevel(logging.WARNING)
# fh = logging.FileHandler('C:\\Users\\weswa\\Projects\\vue_conversations\\python_error_logs\\googlenews_spider.log')
# fh.setLevel(logging.WARNING)
# logger.addHandler(fh)
# end DEV


class GooglenewsScrapePipeline():
	def __init__(self):
		"""
		Initializes database connection and sessionmaker.
		Creates googlenews table if necessary.
		"""
        engine = db_connect()
        
        create_table(engine)
        
        self.Session = sessionmaker(bind=engine)


	def process_item(self, item, spider):
		"""
		Save scraped data in the database.
		"""
		session = self.Session()
		cb = ConversationsBase()
		cb.title = item['title']
		cb.source = item['source']
		cb.time = item['time']
		cb.content_url = item['content_url']
		cb.content = item['content']

		try:
			session.add(cb)
			session.commit()
		except UnicodeEncodeError as e:
			# logger.debug(e, exc_info=False)
			raise
		except:
			session.rollback()
			raise
		finally:
			session.close()
			
		return item
