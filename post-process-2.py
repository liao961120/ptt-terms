#%% 
import os
import json
from utils import to_publish_format

FIRST_CRAWL_DICT, SECOND_CRAWL_DICT = 'data/first_crawl.json', 'data/second_crawl.jl'
OUTPUT_DICT = 'data/dict.json'
OUTPUT_VUE, OUTPUT_TSV = 'data/ptt-terms.json', 'data/ptt-terms.tsv'


# Read data
with open(FIRST_CRAWL_DICT) as f:
    first = json.load(f)
with open(SECOND_CRAWL_DICT) as f:
    second = [ json.loads(l) for l in f ]
all_dict = first + second

# Combine data as dict format
with open(OUTPUT_DICT, "w") as f:
    json.dump(all_dict, f, ensure_ascii=False)


# Convert data to publish format
out = to_publish_format(all_dict)
# Save as json for web app
with open(OUTPUT_VUE, "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=True)

# Save as tsv
with open(OUTPUT_TSV, "w") as f:
    f.write('item\tcategory\tsrc\n')
    for item, category, src in out:
        f.write(f'{item}\t{category}\t{", ".join(src)}\n')
