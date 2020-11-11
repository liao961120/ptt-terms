#%% 
import os
import json

os.system('cp data/dict.json docs/dict.json')
with open("data/dict.json") as f:
    data = json.load(f)

#%%
out = set()
for page in data:
    for src, items in page.items():
        if items is None or src == 'url' or src == 'date': continue
        
        for item in items:
            item = item.strip()
            if len(item) > 2:
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
