### 반복문 - for
## for(초기식:조건식:증감식)
## for i(반복용 변수) in <컨테이너 객체>(list, tuple, dict, range ....)
sum = 0
for i in range(1, 11):
    sum += i
print(sum)
print(list(range(1, 11)))

# for - else 구문 : for문이 정상적으로 수행 후 else 구문 실행
for i in []:
    print(i)
else :
    print("컨테이너 비어있음")

# 리스트 이용한 for문
l = [1, 3, 5, 7, 9]
for i in l:
    print(i, end=",")

# 튜플 이용한 for문
sum = 0
t = tuple(range(1, 11))
for i in t:
    sum += i
print(sum)

# dict 이용한 for문
ramen = {"농심라면":2503, "삼양라면":1750, "오뚜기라면":765}
for key in ramen:
    print(key, ramen.get(key)) #ramen[key]

for k, v in ramen.items():
    print("{}의 가격은 {}입니다".format(k, v))

## 실습문제 -> 총점, 평균
l = [90, 85, 91, 79, 63]
sum = 0
mean = 0
for i in l:
    sum += i
for i in l:
    mean = sum / len(l)
print("총점 : ", sum)
print("평균 : ", mean)

# zip() 함수
e_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
h_days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
print(list(zip(e_days, h_days)))
print(tuple(zip(e_days, h_days)))

for data in zip(e_days, h_days):
    print("{}의 뜻은 {}입니다".format(*data))
for e, h in zip(e_days, h_days):
    print("{}의 뜻은 {}입니다".format(e, h))

# enumerate() 함수
l = ["강감찬", "김유신", "이순신"]
list(enumerate(l))
for i, name in enumerate(l):
    print(i, "-", name)

t = ("사과", "바나나", "한라봉")
list(enumerate(t))
for i, fruit in enumerate(t):
    print("{} - {}".format(i, fruit))

d = {"홍길동":"A", "임꺽정":"B", "장길산":"C"}
print(list(enumerate(d)))
for i, key in enumerate(d):
    print("{}의 학점은 {}입니다.".format(key, d.get(key)))

# 중첩 for문
for i in range(1, 10):
    for j in range(2, 10):
        print(j, "x", i, "=", i*j, sep="", end="\t")
        #print("{}x{}={}".formant(j,i,i*j), end="\t")
    print()

## 실습
"""
◈
◈◈◈
◈◈◈◈◈
◈◈◈◈◈◈◈
◈◈◈◈◈◈◈◈◈
"""
l1 = [1, 3, 5, 7, 9]
for i in range(0, len(l1)):
    print("◈" * l1[i])

for i in range(len(l1)-1, -1, -1):
    print("◈" * l1[i])

for i in range(1, 6):
    print(" "*(5-i), "◈"*(2*i-1))
for j in range(4, 0, -1):
    print(" "*(5-j), "◈"*(2*j-1))

### break : 반복문 빠져나가는 명령 / continue : 반복문의 처음
for i in range(10):
    if i > 5:
        break
    print(i, end=",")

for i in range(10):
    if i < 7:
        continue
    print(i, end=",")



