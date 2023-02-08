import scrapy
from scrapy.item import Item, Field


class QtechnoParserItem(scrapy.Item):
    model = Field()
    price = Field()
    url = Field()
