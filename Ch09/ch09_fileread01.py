### 파일 읽기

# 한번에 읽을 크기 - 글자수 지정해서 파일 읽어옴
chunk = 100
# 읽어온 데이터를 저장할 변수
txt = ""
# 파일 읽기 모드로 오픈
txt_open = open("Ch09/ch09/weather.txt", "rt", encoding="utf-8")
cnt = 0
while True:
    # chunk단위로 파일을 읽다가
    temp = txt_open.read(chunk)
    # 읽을 내용이 없으면 빈문자열 ""을 반환 -> False
    # 이 때 반복문 빠져나감
    if not temp:
        break
    txt += temp
    cnt += 1
    print("연속해서 읽은 횟수는 {}".format(cnt))

# 파일 작업 완료되면 자원 해제
txt_open.close()
print(txt)