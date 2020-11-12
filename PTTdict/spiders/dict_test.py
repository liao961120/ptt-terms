# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy.linkextractors import LinkExtractor


DENY_URLs = [r'\?veaction=edit', r'\?action=edit', r'/zh/wiki/%E7%89%B9%E6%AE%8A:', r'/zh/wiki/%E5%88%86%E9%A1%9E:']
RESTRICTED_CSS = ['.category-page__member-link', '.mw-redirect']

class DictSpider(scrapy.Spider):
    name = 'dict_test'
    allowed_domains = ['pttpedia.fandom.com']
    start_urls = [
        # 'https://pttpedia.fandom.com/zh/wiki/%E5%88%86%E9%A1%9E:PTT%E6%B5%81%E8%A1%8C%E7%94%A8%E8%AA%9E',  # 流行用語
        # 'https://pttpedia.fandom.com/zh/wiki/%E5%88%86%E9%A1%9E:PTT%E6%96%87%E5%8C%96',  # 鄉民文化
        # 'https://pttpedia.fandom.com/zh/wiki/%E5%88%86%E9%A1%9E:PTT%E6%B5%81%E8%A1%8C%E7%AC%A6%E8%99%9F',  # 流行符號
        # 'https://pttpedia.fandom.com/zh/wiki/%E5%88%86%E9%A1%9E:PTT%E5%9F%BA%E6%9C%AC%E7%94%A8%E8%AA%9E',  # 基本用語
        # 'https://pttpedia.fandom.com/zh/wiki/%E5%88%86%E9%A1%9E:PTT%E5%90%8D%E4%BA%BA',  # 名人
        # 'https://pttpedia.fandom.com/zh/wiki/%E5%88%86%E9%A1%9E:PTT%E7%9C%8B%E6%9D%BF',  # 看板
        # 'https://pttpedia.fandom.com/zh/wiki/%E5%88%86%E9%A1%9E:PTT%E4%BA%8B%E4%BB%B6',  # 事件
        # 'https://pttpedia.fandom.com/zh/wiki/%E5%88%86%E9%A1%9E:PTT%E7%9B%B8%E9%97%9C%E4%BA%8B%E7%89%A9',  # 相關事物\
        # 'https://pttpedia.fandom.com/zh/wiki/PTT%E7%9A%84%E5%90%84%E9%A1%9E%E6%96%87%E7%AB%A0',  # 各類文章
        
        # # 隨機頁面
        # 'https://pttpedia.fandom.com/zh/wiki/PTT%E6%94%BF%E6%B2%BB%E4%BA%BA%E7%89%A9%E7%B6%BD%E8%99%9F%E5%88%97%E8%A1%A8',
        # 'https://pttpedia.fandom.com/zh/wiki/%E5%8F%8D%E6%9C%8D%E8%B2%BF%E6%94%BB%E4%BD%94%E7%AB%8B%E6%B3%95%E9%99%A2%E8%88%87ptt',
        # 'https://pttpedia.fandom.com/zh/wiki/%E7%B4%AB%E7%88%86',
        #'https://pttpedia.fandom.com/zh/wiki/%E8%A1%9D%E7%B4%AB%E7%88%86%E4%BA%8B%E4%BB%B6',
        'https://pttpedia.fandom.com/zh/wiki/%E5%88%86%E9%A1%9E:2005%E5%B9%B4PTT%E4%BA%8B%E4%BB%B6'
    ]


    # Scraping an individual page
    #   See https://stackoverflow.com/questions/54138758/scrapy-python-getting-items-from-yield-requests/54140461
    def parse(self, response):
        queue_urls = response.meta.get('queue', None)

        # First case
        if queue_urls is None: queue_urls = []
        
        # Get new links on this page
        links = LinkExtractor(restrict_css=RESTRICTED_CSS, deny=DENY_URLs).extract_links(response)

        # Parse items if all links on this page are in queue 
        #   (i.e., no more new links to add to queue)
        if all_link_requested(links, queue_urls):
            print("\n\n\nAll requested!!!!!!!!!!!!!\n\n\n")
            for link in queue_urls:
                request = scrapy.Request(link, callback=self.parse_items)
                yield request
        else:
            for link in links:
                if link.url not in queue_urls:
                    queue_urls.append(link.url)
                    request = scrapy.Request(link.url, callback=self.parse)
                    request.meta['queue'] = queue_urls
                    yield request


    def parse_items(self, response):
        yield {
            'title': response.xpath('//h1[@class="page-header__title"]/text()').extract_first(),
            'bold': response.css('p b::text').re(r'.{2,}'),
            'bracket': response.css('p::text').re(r'「[^(「|」)]{2,}」'),
            'link_new': getall_xpaths(response.xpath('//p/a[@class="new"]/text()').re(r'.{2,}')),
            'link_redr': getall_xpaths(response.xpath('//a[@class="mw-redirect"]/text()')),
            'link_title': getall_xpaths(response.xpath('//a[@title]/text()'))
        }


def getall_xpaths(xpath):
    return [x.get() for x in xpath]

        
def all_link_requested(links, requested_links):
    requested_links = set(requested_links)
    
    req_num = 0
    for link in links:
        if link.url in requested_links: req_num += 1
    
    if req_num == len(links):
        return True
    return False