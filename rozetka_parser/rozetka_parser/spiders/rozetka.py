import scrapy
import html
from ..items import PhoneSamsungItem


class PhonePider(scrapy.Spider):
    name = 'rozetka'
    start_urls = ['https://rozetka.com.ua/mobile-phones/c80003/producer=samsung;series=galaxy-s/']

    def parse(self, response):
        for link in response.css('div.goods-tile__colors a::attr(href)'):
            yield response.follow(link, callback=self.parse_phone)

    def parse_phone(self, response):
        phone_samsung_item = PhoneSamsungItem()
        phone_samsung_item = {
            'model': response.css('h1.product__title::text').get(),
            'price': html.unescape(response.css('p.product-prices__big::text').get()),
            'url': response.css('a.tabs__link::attr(href)').get()
        }
        yield phone_samsung_item
