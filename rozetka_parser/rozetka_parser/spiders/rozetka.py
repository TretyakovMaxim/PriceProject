import scrapy
import html
from ..items import PhoneSamsungItem


class PhonePider(scrapy.Spider):
    name = 'rozetka'
    start_urls = ['https://rozetka.com.ua/mobile-phones/c80003/']

    def parse(self, response):
        for link in response.css('div.goods-tile__colors a::attr(href)'):
            yield response.follow(link, callback=self.parse_phone)

        next_page = response.css('a.button.button--gray.button--medium.pagination__direction.'
                                 'pagination__direction--forward.ng-star-inserted::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_phone(self, response):
        yield {
            'model': response.css('h1.product__title::text').get(),
            'price': html.unescape(response.css('p.product-prices__big::text').get()),
            'url': response.css('a.tabs__link::attr(href)').get()
        }

