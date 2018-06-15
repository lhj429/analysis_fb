#from analysis_fb.collect import crawler as cw
#from collect import crawler as cw   # cmd에서 출력할 때
import collect
import analyze
import visualize

# version1
#if __name__ == '__main__':
#    cw.crawling("jtbcnews", '2017-01-01', '2017-12-31')

# cw.crawling("jtbcnews", '2017-01-01', '2017-12-31')

# version2
'''
    # 데이터 수집(collection)
    #collect.crawling("jtbcnews", '2017-01-01', '2017-12-31')
    for item in items:
        collect.crawling(**item)

    # 데이터 분석(analyze)

    # 데이터 시각화(visualize)
'''

if __name__ == '__main__':
    items = [
        {'pagename':'jtbcnews', 'since':'2017-01-01', 'until':'2017-12-31'},
        {'pagename':'chosun', 'since':'2017-01-01', 'until':'2017-12-31'}
    ]

# version3
    # 데이터 수집 (collect)
    for item in items:
        resultfile = collect.crawling(**item, fetch=False)
        item['resultfile'] = resultfile

    # 데이터 분석 (analyze)
    # for item in items:
    #     print(item['resultfile'])
    for item in items:
        data = analyze.json_to_str(item['resultfile'], 'message')
        item['count_wordfreq'] = analyze.count_wordfreq(data)
        # print(item['count_wordfreq'])

    # 데이터 시각화 (visualize)
    for item in items:
        count = item['count_wordfreq']
        # count_m50 = count.most_common(50)      # tuple의 list 형태로
        count_m50 = dict(count.most_common(50))     # dict 형태로
        # print(count_m50)

        filename = '%s_%s_%s' % (item['pagename'], item['since'],  item['until'])         # 이미지 저장할 파일
        visualize.wordcloud(filename, count_m50)
        # visualize.graph_bar()