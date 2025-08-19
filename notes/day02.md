[파일 입출력]
    with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!\n")
    f.write("This is the second line.\n")

    - "w" 모드는 쓰기 모드. 기존 파일이 있다면 덮어씀.
    - "r" 모드는 읽기 모드.
    - with open(...) as f: 는 파일을 자동으로 닫아주는 안전한 방법.
    - f.write() 는 한 줄씩 문자열을 파일에 씀.

[웹 크롤링 기초]
<라이브러리>
    import requests # python에서 HTTP 요청 보내는 라이브러리
    from bs4 import BeautifulSoup # HTML 해석 도와주는 라이브러리

<실습>
    url = "http://quotes.toscrape.com"
    response = requests.get(url)  # 웹페이지 요청

    if response.status_code == 200:  # 요청성공했는지 확인
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.select("div.quote")  # 모든 명언 박스 가져오기

        for quote in quotes:
            text = quote.select_one("span.text").get_text(strip=True)
            author = quote.select_one("small.author").get_text(strip=True)
            print(f"{text} - {author}")
    
    - requests.get(url): 해당 주소의 HTML을 가져옴
    - BeautifulSoup(response.text, "html.parser"): HTML 파싱
    - soup.select("div.quote"): <div class="quote"> 태그 전체 선택
    - select_one("span.text"): 내부 명언 텍스트만 추출

<파일로 결과 저장하기>
    with open("quotes_output.txt", "w", encoding="utf-8") as f:
        for quote in quotes:
            text = quote.select_one("span.text").get_text(strip=True)
            author = quote.select_one("small.author").get_text(strip=True)
            f.write(f"{text} - {author}\n")

    - 추출한 데이터를 바로 .txt 파일로 저장 가능
    - \n은 줄바꿈 문자
    - 텍스트 파일은 코드 파일과 같은 디렉토리에 생성됨 (상대경로 기준)