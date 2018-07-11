# FB API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

def fb_gen_url(node='', **params):    # url 생성
    base = "https://graph.facebook.com/v3.0"
    url = '%s/%s/?%s' % (base, node, urlencode(params))     # node = 사용자, 사진, 페이지, 댓글과 같은 항목
    return url

def fb_name_to_id(pagename, access_token=''):                                    # 서비스 페이지에서는 페이지 이름이 url에 쓰이지만 API url에서는 페이지 아이디를 사용해야 한다. (pageName -> pageID)
    url = fb_gen_url(node=pagename, access_token=access_token)
    json_result = json_request(url=url)                         # web_request - json_request
    return json_result.get("id")

def fb_fetch_posts(pagename, since, until, access_token=''):
    url = fb_gen_url(node=fb_name_to_id(pagename, access_token) + "/posts",   # fb_gen_url, fb_name_to_id
                     fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
                     since=since,
                     until=until,
                     limit=50,
                     access_token=access_token)

    isnext = True
    while isnext is True:
        json_result = json_request(url=url)

        paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')

        url = None if paging is None else paging.get('next')
        isnext = url is not None

        yield posts
