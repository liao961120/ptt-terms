[![Support Python Version](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/)
[![Support Scrapy Version](https://img.shields.io/badge/scrapy-1.5-green.svg)](https://docs.scrapy.org/)

# PTT Web & PTT wiki Crawler


## Installation

### Dependencies

This repo is a self-contained [virtualenv](https://virtualenv.pypa.io/en/stable/) folder.
To run the crawler, all you need is to install **virtualenv** locally:
```bash
pip install virtualenv
```

Other dependencies (Python 3.6 & scrapy) are contained in the directory so don't need to be installed.


### Scraping [PTT Web](https://www.ptt.cc/bbs/)

To scrape posts from **[Gossiping](https://www.ptt.cc/bbs/Gossiping/)**:
```bash
source bin/activate
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


### Scraping [PTT Wiki](http://zh.pttpedia.wikia.com/wiki/)

Under Development



