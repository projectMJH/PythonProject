import urllib.request as req
from bs4 import BeautifulSoup
from urllib import parse
import json
# 공공 데이터 => XML / JSON / CSV => 교통 시스템
url='https://www.kobis.or.kr/kobis/business/main/searchMainDailyBoxOffice.do'
text_data=req.urlopen(url).read().decode("utf-8")
print(text_data)
json_data=json.loads(text_data)
for movie in json_data:
    print("영화제목:"+movie['movieNm'])
    print("상영일:"+movie['startDate'])
    print("장르:"+movie['genre'])
    print("등급:"+movie['watchGradeNm'])
    print("상영시간:"+movie['showTm'])
    print("순위:"+str(movie['rank']))
    print("줄거리:"+movie['synop'])
