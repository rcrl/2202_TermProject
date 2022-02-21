#1 패키지, 모듈 임포트
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
#
from konlpy.tag import Okt
from collections import Counter
import pytagcloud
import random
#
import time
#
from website import postWriting
from website import pngToUrl

#2 URL 준비
with open("news.txt", "r") as f:
        newsurl = f.read().split('\n')

#3 URL열기, xml 형태로 다운로드
list_url = []
list_xml = []
for _ in newsurl:
        list_url.append(urllib.request.urlopen(_).read())
for _ in list_url:
        try:
                list_xml.append(_.decode('utf-8'))
        except Exception as e:
                # print(e)
                list_xml.append(_.decode('euc-kr'))

#4 XML 객체를 변수에 저장
list_soup = []
for _ in list_xml:
        list_soup.append(BeautifulSoup(_, 'html.parser'))

#5 태그명과 일치하는 요소를 리스트로 저장
list_tag_title = []
list_tag_description = []
for _ in list_soup:
        list_tag_title.append(_.find_all("title"))
        list_tag_description.append(_.find_all("description"))

#6 문자열 형태로 리스트로 저장
list_title = []
list_description = []
for titles in list_tag_title:
        for title in titles[1:]:
                list_title.append( title.string )
for descriptions in list_tag_description:
        for description in descriptions[1:]:
                list_description.append( description.string )

#7 추출한 문자열 리스트를 하나의 문자열로 합치기
str_all = ""
for _ in list_title:
        str_all += _
for _ in list_description:
        str_all += _

#8 명사 추출 및 빈도 측정
okt = Okt()
count = Counter(okt.nouns(str_all))
tags = count.most_common(20)

#9 조사, 의미 없는 단어 등 필터링
str_meaningless = ""
for _ in tags:
       str_meaningless += _[0]
li = okt.nouns(str_meaningless)
keyword_list = []
for x in tags:
        for y in li:
                if( x[0] == y ):
                        keyword_list.append(x)
                        break
# print(keyword_list)

#10 워드클라우드 생성
r = lambda: random.randint(0,255)
color = lambda: (r(), r(), r())
dic = []
for n, c in keyword_list:
        dic.append({'color': color(), 'tag': n, 'size': c * 2})
pytagcloud.create_tag_image(dic, "wcloud.png", fontname='NanumBarunGothic')

#
print(__name__, time.asctime())

#
postWriting.load_url()
postWriting.post_posting()
