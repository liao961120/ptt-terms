import os
import json
from datetime import date

DATA_DIR = 'data'

with open(f"{DATA_DIR}/dict_test.jl") as f:
    data = [ json.loads(l) for l in f ]
with open(f"{DATA_DIR}/dict_test.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=True)