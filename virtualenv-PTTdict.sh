#!/bin/bash

# Set Up virtualenv
virtualenv -p python3 .
source bin/activate
pip install scrapy

# Begin Crawling
cd PTTdict
bash run.sh
deactivate

# Construct dictionary with R
Rscript -e 'source("dict_constr.R")' 


