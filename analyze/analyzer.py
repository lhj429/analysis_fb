import json
import re
from konlpy.tag import Twitter
from collections import Counter

def json_to_str(filename, key):
    jsonfile = open(filename, 'r', encoding='utf-8')    # 파일 읽기
    json_string = jsonfile.read()
    jsonfile.close()

    data = ''
    json_data = json.loads(json_string)     # 파이썬 객체로 만들어줌
    for item in json_data:
        value = item.get(key)
        if value is None:
            continue
        # print(value)

        data += re.sub(r'[^\w]', '', value)

    return data

def count_wordfreq(data):
    twitter = Twitter()
    nouns = twitter.nouns(data)

    count = Counter(nouns)
    return count