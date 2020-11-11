#%% 
import os
import json

with open("data/dict.json") as f:
    data = json.load(f)
with open("docs/dict.json", "w") as f:
    json.dump(data, f, ensure_ascii=False)

#%%
out = set()
for page in data:
    for src, items in page.items():
        if items is None or src == 'url' or src == 'date': continue
        
        for item in items:
            item = item.strip()
            if len(item) > 1:
                out.add( (item, src) )
out = sorted(out, reverse=True)


#%%
# Save as json for web app
with open("docs/ptt-terms.json", "w") as f:
    json.dump(out, f, ensure_ascii=False)


# Save as tsv
with open("docs/ptt-terms.tsv", "w") as f:
    f.write('item\tsrc\n')
    for item, src in out:
        f.write(f'{item}\t{src}\n')
