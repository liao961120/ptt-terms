# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertiesItem(scrapy.Item):

    # Primary fields
    author = scrapy.Field()
    category = scrapy.Field()
    title = scrapy.Field()
    board = scrapy.Field()
    datetime = scrapy.Field()
    

    # Calculated fields

    # Housekeeping fields
    url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    rtrv_date = scrapy.Field()
