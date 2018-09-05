#!/bin/bash

if [[ -e dict.jl ]]; then rm -r dict.jl; fi

read -p "Enter max scraping items > " counts

scrapy crawl dict -s CLOSESPIDER_ITEMCOUNT=${counts} -o dict.jl

cat dict.jl | jq "." > out.txt

