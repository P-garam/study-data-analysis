# read CSV file as dataframe
import pandas as pd
import os

base_path = os.path.dirname(__file__)  # 현재 파이썬 파일 위치
file_path = os.path.join(base_path, "서울특별시교육청남산도서관 장서 대출목록 (2025년07월).csv")

df = pd.read_csv(file_path, encoding='EUC-KR', low_memory=False)

#print(df.head())

csv_path = os.path.join(base_path, "ns_20250820.csv")

df.to_csv(csv_path)

with open(csv_path) as f:
    for i in range(3):
        print(f.readline(), end="")

ns_df = pd.read_csv(csv_path, index_col=0, low_memory=False)
print(ns_df.head())