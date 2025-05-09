import urllib.request as req
from bs4 import BeautifulSoup
from urllib import parse
import json
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
class MovieSystem:
    url=''
    def __init__(self):
        self.url="https://www.kobis.or.kr/kobis/business/main/searchMainDailyBoxOffice.do"
    def movie_list(self):
        #문자열로 웹 데이터 읽기
        text_data=req.urlopen(self.url).read().decode("utf-8")
        #JSON변경
        json_data=json.loads(text_data)
        for movie in json_data:
            print(movie['rank'],movie['movieNm'],
                   movie['genre'])

    def movie_detail(self,rank):
        text_data = req.urlopen(self.url).read().decode("utf-8")
        # JSON변경
        json_data = json.loads(text_data)
        for movie in json_data:
            if rank==movie['rank']:
                print("영화제목:" + movie['movieNm'])
                print("상영일:" + movie['startDate'])
                print("장르:" + movie['genre'])
                print("등급:" + movie['watchGradeNm'])
                print("상영시간:" + movie['showTm'])
                print("순위:" + str(movie['rank']))
                print("줄거리:" + movie['synop'])
    def movie_test(self,rank):
        text_data = req.urlopen(self.url).read().decode("utf-8")
        # JSON변경
        json_data = json.loads(text_data)
        for movie in json_data:
            if rank == movie['rank']:
                story=movie['synop']
                okt=Okt()
                # 스토리안에 명사만 추출
                noun=okt.nouns(story)
                print(noun)
                # 몇번인지 확인
                count=Counter(noun)
                print(count)

                noun_list=count.most_common(100)
                print(noun_list)

                for data in noun_list:
                    print(data)

                col=["단어","횟수"]
                list=pd.DataFrame(noun_list,columns=col)
                list_top=list.sort_values(by="횟수", ascending=False).head(10)
                #print(list_top)
                plt.figure(figsize=(20,10))
                plt.rc('font',family="Malgun Gothic")
                plt.bar(list_top['단어'],list_top['횟수'])
                plt.title('영화 분석')
                plt.show()

ms=MovieSystem()
ms.movie_list()
mno=int(input("영화 번호 선택:"))
ms.movie_test(mno)
