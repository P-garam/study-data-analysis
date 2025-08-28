import os
base_path = os.path.dirname(__file__)  
file_path = os.path.join(base_path, "ns_book4.csv")
new_file = os.path.join(base_path, "ns_book5_update.csv")
next_file = os.path.join(base_path, "ns_book6.csv")

import pandas as pd
ns_book4 = pd.read_csv(file_path, low_memory=False)
#print(ns_book4.head())
#print(ns_book4.info()) # 데이터프레임 정보를 요약해서 출력

#print(ns_book4.isna().sum()) # NaN 값을 True로 나타내는 매서드에 합을 구하는 매서드를 이어 호출

# 누락된 값을 다른 값으로 바꾸기
set_isbn_na_rows = ns_book4['세트 ISBN'].isna() # 누락된 값들을 찾아 불리언 배열로 반환
ns_book4.loc[set_isbn_na_rows, '세트 ISBN'] = '' # set_isbn_na_rows의 세트 ISBN 값을 빈 문자열 ''로 바꾸기
print(ns_book4['세트 ISBN'].isna().sum()) # 누락된 값의 개수 세기 (빈 문자열로 대체했기 때문에 0이 될 것)

# 위 과정을 더 쉽게하는 매서드 fillna
ns_book4.fillna('없음') # ns_book4에 있는 모든 NaN을 '없음'문자열로 바꿈
ns_book4.fillna({'부가기호': '없음'}) # 특정 열의 NaN을 바꾸면서 전체 데이터프레임을 반환하기

# 또 다른 방법 (NaN이 아니어도 됨) 매서드 replace
# 1. 바꾸려는 값이 하나일 때
import numpy as np
ns_book4.replace(np.nan, '없음') # (원래 값, 새로운 값)으로 매개변수 주면 됨

# 2. 바꾸려는 값이 여러 개일 때
ns_book4.replace([np.nan, '2021'], ['없음', '21']) # ([원래값1, 원래값2], [새로운값1, 새로운값2])
ns_book4.replace({np.nan: '없음', '2021': '21'}) # 또는 딕셔너리 형식도 가능

# 3. 열 마다 다른 값으로 바꿀 때
ns_book4.replace({'부가기호': np.nan}, '없음') # '부가기호'열의 NaN을 '없음'으로 바꾸기
ns_book4.replace({'부가기호': {np.nan: '없음'},
                  '발행년도': {'2021': '21'}}) # 여러개를 한 번에 할 수도 있음

# 정규식 : 문자열 패턴을 찾아서 대체하기 위한 규칙의 모음
# 2021 -> 21 로 바꾸는 정규식 해보기!
# 정규표현식에서 숫자를 나타내는 기호는 /d 이다
# /d/d(/d/d)처럼 그룹가능, 그룹은 /1, /2 이렇게 표현
ns_book4.replace({'발행년도': {r'\d\d(\d\d)': r'\1'}}, regex=True)[100:102] # regex는 정규식을 사용한다는 의미
ns_book4.replace({'발행년도': {r'\d{2}(\d{2})': r'\1'}}, regex=True)[100:102] # 같은 정규표현식이 반복될경우 이렇게도 가능

# 문자 찾기
# 작가명 (지은이), 옮긴이명 (옮긴이) 에서 괄호 안에 있는 문자들만 없애기
print(ns_book4.replace({'저자': {r'(.*)\s\(지은이\)(.*)\s\(옮긴이\)': r'\1\2'},
                  '발행년도': {r'\d{2}(\d{2})': r'\1'}}, regex=True)[['저자', '발행년도']][100:102])

# 잘못된 값 바꾸기
#ns_book4.astype({'발행년도': 'int64'}) # 발행년도 열을 int64로 바꾸니 오류발생 -> 오류 보면 숫자가 아닌 문자가 있는듯
print(ns_book4['발행년도'].str.contains('1988').sum()) # 발행년도 열에 1988이라는 문자열이 포함된 행의 개수

# 모든 문자에 대응하는 정규표현은 \D이다.
invalid_number = ns_book4['발행년도'].str.contains('\D', na=True) # 발행년도 열에서 문자를 포함하는 열들을 찾기
print(invalid_number.sum()) # 문자가 들어간 행의 개수를 출력
print(ns_book4[invalid_number].head()) # 문자가 들어간 행 일부 출력해보기
# 정규표현식을 이용해 연도 앞뒤에 있는 문자들을 제거해보기
ns_book5 = ns_book4.replace({'발행년도':r'.*(\d{4}).*'}, r'\1', regex=True)

unknown_year = ns_book5['발행년도'].str.contains('\D', na=True) # 다시 발행년도열에 숫자 외의 문자가 들어간 행 찾기
print(unknown_year.sum()) # 개수 출력해보기

ns_book5.loc[unknown_year, '발행년도'] = '-1' # 나머지 값들은 뭔지 정확히 모르니 일단 -1로 바꾸기
ns_book5 = ns_book5.astype({'발행년도': 'int64'}) # 발행년도 열의 데이터 타입을 정수형인 int64로 바꾸기

# 4자릿수 숫자이지만 너무 크거나 작은 이상한 값 찾기
#print(ns_book5['발행년도'].gt(4000).sum()) # gt매서드 이용해 4000보다 큰 값의 개수 찾기(부등호도 가능)
dangun_yy_rows = ns_book5['발행년도'].gt(4000)
ns_book5.loc[dangun_yy_rows, '발행년도'] = ns_book5.loc[dangun_yy_rows, '발행년도'] - 2333
dangun_year = ns_book5['발행년도'].gt(4000)
print(dangun_year.sum()) # 단군기원에서 서기로 바꿔준 다음 다시 4000넘는거 확인
ns_book5.loc[dangun_year, '발행년도'] = -1 # 단군에서 서기로 바꿔도 너무 큰 애들은 -1로 변경

old_books = ns_book5['발행년도'].gt(0) & ns_book5['발행년도'].lt(1900) # 발행년도가 0보다 크고 1900보다 작은 행 찾기
ns_book5.loc[old_books, '발행년도'] = -1 # 그 행들도 -1로 채우기
print(ns_book5['발행년도'].eq(-1).sum()) # -1로 바뀐 행들이 몇 개 인지 보기

# 누락된 정보 채우기
ns_rows = ns_book5['도서명'].isna() | ns_book5['저자'].isna() \
        | ns_book5['출판사'].isna() | ns_book5['발행년도'].eq(-1) # 도서명, 저자, 출판사, 발행년도가 누락되거나 이상한 행 찾기
print(ns_rows.sum())

import requests
from bs4 import BeautifulSoup
# yes24에서 isbn으로 검색한 결과 페이지에서 도서명 태그 정보 가져오기
def get_book_title(isbn):
    # yes24 도서 검색 페이지 url
    url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'
    # url에 isbn을 넣어서 html가져오기
    r = requests.get(url.format(isbn))
    soup = BeautifulSoup(r.text, 'html.parser') # html 파싱
    # 클래스 이름이 'gd_name'인 <a> 태그의 텍스트를 가져옴
    title = soup.find('a', attrs={'class': 'gd_name'}).get_text()
    return title

print(get_book_title(9791191266054))

import re

def get_book_info(row):
    title = row['도서명']
    author = row['저자']
    pub = row['출판사']
    year = row['발행년도']
    # Yes24 도서 검색 페이지 url
    url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'
    # url에 isbn을 넣어서 html 가져오기
    r = requests.get(url.format(row['ISBN']))
    soup = BeautifulSoup(r.text, 'html.parser') # html 파싱

    try: # 예외가 발생할 수 있는 코드에 사용
        if pd.isna(title):
            # 클래스 이름이 'gd_name'인 <a> 태그의 텍스트를 가져온다
            title = soup.find('a', attrs={'class':'gd_name'}).get_text()
    except AttributeError: # 예외가 발생했을때 어떻게할지
        pass

    try:
        if pd.isna(author):
            authors = soup.find('span', attrs={'class':'info_auth'}).find_all('a')
            author_list = [auth.get_text() for auth in authors]
            author = ','.join(author_list)
    except AttributeError:
        pass

    try:
        if pd.isna(pub):
            pub = soup.find('span', attrs={'class':'info_pub'}).find('a').get_text()
    except AttributeError:
        pass

    try:
        if year == -1:
            year_str = soup.find('span', attrs={'class':'info_date'}).get_text()
            # 정규 표현식으로 찾은 값 중에 첫 번째 것만 사용
            year = re.findall(r'\d{4}', year_str)[0]
    except AttributeError:
        pass

    return title, author, pub, year

# 위 함수로 모든 열을 처리했을 경우의 파일을 코랩에서 다운받아 사용하기(실제로 하면 오래걸려서)
import gdown
gdown.download('https://bit.ly/3UJZiHw', new_file, quiet=False)
ns_book5_update = pd.read_csv(new_file, index_col=0)

ns_book5.update(ns_book5_update)
na_rows = ns_book5['도서명'].isna() | ns_book5['저자'].isna() | ns_book5['출판사'].isna() | ns_book5['발행년도'].eq(-1)
print(na_rows.sum())

# 어느정도 정제 했는데도 누락된 값은 지우기
ns_book6 = ns_book5.dropna(subset=['도서명', '저자', '출판사'])
ns_book6 = ns_book6[ns_book6['발행년도'] != -1]

ns_book6.to_csv(next_file, index=False)