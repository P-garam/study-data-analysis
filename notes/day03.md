<경로 관리>
import os

base_path = os.path.dirname(__file__)  
file_path = os.path.join(base_path, "서울특별시교육청남산도서관 장서 대출목록 (2025년07월).csv")

- __file__ : 현재 실행 중인 Python 파일의 경로
- os.path.dirname(__file__) : 그 파일이 속한 폴더 경로
- os.path.join() : 파일명을 현재 폴더 경로에 붙여 절대경로 생성
-  이렇게 하면 상대경로 문제 없이 항상 현재 스크립트 위치 기준으로 파일을 읽거나 저장할 수 있음.

<CSV 읽기 (pd.read_csv)>
df = pd.read_csv(file_path, encoding='EUC-KR', low_memory=False)

- EUC-KR : 한글 인코딩 방식.
- utf-8로 하면 오류 날 수 있음 (UnicodeDecodeError)
- low_memory=False : 열 타입 추론 오류 방지용 (메모리 절약 대신 안정성 ↑)

<CSV 저장 (to_csv())>
csv_path = os.path.join(base_path, "ns_20250820.csv")
df.to_csv(csv_path)

- 현재 파일 위치 기준으로 새로운 CSV 파일을 저장함
- index=False를 추가하면 DataFrame 인덱스 열 생략 가능

<저장된 파일 일부 출력>
with open(csv_path) as f:
    for i in range(3):
        print(f.readline(), end="")

- 텍스트 파일처럼 한 줄씩 읽는 방식
- 저장된 내용이 제대로 기록되었는지 확인할 때 사용

<저장된 파일 다시 읽기>
ns_df = pd.read_csv(csv_path, index_col=0, low_memory=False)
print(ns_df.head())

- index_col=0 : 첫 번째 열(기존 DataFrame의 인덱스였던 값)을 인덱스로 다시 사용
- head() : 상위 5행 확인