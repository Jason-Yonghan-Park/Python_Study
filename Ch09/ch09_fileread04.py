### 파일 읽기

## for, with 구문 사용해 파일 읽기

# 파일 읽기모드로 오픈
txt_read = open("Ch09/ch09/weather.txt", "rt", encoding="utf-8")

# for 구문
for line in txt_read:
    print(line)

# 자원 해제
txt_read.close()

# with 구문
# 파일 열고 닫는 작업을 자동으로 해줌
with open("Ch09/ch09/weather.txt", "rt", encoding="utf-8") as f:
    print(f.readlines())

