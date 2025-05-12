
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from wordcloud import WordCloud
import re
import matplotlib.pyplot as plt
import time

def newsData():
    url=requests.get('https://media.naver.com/press/009/newspaper')
    html=bs(url.text)
    #print(html)
    #_persist_wrap
    #article_lst--title_only
    news=html.find('div',class_="_persist_wrap").find_all('a',class_="article_lst--title_only")
    # news=html.select('._persist_wrap .')
    # news=html.select('._persist_wrap .article_lst--title_only')
    # 짜고 , 짜면 ...  짜+ *
    # 맛있는 맛있고 ..... 맛있+  oo  ㅎㅎ ㅋㅋ
    #print(news)
    #for i in news:
        #print(i)
    list=[]
    for n in news:
        list.append([n.text.replace("\n",""),str(n).split("\"")[3]])
    print(list)

    content=[]
    count=1

    for i in list:
        content.append(str(i[0]+""))
    #print(content)
    #go_trans _article_content
        try:
           url=requests.get(i[1])
           print(i[1])
           html2=bs(url.text)
           content.append(str(html2.find('article',class_="go_trans _article_content").text+""))
           time.sleep(1)
           print("{}/{} 저장 완료".format(count,len(list)))
           count+=1
        except Exception as e:
            print("오류발생..."+str(count-1))

        #print(content)
    strr=''.join(s for s in content)
    box=re.findall("[\w]{2,}",strr)
    #print(box)
    dic={}
    for i in box:
      if i in dic:
        dic[i]+=1
      else:
        dic[i]=1
    wordcloud=WordCloud(font_path='c:/pydata/NanumGothic.ttf')
    pic=wordcloud.generate_from_frequencies(dic)
    plt.figure(figsize=(15,10))
    plt.imshow(pic)
    plt.axis('off')
    plt.show()

newsData()
