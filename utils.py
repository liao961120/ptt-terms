import json


def to_publish_format(dict_data):
    out = {}
    for page in dict_data:
        url = get_url(page)
        for cat, items in page.items():
            if items is None or cat == 'url' or cat == 'date': continue
            
            for item in items:
                item = item.strip()
                if len(item) > 1:
                    if item not in out:
                        out[item] = { 
                            'category': [cat],
                            'src': [url]
                        }
                    else:
                        out[item]['category'].append(cat)
                        out[item]['src'].append(url)
    out = sorted( ((item, ', '.join(set(d['category'])), list(set(d['src'])) ) for item, d in out.items()), reverse=True)

    return out


def write_urls_to_crawl(dict_path, extracted_links_path, out='urls_to_crawl.json'):
    with open(dict_path) as f:
        data = json.load(f)
        requested = set( x['url'][0] for x in data if 'url' in x )
    with open(extracted_links_path) as f:
        extracted = set(l.strip() for l in f)
    with open(out, "w") as f:
        links = list(extracted.difference(requested))
        json.dump(links, f)


def get_url(page):
    for src, items in page.items():
        if src == 'url':
            return items[0]
    raise Exception('No url found')
