import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from numpy.random import randn
import numpy as np

def ex1():
    # plt.plot([1, 2, 3, 4], [10, 20, 30, 40])  # (x tick, y tick)
        # plot : 데이터 리스트로 line plot 생성
    plt.plot([10, 20, 30, 40])  # (auto x tick, y tick)
    plt.show()
        # show : 시각화 명령을 실제로 차트로 렌더링하고 마우스 움직임 등의 이벤트를 기다리라

def ex2():
    fig = plt.figure()
    sp1 = fig.add_subplot(2, 1, 1)
                    # subplot(행, 열, 순서)
    sp1.plot([1, 2, 3, 4], [10, 20, 30, 40])

    sp2 = fig.add_subplot(2, 1, 2)
    sp2.plot([1, 2, 3, 4], [100, 200, 300, 400])

    plt.show()

# 원래 Figure를 생성하려면 figure 명령을 사용하여 그 반환값으로 Figure 객체를 얻어야 한다.
# 그러나 일반적인 plot 명령 등을 실행하면 자동으로 Figure를 생성해주기 때문에 일반적으로는 figure 명령을 잘 사용하지 않는다.
# figure 명령을 명시적으로 사용하는 경우는 여러개의 윈도우를 동시에 띄워야 하거나(line plot이 아닌 경우), Jupyter 노트북 등에서(line plot의 경우) 그림의 크기를 설정하고 싶을 때이다.
# 그림의 크기는 figsize 인수로 설정한다.

# subplot 명령은 그리드(grid) 형태의 Axes 객체들을 생성하는데 Figure가 행렬(matrix)이고 Axes가 행렬의 원소라고 생각하면 된다.
# 예를 들어 위와 아래 두 개의 플롯이 있는 경우 행이 2 이고 열이 1인 2x1 행렬이다.
# subplot 명령은 세개의 인수를 가지는데 처음 두개의 원소가 전체 그리드 행렬의 모양을 지시하는 두 숫자이고 세번째 인수가 네 개 중 어느것인지를 의미하는 숫자이다.
# 따라서 위/아래 두개의 플롯을 하나의 Figure 안에 그리려면 다음처럼 명령을 실행해야 한다. 여기에서 숫자 인덱싱은 파이썬이 아닌 Matlab 관행을 따르기 때문에 첫번째 플롯을 가리키는 숫자가 0이 아니라 1임에 주의하라.
#
# subplot(2, 1, 1) - 여기에서 윗부분에 그릴 플롯 명령 실행
# subplot(2, 1, 2) -  여기에서 아랫부분에 그릴 플롯 명령 실행

def ex3():
    fig = plt.figure()

    sp1 = fig.add_subplot(2, 2, 1)
    # print(rand(50).cumsum())
    sp1.plot(randn(50).cumsum())     # cumsum : 누적합 / plot : 점

    sp2 = fig.add_subplot(2, 2, 2)
    sp2.hist(randn(1000), bins=20, color='k', alpha=0.3)     # hist : 히스토그램

    sp3 = fig.add_subplot(2, 2, 3)
    sp3.scatter(np.arange(100), np.arange(100)+3 *randn(100))    # scatter : 산포도

    plt.show()

def ex4():
    fig, subplot = plt.subplots(1, 1)
    subplot.plot([10, 20, 30, 40])
    plt.show()

def ex5():      # 여러 개의 subplot 간격 조절
    fig, subplots = plt.subplots(2, 2, sharex=True, sharey=True)    # x축, y축 공유
    for i in range(2):
        for j in range(2):
            subplots[i, j].hist(randn(100), bins=20, color='k', alpha=0.3)  # k : black / alpha : 투명도
    plt.subplots_adjust(wspace=0, hspace=0)     # subplot 간격 조절
    plt.show()

def ex6():      # 색상, 마커, 선 스타일
    fig, subplots = plt.subplots(1, 1)
    subplots.plot([1, 2, 3, 4], [10, 20, 30, 40], 'go--')   # g: green / o : 점 / -- : 선 스타일
    plt.show()

def ex7():      # ex6을 명시적으로 표현
    fig, subplots = plt.subplots(1, 1)
    subplots.plot([1, 2, 3, 4], [10, 20, 30, 40], color="g", linestyle="--", marker="o")
    plt.show()

def ex8():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot([1, 2, 3, 4], [10, 20, 30, 40], color="#335599", linestyle="solid", marker="v")
    plt.show()

def ex9():      # 하나의 subplot에 2개의 그래프
    fig, subplot = plt.subplots(1, 1)

    data = randn(50).cumsum()
    subplot.plot(data, color='black', linestyle='dashed', label='AAA')
    subplot.plot(data, color='blue', linestyle='steps-mid', label='BBB')

    plt.legend(loc='best')
    plt.show()

def ex10():     # x축 눈금 설정
    fig, subplot = plt.subplots(1, 1)
    subplot.plot(randn(1000).cumsum())
    subplot.set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])      # set_xticks : x축 눈금 변경
    plt.show()

def ex11():     # 제목, 축 이름, 눈금, 눈금 이름
    fig, subplot = plt.subplots(1, 1)
    subplot.plot(randn(1000).cumsum())
    subplot.set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
    subplot.set_xticklabels(['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'], rotation=30, fontsize='small')  # set_xticklabels : x축 눈금 이름 설정
    subplot.set_xlabel('Points')    # set_xlabel : x축 이름 설정
    subplot.set_title('Matplotlib Test')    # set_title : 그래프 제목 설정
    plt.show()

def ex12():     # 범례 설정
    fig, subplots = plt.subplots(1, 1)

    subplots.plot(randn(1000).cumsum(), 'k', label='one')
    subplots.plot(randn(1000).cumsum(), 'k-.', label='two')
    subplots.plot(randn(1000).cumsum(), 'k.', label='three')

    plt.legend(loc='best')
    plt.show()

def ex13():     # 한글 처리
    # font_filename = 'c:/Windows/fonts/malgun.ttf'
    # font_name = font_manager.FontProperties(fname=font_filename).get_name()
    # print(font_name)
    # font_options = {'family': 'Malgun Gothic'}
    # plt.rc('font', **font_options)
    # plt.rc('axes', unicode_minus=False)

    fig, subplots = plt.subplots(1, 1)

    subplots.plot(randn(1000).cumsum(), 'k', label='기본')
    subplots.plot(randn(1000).cumsum(), 'k--', label='대시')
    subplots.plot(randn(1000).cumsum(), 'k.', label='점')

    subplots.set_xticklabels(['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'], rotation=30, fontsize='small')
    subplots.set_xlabel('포인트')
    subplots.set_title('예제12 한글처리')
    plt.legend(loc='best')

    plt.show()


if __name__ == '__main__':
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
    # ex10()
    # ex11()
    # ex12()
    ex13()