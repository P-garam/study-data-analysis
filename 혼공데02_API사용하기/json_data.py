import json

d = {"name" : "garam"}
print(d['name'])

d_str = json.dumps(d) # python dic -> json str
print(type(d_str))

d_2 = json.loads(d_str) # json str -> python dic

d4_str = """
[
    {"name" : "garam", "age" : "21"},
    {"name" : "yurim", "age" : "21"}
]
"""
d4 = json.loads(d4_str)

from io import StringIO
import pandas as pd
print(pd.read_json(StringIO(d4_str))) # str -> df

pd.DataFrame(d4) # dic -> df



