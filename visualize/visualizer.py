import pytagcloud
import os
import collections
import matplotlib.pyplot as plt

RESULT_DIRECTORY = '__results__/visulization'

def wordcloud(filename, wordfreq):
    taglist = pytagcloud.make_tags(wordfreq.items(), maxsize=80)
                        # make_tags : 태그 컬러, 사이즈 지정 / maxsize : 글자 크기 지정
                            # [{'color': (49, 209, 142), 'size': 92, 'tag': '오늘'}, {'color': (156, 139, 48), 'size': 82, 'tag': '일'},
                            #  {'color': (196, 89, 31), 'size': 24, 'tag': '국정원'}, {'color': (39, 209, 214), 'size': 24, 'tag': '후보'}]

    # print(taglist)
    save_filename = '%s/wordcloud_%s.jpg' %(RESULT_DIRECTORY, filename)
    pytagcloud.create_tag_image(taglist, save_filename, size=(900, 600), fontname='Malgun', rectangular=False, background=(0, 0, 0))
                # create_tag_image : 이미지로 저장

def graph_bar(title=None, xlabel=None, ylabel=None, showgrid=False, values=None, ticks=None, filename=None, showgraph=True):
    fig, subplots = plt.subplots(1, 1)
    subplots.bar(range(len(values)), values, align='center')    # x축, y축, 정렬

    # ticks
    if ticks is not None and isinstance(ticks, collections.Sequence):
        subplots.set_xticks(range(len(ticks)))
        subplots.set_xticklabels(ticks, rotation=80, fontsize='xx-small')

    # title
    if title is not None and isinstance(title, str):
        subplots.set_title(title)

    # xlabel
    if xlabel is not None and isinstance(xlabel, str):
        subplots.set_xlabel(xlabel)

    # ylabel
    if ylabel is not None and isinstance(ylabel, str):
        subplots.set_ylabel(ylabel)

    # show grid
    subplots.grid(showgrid)

    if filename is not None and isinstance(filename, str):
        save_filename = '%s/bar_%s.png' % (RESULT_DIRECTORY, filename)
        plt.savefig(save_filename, dpl=400, bbox_inches='tight')    # figure 저장 (filename, 해상도, 여백)

    # show graph
    if showgraph:
        plt.show()

if os.path.exists(RESULT_DIRECTORY) is False:
    os.mkdir(RESULT_DIRECTORY)