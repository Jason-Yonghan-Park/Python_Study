### 파일 입출력
## 연습문제 1
# txt 파일 생성
txt_word = open("word.txt", "w")
txt_word.write("Hello World\n"
               "Hello Python\n"
               "Welcome to Python Programming\n"
               "Python File Input Output test")
txt_word.close()

# 생성한 txt 파일 읽기
word_read = open("word.txt", "rt")

# 라인 별 단어 수 출력 프로그램 생성
# txt 파일의 줄 수
temp_line = 0
while True:
    # 한줄 씩 읽기
    temp = word_read.readline()
    # txt 파일의 줄 수 계산
    temp_line += 1
    # 줄 당 단어 분리
    word = temp.split()
    print(word)
    print(len(word))
    if temp_line == 4:
        break
# 자원 해제
word_read.close()

## 연습문제 2
# txt 파일 생성
txt_word = open("m_list.txt", "wt", encoding="utf-8")
txt_word.write("""임꺽정 000914-3752364
홍길동 750124-1476521
박현명 011226-3125475
김유신 891025-1524287
이순신 791115-1512475
양순영 010618-4205145
강감찬 820507-1912454
어머나 731004-2845721
왕빛나 001219-4512875
강호감 870713-1475125""")
txt_word.close()

# 생성한 txt 파일 쓰기모드 오픈
with open("m_list.txt", "r", encoding="utf-8") as ml:
    new_degit = "-*******"
    new_data = []
    for line in ml:
        line = line.rsplit("-")
        line.remove(line[1])
        lines = line.pop(0)
        new_lines = lines + new_degit
        new_data.append(new_lines+"\n")
    print(new_data)

with open("m_result.txt", "w", encoding="utf-8") as mr:
    mr.writelines(new_data[0:])
