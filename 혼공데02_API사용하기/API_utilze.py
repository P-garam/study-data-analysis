import requests
import pandas as pd
import os

base_path = os.path.dirname(__file__)  
file_path = os.path.join(base_path, "20s_best_book.json")

url = "http://data4library.kr/api/loanItemSrch?&format=json&startDt=2025-06-01&endDt=2025-06-30&age=20&authKey=f0cc6be708389973f33dc9a545dafba5b9fd0bb9029a72a99723203ecb9f7576"

r = requests.get(url)

data = r.json() # json str -> python obj
#print(data)

books = []
for d in data['response']['docs']:
    books.append(d['doc'])

#print(books)

books_df = pd.DataFrame(books)
#print(books_df)

books_df.to_json(file_path) # save as json file