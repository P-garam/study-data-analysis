import os
base_path = os.path.dirname(__file__)  
file_path = os.path.join(base_path, "ns_book6.csv")
save_path = os.path.join(base_path, "ns_book7.csv")


import pandas as pd
ns_book6 = pd.read_csv('./혼공데03_데이터정제/ns_book6.csv', low_memory=False)

# 판닷스에서 몇 가지 기술통계를 자동으로 추출해주는 매서드
print(ns_book6.describe())

ns_book7 = ns_book6[ns_book6['도서권수']>0] # 실제로 없는 책의 데이터 빼고 다시 저장
print(ns_book7.describe(percentiles=[0.3, 0.6, 0.9])) # 30%, 60%, 90%에 위치한 값을 보고싶을때
print(ns_book7.describe(include='object')) # 열의 데이터타입이 수치가 아닌 다른 데이터타입 열의 기술통계를 보고싶을때

print(ns_book7['대출건수'].mean()) # 평균값
print(ns_book7['대출건수'].median()) # 중앙값
print(ns_book7['대출건수'].drop_duplicates().median()) # 중복값 제거하고 중앙값 구하기
print(ns_book7['대출건수'].mean()) # 최솟값
print(ns_book7['대출건수'].max()) # 최댓값
print(ns_book7['대출건수'].quantile(0.25)) # 분위수 구하기(0.25씩 건너뛰면 사분위수)

# 백분위 구하기 (특정 백분위수를 구할때는 불리언배열 이용해보기!)
borrow_10_flag = ns_book7['대출건수'] < 10 # 대출건수 열의 값이 10부다 작은지 비교하여 불리언배열 만들기
print(borrow_10_flag.mean()) # 10보다 작은 대출건수의 비율을 알 수 있음

print(ns_book7['대출건수'].var()) # 분산(데이터가 얼마나 퍼져있는지) 구하기
print(ns_book7['대출건수'].std()) # 표준편차(평균을 중심으로 데이터가 대략 얼만큼 떨어져 분포해있는지)
print(ns_book7['대출건수'].mode()) # 최빈값 // 텍스트, 수치형 모두 적용가능

print(ns_book7.mean(numeric_only=True)) # 데이터프레임의 모든 열 중, 수치형데이터 열에만 적용

ns_book7.to_csv(save_path, index=False)