# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealestateItem(scrapy.Item):
     name = scrapy.Field()
     market_cap = scrapy.Field()
     price = scrapy.Field()
     country = scrapy.Field()
     pass
