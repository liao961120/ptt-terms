#!/bin/bash

if [[ -e dict.json ]]; then rm -r dict.json; fi

#read -p "Enter max scraping items > " counts

counts=${1}
delay=${2}

if [ -z "$counts" ]; then counts=0; fi
if [ -z "$delay" ]; then delay=0.8; fi

scrapy crawl dict -s CLOSESPIDER_ITEMCOUNT=${counts} -s DOWNLOAD_DELAY=0${delay}  -o dict.json

cat dict.json | jq "." > view.json

