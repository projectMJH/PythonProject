#_*_ coding:utf-8 _*_
from bs4 import BeautifulSoup
import requests
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
"""
	<tr class="list hover">
		<td class="number">1</td>
		<td class="td-rank"><span class='rank'><span class=' rank-none '><span class="rank-txt">변동 없음</span></span></span></td>
		<td class="info">
			<a href="#" class="cover" onclick="fnViewAlbumLayer(83570761);return false;"><span class="mask"></span><img src="//image.genie.co.kr/Y/IMAGE/IMG_ALBUM/083/570/761/83570761_1682496044865_1_140x140.JPG" onerror="this.src='//image.genie.co.kr/imageg/web/common/blank_68.gif';" alt="앨범 제목이 들어갑니다." /></a>
			<a href="#" class="title ellipsis" title="새창 열림" onclick="fnPlaySong('101514417','1');return false;">Drowning</a>
			<a href="#" class="artist ellipsis" onclick="fnViewArtist(80619594); return false;">WOODZ</a>
		</td>
		<td class="btns"><a href="#" class="btn-basic btn-listen" title="새창 열림" onclick="fnPlaySong('101514417','1'); return false;">듣기</a></td>
		<td class="btns"><a href="#" class="btn-basic btn-add" title="새창 열림" onclick="fnPlaySong('101514417','3'); return false;">재생목록에 추가</a></td>
		<td class="more">
			<div class="toggle-button-box duplicate-add-album">
				<button type="button" class="btn btn-basic btn-more">더보기</button>
				<div class="list">
					<div class="duration ranking-1">
						<span class="ranking"><strong class="btn-radius">1위</strong>연속 3시간 째</span>
						<span class="top10"><strong class="btn-radius">TOP10</strong>연속 3시간 째</span>
					</div>
					<div id="svgContainer-1" class="svg-container"></div>
					<div class="time">
						<span class="hour">h</span>
<span>22</span><span>23</span><span>00</span><span>01</span><span>02</span><span>03</span><span>04</span><span>05</span><span>06</span><span>07</span><span>08</span><span>09</span>
					</div>
					<div class="ranking-link ranking-1">
						<span class="active">1위</span>
						<span>2위</span>
						<span>3위</span>
					</div>

					<div class="more-btns">
						<button type="button" id="add_my_album_101514417" class="btn-basic btn-album" songId=101514417 onclick="fnAddMyAlbumForm('#add_my_album_101514417','101514417',0,30);return false;">마이앨범에 담기</button>
						<a href="#" class="btn-basic btn-down" title="새창 열림" onclick="fnDownSong('101514417');return false;">다운로드</a>
					</div>
					<button type="button" class="close btn-close">닫기</button>
				</div>
			</div>
		</td>
	</tr>

"""
def genieMusic():
  headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  for page in range(1,5):
    url=f"https://www.genie.co.kr/chart/top200?ditc=D&ymd=20250509&hh=09&rtm=Y&pg={page}"
    music_data=requests.get(url,headers=headers)
    music_data=music_data.text
    #print(music_data)
    soup=BeautifulSoup(music_data,'html.parser')
    title=soup.select('.list-wrap .title')
    singer=soup.select('.list-wrap .artist')
    album=soup.select('.list-wrap .albumtitle')
    poster=soup.select('.list-wrap .cover img')
    for i in range(0,len(title)):
      print(title[i].text)
      print(singer[i].text)
      print(album[i].text)
      print(poster[i].attrs['src'])

#genieMusic()

def melonMusic():
  url="https://www.melon.com/chart/index.htm"
  music_data=requests.get(url)
  music_data=music_data.text
  print(music_data)

melonMusic()