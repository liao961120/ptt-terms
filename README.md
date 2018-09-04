[![Support Python Version](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/)
[![Support Scrapy Version](https://img.shields.io/badge/scrapy-1.5-green.svg)](https://docs.scrapy.org/)

# PTT Web & Wiki Crawler

## Installation

This project uses [virtualenv](https://virtualenv.pypa.io/en/stable/).

Install **virtualenv**:
```bash
pip install virtualenv
```

Activate environment:
```bash
virtualenv -p python3 PTT-scrapy

cd PTT-scrapy
source bin/activate
pip install scrapy
```

## Scraping [PTT Web](https://www.ptt.cc/bbs/)

To scrape posts from **[Gossiping](https://www.ptt.cc/bbs/Gossiping/)**:
```bash
cd PTTweb

scrapy crawl PTT -s CLOSESPIDER_ITEMCOUNT=50 -o ptt.jl
```

To view scraped data:
```bash
cat ptt.jl | jq "." | less
```

To modify spider:
```bash
vim PTTweb/spiders/PTT.py
vim PTTweb/items.py
```

## Scraping [PTT Wiki](http://zh.pttpedia.wikia.com/wiki/)

Under Development



