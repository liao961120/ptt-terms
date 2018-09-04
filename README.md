[![Support Python Version](https://img.shields.io/badge/Python-3-blue.svg)](https://www.python.org/)

[![Support Scrapy Version](https://img.shields.io/badge/scrapy-1.5.1-green.svg)]

# PTT Web & PTT wiki Crawler


## Installation

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
```


### Scraping [PTT Wiki](http://zh.pttpedia.wikia.com/wiki/)

Under Development



