#!/bin/bash

ori_dir=$PWD

# Set Up virtualenv
virtualenv -p python3 .
source bin/activate
pip install scrapy

# Begin Crawling
cd PTTdict
bash run.sh  # Crawl website
deactivate

# Construct dictionary with R
cd data
Rscript dict_constr.R && Rscript -e 'rmarkdown::render_site(encoding = "UTF-8")'
cp -r docs/ $ori_dir

cd $ori_dir

