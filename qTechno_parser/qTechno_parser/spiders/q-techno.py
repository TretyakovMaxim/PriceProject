import scrapy
import html
from ..items import QtechnoParserItem


class PhoneSpider(scrapy.Spider):
    name = 'q_techno'
    start_urls = ['https://q-techno.com.ua/ru/shop/telefony-mobil-nye']

    def parse(self, response):
        for link in response.css('div.product-name.m_b15 a::attr(href)'):
            yield response.follow(link, callback=self.parse_phone)

        next_page = response.css('#catalog-listing > div > div.toolbar-bottom.m_b50.clearfix > div > '
                                 'div.pager.clearfix > div > ol > li:nth-child(6) > a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_phone(self, response):
        phone_q_techno_item = QtechnoParserItem()  # !
        phone_q_techno_item = {
            'model': response.css('h1.dynamic-data-name::text').get(),
            'price': html.unescape(response.css('span.price::text').get()),
            'url': response.css('head > meta:nth-child(9)::attr(content)').get()
        }
        yield phone_q_techno_item
