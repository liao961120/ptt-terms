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
├── run.sh         # scrapy crawl parameters
├── dict.json      # Auto-generated (output)
├── view.json      # Auto-generated (for viewing)
│
├── PTTdict/
│   ├── __init__.py
│   ├── items.py          # Set item fields
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── postprocess/
│   │   ├── __pycache__/
│   │   └── tidyup.py     # Clean scraped items (piplines)
│   ├── __pycache__/
│   ├── settings.py       # set item piplines
│   └── spiders/
│       ├── dict.py       # Spider
│       ├── __init__.py
│       └── __pycache__/
└── scrapy.cfg
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


