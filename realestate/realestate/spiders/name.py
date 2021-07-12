import scrapy
from ..items import RealestateItem

class NameSpider(scrapy.Spider):
    name = 'name'
    start_urls = ['https://companiesmarketcap.com/real-estate/largest-real-estate-companies-by-market-cap/?page=1']

    def parse(self, response):
        items = RealestateItem()

        heads = response.css('tr')
        for h in heads:
            items['name'] = h.css('.company-name::text').extract()
            items['market_cap'] = h.css('.name-td+ .td-right::text').extract()
            items['price'] = h.css('.td-right+ .td-right::text').extract()
            items['country'] = h.css('.responsive-hidden::text').extract()
            yield items
        next_page = 'https://companiesmarketcap.com/real-estate/largest-real-estate-companies-by-market-cap/?page=2'
        yield response.follow(next_page)