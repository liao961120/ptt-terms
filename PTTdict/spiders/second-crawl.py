# -*- coding: utf-8 -*-
import json
import scrapy
import datetime
from scrapy.linkextractors import LinkExtractor

URLS_TO_CRAWL = 'urls_to_crawl.json'

class DictSpider(scrapy.Spider):
    name = 'second_crawl'
    allowed_domains = ['pttpedia.fandom.com']
    start_urls = ['https://example.com']  # Dummy


    def parse(self, response):
        with open(URLS_TO_CRAWL) as f:
            urls = json.load(f)
        
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_item)


    def parse_item(self, response):
        yield {
            'title': response.xpath('//h1[@class="page-header__title"]/text()').extract_first(),
            'bold': response.css('p b::text').re(r'.{2,}'),
            'bracket': response.css('p::text').re(r'「[^(「|」)]{2,}」'),
            'link_new': response.css('p a.new::text').re(r'.{2,}'),
            'link_redr': response.css('a.mw-redirect::text').re(r'.{2,}'),
            'link_title': response.css('a[title]::text').re(r'.{2,}'),
            'url': [response.url],
        }