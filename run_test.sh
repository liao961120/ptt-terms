#!/bin/bash

if [[ -e ./data/dict.json ]]; then rm -r ./data/dict.json; fi

#read -p "Enter max scraping items > " counts

counts=${1}
delay=${2}

if [ -z "$counts" ]; then counts=0; fi
if [ -z "$delay" ]; then delay=0.7; fi

scrapy crawl dict_test -o data/dict_test.jl

python3 test.py



