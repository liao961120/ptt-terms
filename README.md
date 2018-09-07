[![Support Python Version](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/)
[![Support Scrapy Version](https://img.shields.io/badge/scrapy-1.5-orange.svg)](https://docs.scrapy.org/)


# PTT Wiki & Web Crawler

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

## Scraping [PTT Wiki](http://zh.pttpedia.wikia.com/wiki/)

See [`render-PTTdict.sh`](https://github.com/liao961120/PTT-scrapy/blob/master/render-PTTdict.sh) or [`PTTdict/`](https://github.com/liao961120/PTT-scrapy/tree/master/PTTdict) for details.


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

To modify the spider:
```bash
vim PTTweb/spiders/PTT.py
vim PTTweb/items.py
```


