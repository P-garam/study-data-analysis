import pandas as pd
ns_book7 = pd.read_csv('./혼공데04_데이터요약/ns_book7.csv', low_memory=False)
#print(ns_book7.head())

import matplotlib.pyplot as plt

# 산점도
#plt.scatter([1,2,3,4], [1,2,3,4]) # [x좌표], [y좌표]

#plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha=0.1) # alpha는 투명도

average_borrow = ns_book7['대출건수']/ns_book7['도서권수']
#plt.scatter(average_borrow, ns_book7['대출건수'], alpha=0.1)

# 히스토그램
#plt.hist([0,3,5,6,7,7,9,13], bins=5) # 데이터를 5개의 구간으로 나눈다는 뜻

import numpy as np
print(np.histogram_bin_edges([0,3,5,6,7,7,9,13], bins=5)) #다섯 구간의 경계값을 알아내기

np.random.seed(42)
random_samples = np.random.randn(1000) # 표준정규분포를 따르는 랜덤한 실수 1000개 생성
#plt.hist(random_samples)
#plt.show()

# 구간 조정하기
# 한 구간의 도수가 너무 큰 문제가 발생하면 y축을 로그스케일로 바꾸어 해결 가능
#plt.hist(ns_book7['대출건수'], bins=100) # 분포를 세밀하게 보기 위해 100개의 구간으로 나누기
#plt.yscale('log') # 기본적으로 상용로그를 이용함
#plt.show()

# 도서명의 길이 분포 보기
title_len = ns_book7['도서명'].apply(len)
#plt.hist(title_len, bins=100)
#plt.xscale('log') # 왼쪽에 편향된 그래프를 조정해주기
#plt.show()

# 상자 수염 그림 그리기
plt.boxplot(ns_book7[['대출건수', '도서권수']], vert=False) # vert=False로 하면 그림이 가로로 출력됨
# 그냥 출력하니 사분위수가 매우 작아서 상자가 거의 보이지 않음
plt.xscale('log')
plt.show()
# 기본적으로 수염의 길이는 IQR의 1.5배이나, whis= 매개변수로 길이를 조절할 수 있음

