#!/bin/bash

if [[ -e dict.jl ]]; then rm -r dict.jl; fi

#read -p "Enter max scraping items > " counts

counts=${1}

if [ -z "$counts" ]; then counts=0; fi

scrapy crawl dict -s CLOSESPIDER_ITEMCOUNT=${counts} -s DOWNLOAD_DELAY=0.8  -o dict.jl

cat dict.jl | jq "." > out.txt

