import gdown

# 구글 드라이브 공유 링크 (bit.ly 가능)
#url = 'https://bit.ly/3q9SZix'  # 책에서 제공한 링크
output = '20s_best_book.json'

#gdown.download(url, output, quiet=False)

import pandas as pd
books_df = pd.read_json('20s_best_book.json')

# 직접 df에서 특정 열만 가져오는법
#books = books_df[['no', 'ranking', 'bookname', 'authors', 'publisher', 'publication_year', 'isbn13']]
#print(books.head())

# 매서드 사용하는법
#books_df.loc[[0,1], ['bookname', 'authors']] #첫번째,두번째 행의 도서명과 저자명만 추출
#books_df.loc[0:1, ['bookname', 'authors']] #첫번째 행부터 두번째 행까지의 도서명과 저자명

books = books_df.loc[:, 'no':'isbn13'] #모든행의 no 부터 isbn13열까지
# [::2, 'no':'isbn13'] 이렇게 하면 행을 2칸씩 뛰면서라는뜻

import requests
isbn = 9791190090018
url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'
r = requests.get(url.format(isbn))

#print(r.text)

# 뷰티풀수프 해보기
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

# yes24 검색 결과 페이지에서 도서의 상세 페이지로 넘어가는 링크 찾기
#prd_link = soup.find('a', attrs={'class':'gd_name'})
#print(prd_link['href'])

#url2 = 'http://www.yes24.com'+prd_link['href']
#r = requests.get(url2)
#soup = BeautifulSoup(r.text, 'html.parser')
#prd_detail = soup.find('div', attrs={'id':'infoset_specific'})
#print(prd_detail)

#prd_tr_list = prd_detail.find_all('tr') #tr html 태그를 모두 찾아서 리스트로 반환

#for tr in prd_tr_list:
   # if tr.find('th').get_text() == '쪽수, 무게, 크기': #각 행에서 <th> 안의 텍스트의 내용이 '쪽수,무게,크키'인지 확인
        #page_td = tr.find('td').get_text() 
        #break

# 쪽수만 필요
#print(page_td.split()[0])

# isbn 정수 값을 받아 쪽수를 반환하는 함수 만들기
def get_page_cnt(isbn):
    url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'
    r = requests.get(url.format(isbn))
    soup = BeautifulSoup(r.text, 'html.parser')
    prd_info = soup.find('a', attrs={'class':'gd_name'})
    if prd_info == None:
        return ''
    
    url = 'http://www.yes24.com'+prd_info['href']
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    prd_detail = soup.find('div', attrs={'id':'infoset_specific'})
    prd_tr_list = prd_detail.find_all('tr')
    for tr in prd_tr_list:
        if tr.find('th').get_text() == '쪽수, 무게, 크기':
            result = tr.find('td').get_text().split()[0]
            print(result)
            return result
            
    return

#get_page_cnt(9791190090018)

# 데이터프레임 행 혹은 열에 함수 적용하기
top10_books = books.head(10)
def get_page_cnt2(row):
    isbn = row['isbn13']
    return get_page_cnt(isbn)

page_count = top10_books.apply(get_page_cnt2, axis=1) # (실행할함수, 1(행이라는뜻))
page_count.name = 'page_count'

top10_with_page_count = pd.merge(top10_books, page_count, left_index=True, right_index=True)
#(첫번째 데이터, 두번째 데이터, 첫번째데이터인덱스, 두번째데이터인덱스)

print(top10_with_page_count)