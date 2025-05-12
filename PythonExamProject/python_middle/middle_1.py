#_*_ coding:utf-8 _*_
# BS => 크롤링 = 셀리니움
import urllib.request as req
from bs4 import BeautifulSoup
import requests
'''
        <ul class="common_sp_list_ul ea4" style="padding:0 0 0 8px;">
            <li class="common_sp_list_li">
                <div class="common_sp_thumb">
                    <a href="/recipe/6987681" class="common_sp_link">
                                                    <span class="common_vod_label"><img src="https://recipe1.ezmember.co.kr/img/icon_vod.png"></span>
                                                <img src="https://recipe1.ezmember.co.kr/cache/recipe/2022/09/18/0d6e2ddd80f2e6fc3bc19da492471bc91_m.jpg">
                    </a>
                </div>
                <div class="common_sp_caption">
                                        <div class="common_sp_caption_tit line2">남은 자투리 식빵으로 갈릭버터 러스크 만들기</div>
                    <div class="common_sp_caption_rv_name" style="display: inline-block; vertical-align: bottom;">
                        <a href="/profile/recipe.html?uid=28205578"><img src="https://recipe1.ezmember.co.kr/img/df/pf_100_100.png">샐럽요리</a>
                    </div>
                    <div class="common_sp_caption_rv">
                                                <span class="common_sp_caption_buyer" style="vertical-align: middle;">조회수 746</span>
                    </div>
                </div>
            </li>
'''

def recipe():
  for page in range(1,10+1):
    url=f"https://www.10000recipe.com/recipe/list.html?order={page}"
    res_html=requests.get(url)
    # Document doc=Jsoup.connection().get()
    recipe_data=res_html.text
    #print(recipe_data)
    soup=BeautifulSoup(recipe_data,'html.parser')
    title=soup.select(".common_sp_caption .common_sp_caption_tit")
    chef=soup.select(".common_sp_caption_rv_name")
    img=soup.select(".common_sp_thumb .common_sp_link img")
    hit=soup.select(".common_sp_caption_buyer")
    #print(title)
    for i in range(0,len(title)):
      print(title[i].text)
      print(chef[i].text)
      print(hit[i].text)
      print(img[i].attrs['src'])

  """
    데이터 : text / attrs['속성명']
  """

recipe()