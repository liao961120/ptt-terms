# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertiesItem(scrapy.Item):
    # Primary fields
    title = scrapy.Field()
    author = scrapy.Field()
    bold = scrapy.Field()
    bracket = scrapy.Field()
    link_new = scrapy.Field()
    link_redr = scrapy.Field()
    link_title = scrapy.Field()
    
    
    
    # Housekeeping fields
    url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    date = scrapy.Field()
