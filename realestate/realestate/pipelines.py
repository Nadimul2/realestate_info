# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class RealestatePipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='123456',
            database='real_estate'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS details""")
        self.curr.execute('CREATE TABLE details(name VARCHAR(250),share_price VARCHAR(250),market_capital VARCHAR(250),Country VARCHAR(250))')


    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute('INSERT INTO details VALUES(%s, %s, %s, %s)', (
            item['name'][0],
            item['price'][0],
            item['market_cap'][0],
            item['country'][0]
        ))
        self.conn.commit()
