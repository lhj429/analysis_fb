# FB API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN = "EAACEdEose0cBAARXRjrPhh1IAvCYAm9QzzNUQ3YzrFxFQBm8NG8L3gSgtkHDPVQIz9CZCmxBVYZCbZBW1ULZBa1heBDgoZBA6rpT0DJNr2DtmsJYWl7ECSVfMC8sYWTrrzqSk5Xuy8sdgPZBof7ZBsM9Rv2yGZB8zWSuyjAq50v8YKWRZCTv9543ZBlGX1gCGX0PCvcqXs3cSBrReLvpKlPaZCLXZCnkOG6LyjVXvi0TpHdUdgZDZD"
# 도구 - 그래프 API 탐색기 - 사용자 액세스 토큰 받기
BASE_URL_FB_API = "https://graph.facebook.com/v3.0"


def fb_gen_url(base=BASE_URL_FB_API, node='', **params):    # url 생성
    url = '%s/%s/?%s' % (base, node, urlencode(params))     # node = 사용자, 사진, 페이지, 댓글과 같은 항목
    return url


def fb_name_to_id(pagename):                                # 서비스 페이지에서는 페이지 이름이 url에 쓰이지만 API url에서는 페이지 아이디를 사용해야 한다. (pageName -> pageID)
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    json_result = json_request(url=url)
    return json_result.get("id")


def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(node=fb_name_to_id(pagename) + "/posts",
                     fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
                     since=since,
                     until=until,
                     limit=50,
                     access_token=ACCESS_TOKEN)

    json_result = json_request(url=url)
    print(json_result)


'''
https://graph.facebook.com/v3.0/jtbcnews/posts/?
access_token=ca31sqw3&
since=20170101&
until=20171231&
limit=50&
fields=id,message,link.....

fb_gen_url(
        'https://graph.facebook.com/v2.0',
        'chosun', 
        since=20171231, 
        until=20181231)

https://graph.facebook.com/v3.0/jtbcnews/posts/?access_token=dfdfdfdfdfdfd
'''


