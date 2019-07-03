# -*- coding: utf-8 -*-
import scrapy


class PropertiesSpider(scrapy.Spider):
    name = "properties"
    allowed_domains = ["www.immoweb.be"]
    start_urls = [
        'https://www.immoweb.be/en/search/house/for-sale/tubize/1480?maxprice=300000',
    ]

    def parse(self, response):
        for property_url in response.css("#result > div > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(property_url), callback=self.parse_single_property)

    def parse_single_property(self, response):
        item = {}
        product = response.css("div#newpropertypage")
        item["title"] = product.css("#propertyPage-title .orange ::text").extract_first()
        yield item
