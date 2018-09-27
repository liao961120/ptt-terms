# -*- coding: utf-8 -*-
import scrapy, datetime, socket
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urlparse, urljoin
from PTTdict.items import PropertiesItem


class DictSpider(CrawlSpider):
    name = 'dict'
    allowed_domains = ['zh.pttpedia.wikia.com']
    start_urls = [
        'http://zh.pttpedia.wikia.com/wiki/%E5%88%86%E9%A1%9E:PTT%E6%B5%81%E8%A1%8C%E7%94%A8%E8%AA%9E', # 流行用語
        'http://zh.pttpedia.wikia.com/wiki/%E5%88%86%E9%A1%9E:PTT%E6%96%87%E5%8C%96', # 鄉民文化
        'http://zh.pttpedia.wikia.com/wiki/%E5%88%86%E9%A1%9E:PTT%E6%B5%81%E8%A1%8C%E7%AC%A6%E8%99%9F', # 流行符號
        'http://zh.pttpedia.wikia.com/wiki/%E5%88%86%E9%A1%9E:PTT%E5%9F%BA%E6%9C%AC%E7%94%A8%E8%AA%9E', # 基本用語
        'http://zh.pttpedia.wikia.com/wiki/%E5%88%86%E9%A1%9E:PTT%E5%90%8D%E4%BA%BA', # 名人
        'http://zh.pttpedia.wikia.com/wiki/%E5%88%86%E9%A1%9E:PTT%E7%9C%8B%E6%9D%BF', # 看板
        'http://zh.pttpedia.wikia.com/wiki/%E5%88%86%E9%A1%9E:PTT%E4%BA%8B%E4%BB%B6', # 事件
        'http://zh.pttpedia.wikia.com/wiki/%E5%88%86%E9%A1%9E:PTT%E7%9B%B8%E9%97%9C%E4%BA%8B%E7%89%A9' # 相關事物
    ]

    # Rules for Horizontal & vertical crawling
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@id="mw-pages"]/*[contains(text(), "後200個")]')),
        Rule(LinkExtractor(restrict_xpaths='//*[@id="mw-pages"]//li'), callback='parse_item'),
    )

    
    # Scraping an individual page
    def parse_item(self, response):
        l = ItemLoader(item=PropertiesItem(), response=response)
        
        l.add_xpath('title', '//h1[@class="page-header__title"]/text()')
        l.add_xpath('bold', '//p/b/text()', re='.{2,}')
        l.add_xpath('bracket', '//p/text()', re='「[^(「|」)]{2,}」') # Match all words but '「' & '」' in 「 ... 」
        l.add_xpath('link_new', '//a[@class="new"]/text()', re='.{2,}')
        #l.add_xpath('link_redr', '//a[@class="mw-redirect"]/text()')
        
        # Housekeeping fields
        l.add_value('url', response.url)
        l.add_value('date', datetime.datetime.now())
    
        return l.load_item()
