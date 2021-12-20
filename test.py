import feedparser
import json

website = 'https://sspai.com/feed'
rss = feedparser.parse(website)

print(len(rss.entries))
print(rss.encoding)
jsons = json.dumps(rss, ensure_ascii=False)
filename = 'test/1.json'
with open(filename, 'w', encoding='utf-8') as fileobject:
    fileobject.write(jsons)
fileobject.close()
