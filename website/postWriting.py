#
import requests
import time
import datetime
#
from website import pngToUrl
from bs4 import BeautifulSoup

#
def load_url():
    with open(r"C:\Users\USER\PycharmProjects\TermProject\website\postContent.html", "r", encoding='utf-8') as f:
        html_content = BeautifulSoup(f, 'html.parser')

    #
    try:
        url = pngToUrl.getImageUrl_ifh()
    except Exception as e:
        url = pngToUrl.getImageUrl_zpat()
    html_content.find('img')['src'] = url

    #
    html = html_content.prettify().encode('utf-8')
    with open(r"C:\Users\USER\PycharmProjects\TermProject\website\postContent.html", "wb") as f:
        f.write(html)

    #
    print(__name__, time.asctime())

#
def post_posting():
    url = "https://www.tistory.com/apis/post/write?access_token={access_token}&output={output_type}&blogName={blog_name}&title={title}&content={content}&visibility={visibility}&category={category_id}&published={published}&slogan={slogan}&tag={tag}&acceptComment={acceptComment}&password={password}"
    token = "d064aab2e1ce54057f50fda0556e7535_a2b184d3be3f1ab1e04e99d9eaf34f58"
    name = 'rcrl'
    cur_time = (time.asctime()).split()
    title = "{year}.{month}.{date} {day} {time}".format(year= cur_time[4], month= cur_time[1], date= cur_time[2], day= cur_time[0], time= cur_time[3] )
    categoryId = "1005938"
    with open(r"C:\Users\USER\PycharmProjects\TermProject\website\postContent.html", "r", encoding='utf-8') as f:
        content = f.read()

    url = url.format(access_token= token, output_type= 'json', blog_name= name, title= title, content= content, visibility= '0', category_id= categoryId, published=datetime.datetime, slogan= "", tag= "", acceptComment= "", password= "")

    s = requests.session()
    data = s.post(url)

    #
    print(__name__, time.asctime())
