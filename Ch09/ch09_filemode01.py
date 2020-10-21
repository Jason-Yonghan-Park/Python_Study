### 파일 입출력

## 파일 처리 모드

# 파일 쓰기 모드로 오픈 (없으면 새로 생성)
txt_weather = open("txt_weather.txt", "w", encoding = "utf-8")
txt_weather.write("오늘은 10월 20일(화요일) 날씨 맑음") # 직접 파일에 쓰기

# 파일 작업이 끝나면 자원을 해제(연결 해제)
txt_weather.close()

# 파일 읽기 모드로 오픈 (없으면 에러)
txt_read = open("Ch09/ch09/weather.txt", "r", encoding="utf-8")
print(txt_read.read()) # 파일 읽음

# 파일 작업이 끝나면 자원을 해제(연결 해제)
txt_read.close()











