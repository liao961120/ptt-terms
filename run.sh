#!/bin/bash

if [[ -e ./data/first_crawl.json ]]; then rm -r ./data/first_crawl.json; fi
if [[ -e ./data/second_crawl.jl ]]; then rm -r ./data/second_crawl.jl; fi
if [[ -e extracted_links.txt ]]; then rm extracted_links.txt; fi

#read -p "Enter max scraping items > " counts

counts=${1}
delay=${2}

if [ -z "$counts" ]; then counts=0; fi
if [ -z "$delay" ]; then delay=0.7; fi

# First crawl
printf "START FIRST CRAWL...\n\n"
scrapy crawl first_crawl -s CLOSESPIDER_ITEMCOUNT=${counts} -s DOWNLOAD_DELAY=0${delay} -o ./data/first_crawl.json
python3 post-process.py

# Second crawl 
printf "\n\nSTART SECOND CRAWL...\n\n"
# scrapy crawl second_crawl -s CLOSESPIDER_ITEMCOUNT=1 -o ./data/second_crawl.jl
scrapy crawl second_crawl -s CLOSESPIDER_ITEMCOUNT=${counts} -s DOWNLOAD_DELAY=0${delay} -o ./data/second_crawl.jl
python3 post-process-2.py