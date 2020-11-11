[![Build Status](https://travis-ci.org/liao961120/PTT-scrapy.svg?branch=master)](https://travis-ci.org/liao961120/PTT-scrapy)
[![Support Python Version](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/)
[![Support Scrapy Version](https://img.shields.io/badge/scrapy-1.5-orange.svg)](https://docs.scrapy.org/)


## Modification

To modify the behavior of the spider,
edit the files marked with `#` in the directory tree below.

Directory structure of `PTTdict/`: 
```
.
├── run.sh                # scrapy crawl parameters
├── view.json             # Auto-generated (for viewing)
├── scrapy.cfg
├── setup.py
│
├── PTTdict
│   ├── __init__.py
│   ├── items.py          # Define item fields
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── postprocess
│   │   ├── __pycache__/
│   │   └── tidyup.py     # Process items before output
│   ├── __pycache__/
│   ├── settings.py       # Setting for item piplines
│   └── spiders
│       ├── dict.py       # Spider for scraping PTT wiki
│       ├── __init__.py
│       └── __pycache__/
└── data
    ├── dict_constr.R     # Filter & convert to data frame
    ├── index.Rmd         # Build Web Site
    ├── _site.yml
    └── style.css
```

