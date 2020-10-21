### 파일 읽기

## 한 줄 씩 읽기

txt = ""

# 파일 읽기 모드로 오픈
txt_read = open("Ch09/ch09/weather.txt", "rt", encoding="utf-8")
while True:
    temp = txt_read.readline()
    # 파일에서 읽을 내용 없으면 반복문 탈출
    if not temp:
        break
    # 한줄씩 읽어 txt에 저장
    txt += temp

# 파일 작업 완료 -> 자원 해제
txt_read.close()
print(txt)