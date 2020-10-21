### while 문
cnt = 1
while cnt <= 10:
    print(cnt, end=" ")
    cnt += 1
else:
    print("정상실행")

## 컴프리헨션 comprehension
## 이터레이터 iterator (반복가능한 객체)로 부터 자료구조를 만들어주는 함축적 방법
L = []
for i in range(10):
    L.append(i)
print(L)

# 리스트 컴프리헨션
LH = [i*2 for i in range(10)]
print(LH)

LH2 = [i for i in range(1, 11) if i % 2 == 1]
print(LH2)

# 중첩 for문 컴프리헨션
L = []
for row in range(1, 4):
    for col in range(1, 4):
        L.append((row, col))
print(L)
# -->
NLH = [(row,col) for row in range(1, 4) for col in range(1, 4)]
print(NLH)

# dict 컴프리헨션
L = ["가위", "바위", "보", "가위", "바위", "가위", "보"]
d1 = {key:L.count(key) for key in L}
print(d1)

# 제너레이터 컴프리헨션
GE = (num for num in range(1, 6))
for i in GE:
    print(i, end= " ")

### 실습문제 02
word = ["none", "oop", "class", "sequence", "enumerate"]
meaning = ["아무도(...)않다", "객체지향 프로그래밍", "학급, 수업", "(사건행동 등의) 순서", "열거하다"]
e_dict = dict(zip(word, meaning))
print(e_dict)
print(e_dict.get("none"))

e_dict = {word : meaning for word, meaning in zip(word, meaning)}
print(e_dict)
print(e_dict.get("none"))





