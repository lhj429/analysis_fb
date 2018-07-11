import os
import json
from datetime import datetime, timedelta
from .api import api

def preprocess_post(post):
    # 공유수
    if 'shares' not in post:    # not in : 딕셔너리 오버로딩 (post가 딕셔너리라서 가능함)
        post['count_shares'] = 0    # shares가 없을 때 디폴트 값 처리
    else:
        post['count_shares'] = post['shares']['count']

    # 전체 리액션 수
    if 'reactions' not in post:
        post['count_reactions'] = 0
    else:
        post['count_reactions'] = post['reactions']['summary']['total_count']

    # 전체 코멘트 수
    if 'comments' not in post:
        post['count_comments'] = 0
    else:
        post['count_comments'] = post['comments']['summary']['total_count']

    # KST = UTC + 9
    kst = datetime.strptime(post['created_time'], '%Y-%m-%dT%H:%M:%S+0000')   # strptime : 시간 포맷팅 (문자열 -> 날짜/시간 변환)
    kst += timedelta(hours=9)
    post['created_time'] = kst.strftime('%Y-%m-%d %H:%M:%S')   # strftime : 시간 포맷팅 (날짜/시간 -> 문자열 변환)

def crawling(pagename, since, until, fetch=True, result_directory='', access_token=''):
    results = []
    filename = '%s/%s_%s_%s.json' %(result_directory, pagename, since, until)

    if fetch:
        for posts in api.fb_fetch_posts(pagename, since, until, access_token=access_token):
            for post in posts:
                preprocess_post(post)

            results += posts

        # save results to file(저장/적재)
        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)   # 리스트 -> json string 변환
            outfile.write(json_string)

    return filename


