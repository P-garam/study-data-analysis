import os
import chardet # to find file encoding type

base_path = os.path.dirname(__file__)  # 현재 파이썬 파일 위치
file_path = os.path.join(base_path, "서울특별시교육청남산도서관 장서 대출목록 (2025년07월).csv")

# 1. 바이너리 모드로 파일 열기
with open(file_path, "rb") as f:
    rawdata = f.read(10000)  # 처음 10000바이트만 읽어도 충분

# 2. 바이트 데이터를 chardet에 전달
result = chardet.detect(rawdata)

# 3. 결과 확인
print(result)

with open(file_path, encoding='EUC-KR') as f:
    print(f.readline()) # print first line
    print(f.readline()) # print second line