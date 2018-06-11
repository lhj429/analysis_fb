# FB API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN = "EAACEdEose0cBAHOC3djXuiZCRFYoJZCLMMhpTKPU0uZBfmksVSQND9La91VcDmmR7NrFxPkbYwCuEBhLxlbxkqh47oiAF2sVqUn189yGPc7gbaDrOVHMVAdxhAjWDkPYh5JobazqT9OO0uiFZBzll1M2qmV6xQfoVyTL4DeCfYnsloZCUUE6PkxFJUxKuZACkCi1Mka2SUve7I0Fkjwo30PLGky2RUZCepmZCf9jeb0h6AZDZD"
# 도구 - 그래프 API 탐색기 - 사용자 액세스 토큰 받기
BASE_URL_FB_API = "https://graph.facebook.com/v3.0"


def fb_gen_url(base=BASE_URL_FB_API, node='', **params):
    url = '%s/%s/?%s' % (base, node, urlencode(params))
    return url


def fb_name_to_id(pagename):
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


