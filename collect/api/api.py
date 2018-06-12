# FB API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN = "EAACEdEose0cBALuXJ9WJqmS8bNxAqj0OoZAVfvbZCZCZAiXtv4jxt3SXZAS23h9q3i4uZCudcawmSOMKZA5BMDYCGf5yp2Uz67W2RpnJaBZBxMarpXabKZCq3OLu1dSaIEBmO05gTv1QSU8iGX8KV4ZA2mqCPs6mzTYZAncZAdpyENvYE9FLpreMz537v04JQMkMTJWGpWOpCyW3TN8rV4b63VrbuUxERVXx3kmLlZCmzLE5p3gZDZD"
# 도구 - 그래프 API 탐색기 - 사용자 액세스 토큰 받기
BASE_URL_FB_API = "https://graph.facebook.com/v3.0"

def fb_gen_url(base=BASE_URL_FB_API, node='', **params):    # url 생성
    url = '%s/%s/?%s' % (base, node, urlencode(params))     # node = 사용자, 사진, 페이지, 댓글과 같은 항목
    return url

def fb_name_to_id(pagename):                                    # 서비스 페이지에서는 페이지 이름이 url에 쓰이지만 API url에서는 페이지 아이디를 사용해야 한다. (pageName -> pageID)
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    json_result = json_request(url=url)                         # web_request - json_request
    return json_result.get("id")

def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(node=fb_name_to_id(pagename) + "/posts",   # fb_gen_url, fb_name_to_id
                     fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
                     since=since,
                     until=until,
                     limit=50,
                     access_token=ACCESS_TOKEN)

    #results = []
    isnext = True
    while isnext is True:
        json_result = json_request(url=url)
        paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')

        #results += posts
        url = None if paging is None else paging.get('next')
        isnext = url is not None

        yield posts
    #return results

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


