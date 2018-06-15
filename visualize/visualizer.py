import pytagcloud
import os

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

if os.path.exists(RESULT_DIRECTORY) is False:
    os.mkdir(RESULT_DIRECTORY)