### csv 파일 쓰기
import csv
# csv에 저장할 데이터
list_data = [["이름", "점수"],
             ["홍길동", 86],
             ["김철수", 75],
             ["김길동", 96],
             ["이희진", 83],
             ["박미희", 90] ]

# 파일 쓰기모드로 오픈
with open("Ch09/ch09/studentlist.csv", "wt") as fout:
    # 파일에 쓰기 기능을 제공하는 객체 - writer
    csvout = csv.writer(fout)
    # csv 파일로 출력
    csvout.writerows(list_data)
print("studentlist.csv 파일 쓰기 완료")