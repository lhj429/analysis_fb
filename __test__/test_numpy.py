import numpy as np

arr = np.arange(10) # arange : 반열린구간에서 step의 크기만큼 일정하게 떨어져 있는 숫자들을 array 형태로 반환 (start=0, stop=10, step=1)
print(type(arr))    # numpy.ndarray : 4차원 배열
print(arr)

arr = np.random.normal(5, 3, 500)   # np.random.normal(평균, 표준편차, 크기(행렬크기/인자 개수)
print(arr)

# 평균
print(arr.mean())

# 합계
print(arr.sum())

# 표준편차
print(arr.std())

# 분산
print(arr.var())

# 최대값
print(arr.max())

# 최소값
print(arr.min())

# 최대값, 최소값 위치
print(arr.argmax(), arr.argmin())