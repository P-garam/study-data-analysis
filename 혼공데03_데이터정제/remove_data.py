import os
base_path = os.path.dirname(__file__)  
file_path = os.path.join(base_path, "ns_202104.csv")
file_path2 = os.path.join(base_path, "ns_book4.csv")

import gdown
gdown.download('https://bit.ly/3RhoNho', file_path, quiet=False)

import pandas as pd
ns_df = pd.read_csv(file_path, low_memory=False)
#print(ns_df.head())

# 슬라이싱을 이용하여 '번호' 열부터 '등록일자' 열까지 새로운 df
ns_book = ns_df.loc[:, '번호':'등록일자']
#print(ns_book.head())

# 번호~등록일자 사이에 '부가기호' 제거하기
#print(ns_df.columns) # ns_df의 열이름들을 확인하기
print(ns_df.columns[0]) # 숫자 인덱스로도 접근 가능함

selected_columns = ns_df.columns != '부가기호' # 열이름이 '부가기호'이 아닌 것을 표시하는 배열
ns_book = ns_df.loc[:, selected_columns]
#print(ns_book.head())

# drop() 사용해보기
ns_book = ns_df.drop(['부가기호', 'Unnamed: 13'], axis=1) #삭제하려는 열이름을 주고 axis를 1로 설정하면 삭제함
# 새 변수에 옮기지 않고 현재 데이터프레임을 바로 수정하기
ns_book.drop('주제분류번호', axis=1, inplace=True)

# dropna() 사용해보기
ns_book = ns_df.dropna(axis=1) # Nan이 하나라도 있는 행이나 열은 삭제
ns_book = ns_df.dropna(axis=1, how='all') # 모든 값이 Nan인 '열'을 삭제

# 행 삭제하기
ns_book2 = ns_book.drop([0,1]) # 0~1 인덱스의 행을 삭제

# []연산자와 슬라이싱
# []연산자에 슬라이싱이나 불리언배열을 전달하면 행을 선택함
ns_book2 = ns_book[2:] # 0,1 제와한 2 인덱스부터 끝까지 선택

# []연산자와 불리언 배열
selected_rows = ns_df['출판사'] == '한빛미디어' # ns_df 에서 출판사가 한빛미디어인 행만 True인 불리언 배열
ns_book2 = ns_book[selected_rows] # 선택된 행만을 포함하는 새 df

ns_book2 = ns_book[ns_book['대출건수'] > 1000] # 조건을 넣어서도 사용 가능

# 중복된 행 찾기
print(sum(ns_book.duplicated())) # 중복된 행이 있으면 True 즉 1이 되므로 sum 이용하면 개수를 알 수 있음

dup_rows = ns_book.duplicated(subset=['도서명', '저자', 'ISBN'], keep=False) # 도서명, 저자, ISBN을 기준으로 중복된 행들만 가져오기
ns_book3 = ns_book[dup_rows] # 빼놓은 중복된 행들의 인덱스를 넣기
# drop_duplicates() 매서드를 사용하면 중복된 행들을 삭제할 수 있음

# 그룹별로 모으기
# 도서명, 저자, ISBN, 권이 다 같은 행끼리는 합쳐버린다
count_df = ns_book[['도서명', '저자', 'ISBN', '권', '대출건수']] # 그룹으로 묶을 기준 열과 '대출건수'열만 선택(여러개의 열을 리스트로 주기)
group_df = count_df.groupby(by=['도서명', '저자', 'ISBN', '권'], dropna=False) # NaN이 포함된 행을 삭제하지 않고 진행
loan_count = group_df.sum() # 그룹으로 묶인 행들의 대툴건수 합치기

# 위 작업을 한 줄로 하면
loan_count = count_df.groupby(by=['도서명', '저자', 'ISBN', '권'], dropna=False).sum()

# 원본 데이터 업데이트하기
dup_rows = ns_book.duplicated(subset=['도서명', '저자', 'ISBN', '권']) # 중복된 행을 TRUE로 표시
unique_rows = ~dup_rows # 위 배열을 반전시켜 중복되지 않은 행이 TRUE가 되게 함
ns_book3 = ns_book[unique_rows].copy() # 원본 배열에서 중복되지 않은 행만 복사해서 새 배열에 넣기
print(sum(ns_book3.duplicated(subset=['도서명', '저자', 'ISBN', '권']))) # 중복된 행 없이 잘 됐는지 확인

ns_book3.set_index(['도서명', '저자', 'ISBN', '권'], inplace=True) # ns_book3인덱스를 loan_count인덱스와 동일하게 만듦
# 열이던것들이 인덱스가 된 것 (행으로)

ns_book3.update(loan_count) # loan_count를 이용해 ns_book3의 값을 업데이트

ns_book4 = ns_book3.reset_index() # 인덱스 설정했던 열들을 다시 돌려놓기 (그냥 열로)

print(sum(ns_book['대출건수']>100)) # 대출건수가 100회 이상인 책의 개수는?(중복된 도서가 합쳐지지 않음)
print(sum(ns_book4['대출건수']>100)) # 중복된 도서의 대출건수를 합쳤기 때문에 더 많아짐

# 원래 데이터와 수정한 데이터의 열 순서를 맞춰주기(내 편의를 위한거)
ns_book4 = ns_book4[ns_book.columns] # 원래 데이터의 열 이름을 그대로 전달하면됨

ns_book4.to_csv(file_path2, index=False)

# 위에서 했던 내용을 한 번에 처리하는 일괄처리함수 만들기
def data_cleaning(filename):
    # 파일을 데이터프레임으로 읽기
    ns_df = pd.read_csv(filename, low_memory=False)
    # NaN인 열 삭제
    ns_book = ns_df.dropna(axis=1, how=all)
    # 대출건수를 합치기 위해 필요한 행만 추출하여 count_df 데이터프레임 만들기
    count_df = ns_book[['도서명', '저자', 'ISBN', '권', '대출건수']]
    # 도서명, 저자, ISBN, 권을 기준으로 대출건수를 groupby하기
    loan_count = count_df.groupby(by=['도서명', '저자', 'ISBN', '권'], dropna=False).sum()
    # 원본 데이터프레임에서 중복된 행을 제외하고 고유한 행만 추출하여 복사
    dup_rows = ns_book.duplicated(subset=['도서명', '저자', 'ISBN', '권'])
    unique_rows = ~dup_rows
    ns_book3 = ns_book[unique_rows].copy()
    # 도서명, 저자, ISBN, 권을 인덱스로 설정
    ns_book3.set_index(['도서명', '저자', 'ISBN', '권'], inplace=True)
    # loan_count에 저장된 누적 대출건수를 업데이트
    ns_book3.update(loan_count)
    # 인덱스를 재설정
    ns_book4 = ns_book3.reset_index()
    # 원본 데이터프레임의 열 순서로 변경
    ns_book4 = ns_book4[ns_book.columns]

    result = ns_book4
    return result
