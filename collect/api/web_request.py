from urllib.request import Request, urlopen
from datetime import *
import json
import sys

#def print_error(error):
#    print('%s %s' % (e, datetime.now()), file=sys.stderr)

def html_request(url='', encoding='utf-8', success=None, error=lambda e : print('%s %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)
        resp = urlopen(request)

        html = resp.read().decode(encoding)

        print('%s : success for request[%s]' %(datetime.now(), url))

        if callable(success) is False:
            return html

        success(html)
    except Exception as e:
        if callable(error) is True:
            error(e)

def json_request(url='', encoding='utf-8', success=None, error=lambda e : print('%s %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)
        resp = urlopen(request)
        resp_body = resp.read().decode(encoding)

        json_result = json.loads(resp_body)     # 파이썬 객체로 만들어줌

        print('%s : success for request[%s]' % (datetime.now(), url))

        if callable(success) is False:
            return json_result

        success(json_result)
    except Exception as e:
        if callable(error) is True:
            error(e)

# html = html_request(url='http://www.naver.com')
# html_request(url='http://www.naver.com', success=print_html) -- 비동기 통신 (성공하면 print_html 콜백)
# html_request(url='http://www.naver.com', success=print_html, error=error_my) -- 비동기 통신 (성공하면 print_html 콜백)

#html_request(url='http://www.naver.com')
#json_request(url='http://www.naver.com')