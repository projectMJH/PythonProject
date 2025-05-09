#_*_ coding:utf-8 _*_
import urllib.request as req
from bs4 import BeautifulSoup #Jsoup
from urllib import parse
import json
url="https://python.bakyeono.net/data/movies.json"
text_data=req.urlopen(url).read().decode('utf-8')
print(text_data)
movies=json.loads(text_data)
print(movies)
for m in movies:
    print(m['title'])
    print(m['genre'])
    print(m['year'])
    actors=m['starring']
    for actor in actors:
        print(actor,end=" ")