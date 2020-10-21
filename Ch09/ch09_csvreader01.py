### csv 파일 읽기
import csv

with open("Ch09/ch09/studentlist.csv", "r") as fin:
    # csv 파일을 읽어 _csv.reader 객체를 반환
    cin = csv.reader(fin)
    for l in cin:
        print(l)