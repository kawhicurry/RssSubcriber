import json
import re
from pymongo import MongoClient

# 端口为默认端口，不用管，连上就能用

client = MongoClient("39.101.192.198")
db = client["pythondb"]
collection = db["images"]

output = []
for i in collection.find():
    i["_id"] = re.findall("'(.*)'", i.get("_id").__repr__())[0]
    output.append(i)

with open("images.json", "w", encoding="UTF-8") as jf:
    jf.write(json.dumps(output, indent=2))
