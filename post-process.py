#%% 
import os
import json
from datetime import date
from utils import write_urls_to_crawl, to_publish_format

# Input
FIRST_CRAWL_DICT= 'data/first_crawl.json'
EXTRACTED_LINKS = "extracted_links.txt"
# Ouput
LAST_UPDATED = 'data/last-updated.json'
URLS_TO_CRAWL = 'urls_to_crawl.json'


with open(FIRST_CRAWL_DICT) as f:
    data = json.load(f)
with open(FIRST_CRAWL_DICT, "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=True)

with open(LAST_UPDATED, "w") as f:
    json.dump([str(date.today())], f)


write_urls_to_crawl(FIRST_CRAWL_DICT, EXTRACTED_LINKS, out=URLS_TO_CRAWL)
