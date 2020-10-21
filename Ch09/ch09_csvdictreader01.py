### csv 파일 읽기

## dictreader
import csv

with open("Ch09/ch09/studentlist.csv", "rt") as fin:
    cin = csv.DictReader(fin)

    list_data = [row for row in cin]

print(list_data)

with open("Ch09/ch09/studentlist.csv", "wt") as fout:
    cout = csv.DictWriter(fout, ["name", "sex", "age", "grade", "absence", "bloodtype", "height", "weight"])
    cout.writeheader()
    cout.writerows(list_data)
print("student_dict.csv 파일 쓰기 완료")