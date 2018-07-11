#from analysis_fb.collect import crawler as cw
#from collect import crawler as cw   # cmd에서 출력할 때
import collect
import analyze
import visualize
from config import CONFIG

# def crawling(pagename, since, until, fetch=True, result_directory=''):

if __name__ == '__main__':

    # 데이터 수집 (collect)
    for item in CONFIG['items']:
        resultfile = collect.crawling(**item, **CONFIG['common'])
        item['resultfile'] = resultfile

    # 데이터 분석 (analyze)
    for item in CONFIG['items']:
        data = analyze.json_to_str(item['resultfile'], 'message')
        item['count_wordfreq'] = analyze.count_wordfreq(data)

    # 데이터 시각화 (visualize)
    for item in CONFIG['items']:
        count = item['count_wordfreq']
        count_m50 = dict(count.most_common(50))     # dict 형태로

        filename = '%s_%s_%s' % (item['pagename'], item['since'],  item['until'])         # 이미지 저장할 파일
        visualize.wordcloud(filename, count_m50)        # def wordcloud(filename, wordfreq): pytagcloud
        visualize.graph_bar(
            title='%s 빈도 분석' % (item['pagename']),
            xlabel='단어',
            ylabel='빈도수',
            values=list(count_m50.values()),    # 그래프의 y 값 : count_m50 딕셔너리의 values
            ticks=list(count_m50.keys()),        # 그래프의 x 값 : count_m50 딕셔너리의 keys
            showgrid=False,     # 격자 여부
            filename=filename,      # 파일로 저장
            showgraph=False)         # pop-up window 띄울지 여부