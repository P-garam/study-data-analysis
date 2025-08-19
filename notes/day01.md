print(값1, 값2, ..., sep=' ', end='\n')
- 값1, 값2 : 출력할 값들
- sep : 값들 사이에 넣을 구분자
- end : 줄 끝에 붙는 문자

<조건문 문법>
if 조건:
    실행문
elif 조건2:
    실행문2
else:
    실행문3

<반복문 문법>
for 변수 in 순회가능한객체:
    실행문

(예시)
for i in range(3):  # 0, 1, 2
    print(i)

i = 0
while i < 3:
    print(i)
    i += 1

break: 반복 종료
continue: 다음 반복으로 건너뜀
