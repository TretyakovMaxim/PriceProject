from scrapy.item import Item, Field


class PhoneSamsungItem(Item):
    model = Field()
    price = Field()
    url = Field()


