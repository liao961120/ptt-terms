[![Build Status](https://travis-ci.org/liao961120/PTT-scrapy.svg?branch=master)](https://travis-ci.org/liao961120/PTT-scrapy)
[![Support Python Version](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/)
[![Support Scrapy Version](https://img.shields.io/badge/scrapy-1.5-green.svg)](https://docs.scrapy.org/)


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

```bash
cd PTTdict
bash run.sh
```

### Modification

To modify the behavior of the spider,
edit the files marked with `#` in the directory tree below.

Directory structure of `PTTdict/`: 
```
.
├── run.sh           # scrapy crawl parameters
├── view.json        # Auto-generated (for viewing)
├── scrapy.cfg
├── setup.py
│
├── PTTdict
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── postprocess
│   │   ├── __pycache__/
│   │   └── tidyup.py
│   ├── __pycache__/
│   ├── settings.py
│   └── spiders
│       ├── dict.py
│       ├── __init__.py
│       └── __pycache__/
└── data
    ├── dict_constr.R
    ├── index.Rmd
    ├── _site.yml
    └── style.css
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


