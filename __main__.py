#from analysis_fb.collect import crawler as cw
#from collect import crawler as cw   # cmd에서 출력할 때
import collect
import analyze
import visualize

if __name__ == '__main__':
    items = [
        {'pagename':'jtbcnews', 'since':'2017-01-01', 'until':'2017-12-31'},
        {'pagename':'chosun', 'since':'2017-01-01', 'until':'2017-12-31'}
    ]

    # 데이터 수집(collection)
    #collect.crawling("jtbcnews", '2017-01-01', '2017-12-31')
    for item in items:
        collect.crawling(**item)

    # 데이터 분석(analyze)

    # 데이터 시각화(visualize)

#if __name__ == '__main__':
#    cw.crawling("jtbcnews", '2017-01-01', '2017-12-31')

# cw.crawling("jtbcnews", '2017-01-01', '2017-12-31')