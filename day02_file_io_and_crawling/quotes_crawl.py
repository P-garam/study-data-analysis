import os

# 현재 스크립트 파일과 같은 경로에 저장되도록 설정
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "quotes_output.txt")


# 크롤링 시작
import requests # python에서 HTTP 요청 보내는 라이브러리
from bs4 import BeautifulSoup # HTML 해석 도와주는 라이브러리

# Set the URL of the website to crawl
url = "http://quotes.toscrape.com"
# 크롤링할 대상 웹사이트 주소를 문자열로 저장

# Send a GET request to the website
response = requests.get(url)
# 해당 주소에 get요청을 보내고 response로 저장

# Check if the request was successful(200이면 정상)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quote blocks
    quotes = soup.find_all("div", class_="quote")

    # Extract and print each quote and author
    with open(file_path, "w", encoding="utf-8") as f:
        for quote in quotes:
            # 5. 명언과 작가 추출
            text = quote.select_one("span.text").get_text(strip=True)
            author = quote.select_one("small.author").get_text(strip=True)

            # 6. 파일에 쓰기
            f.write(f"{text} - {author}\n")

    print("명언 파일 저장 완료: quotes_output.txt")
else:
    print("웹페이지를 불러오는 데 실패했습니다.")