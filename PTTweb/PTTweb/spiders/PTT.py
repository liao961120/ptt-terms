# -*- coding: utf-8 -*-
import scrapy, datetime, socket
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest, Request
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from PTTweb.items import PropertiesItem
from urllib.parse import urlparse, urljoin


class PTTSpider(CrawlSpider):
    name = 'PTT'
    allowed_domains = ['www.ptt.cc']
    
    # Start with over18 Request
    def start_requests(self):
        yield Request(url="https://www.ptt.cc/bbs/Gossiping/",
                      cookies={'over18': '1'})
        #yield Request(url="https://www.ptt.cc/bbs/baseball/",
        #              cookies={'over18': '1'})
                      
    # Rules for Horizontal and Vertical Crawling
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="action-bar"]//*[contains(text(), "上頁")]')),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="r-ent"]//div[@class="title"]'),
             callback='parse_item'),
    )
    

    def parse_item(self, response):
    
        l = ItemLoader(item=PropertiesItem(), response=response)

        l.add_xpath('author', '//*[@id="main-content"]/div[1]/span[2]/text()')
        l.add_xpath('title', '//*[@id="main-content"]/div[3]/span[2]/text()')
        l.add_xpath('datetime', '//*[@id="main-content"]/div[4]/span[2]/text()')
        l.add_xpath('board', '//*[@id="main-content"]/div[2]/span[2]/text()')
        
        
        l.add_xpath('category', '//*[@id="main-content"]/div[3]/span[2]/text()',
                    re='^\[.+\]')
        if len(l.get_collected_values('category')) == 0:
            l.add_xpath('category', '//*[@id="main-content"]/div[3]/span[2]/text()',
                        re='^Re')

        # Housekeeping fields
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('rtrv_date', datetime.datetime.now())

        return l.load_item() 
