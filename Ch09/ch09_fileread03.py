### 파일 읽기

## 반복문 안쓰고 한줄씩 읽기

# 읽기 모드로 파일 오픈
txt_read = open("Ch09/ch09/weather.txt", "rt", encoding="utf-8")

# 파일의 내용을 한 줄 씩 읽어서 list로 반환
txt = txt_read.readlines()

# 자원 해제
txt_read.close()
print(txt)
print(len(txt))