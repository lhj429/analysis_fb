# http test
from urllib.request import Request, urlopen
from datetime import *
import sys

try:
    url = 'http://www.naver.com'
    request = Request(url)
    resp = urlopen(request)
    resp_body = resp.read().decode("utf-8")
    print(resp_body)
except Exception as e:
    print('%s %s' %(e, datetime.now()), file=sys.stderr)