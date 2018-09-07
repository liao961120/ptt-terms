[![Build Status](https://travis-ci.org/liao961120/PTT-scrapy.svg?branch=master)](https://travis-ci.org/liao961120/PTT-scrapy)
[![Support Python Version](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/)
[![Support Scrapy Version](https://img.shields.io/badge/scrapy-1.5-orange.svg)](https://docs.scrapy.org/)


# PTT Wiki Crawler

## Scraping [PTT Wiki](http://zh.pttpedia.wikia.com/wiki/)

```bash
bash run.sh 10 0.7
# First para: number of items to scrape
# Second para: time interval between requests (unit = sec)
```

## Construct Word List & Build Site
```bash
cd data
Rscript dict_constr.R
Rscript -e 'rmarkdown::render_site(encoding = "UTF-8")'
```

### Modification

To modify the behavior of the spider,
edit the files marked with `#` in the directory tree below.

Directory structure of `PTTdict/`: 
```
.
├── run.sh              # scrapy crawl parameters
├── view.json           # Auto-generated (for viewing)
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
│       ├── dict.py     # Spider for scraping PTT wiki
│       ├── __init__.py
│       └── __pycache__/
└── data
    ├── dict_constr.R   # Filter & convert to data frame
    ├── index.Rmd       # Build Web Site
    ├── _site.yml
    └── style.css
```

