## 데이터 타입
import sys

# 수치형 데이터 (int)
i = 15; octal = 0o15; hexa = 0x15; b = 0b11111
print(i, octal, hexa, b)
print(sys.maxsize)

# 실수
x = 3.5; y = 2.3e3; z = -0.5e3
print(x, y, z)
print(type(x), type(z))

## 수치 연산 - 연산자 / 나머지 연산자
print(i % 2, " : ", 3.5 % 2)

# 실수 나누기
print(i / 2, " : ", 3.5 / 2)

# 정수 나누기
print(i//2, " : ", 3.5//2)

# 지수 연산
print(i ** 2, pow(i, 2), 3.5 ** 2)

# 몫과 나머지 한꺼번에 구하는 함수
divmod(i, 2)

# 정수 및 실수로 변환하는 함수
print(int(45.6), " : ", float(100))

## 수학 관련 모듈
import math
print(math.pi, math.e, math.sqrt(2))

## 문자열
print("문자열 데이터", '문자 데이터')

# 여러 줄 문자열
mline = """
multi
line
string
여러
줄
문자열
"""

# 문자열에 대한 인덱싱
s = "Hello Python"
print(s[0],"-", s[-5])

# 문자열 슬라이싱
print(s[0:])
print(s[0:4])
print(s[5:-1], s[5:], s[:])
print(s[::2])

# 문자열 연산 + : 문자열 연결
# 문자열 연산 * : 문자열 반복

# \ -> 코드가 다음줄로 연결되는 것을 의미
sum1 = 1 + 2 + 3 + 4 + 5 + \
    6 + 7 + 8 + 9
print(sum1)

# 문자열 변경 -> 변경 불가능 -> 문자열 자체는 바꿀수 없음

s[6] = "p"

# 유니코드 u
u1 = u"한글"
print(type(u1), len(u1), len("한글"))

## 문자열 관련 함수

s = "     i like python like    "
print(s.upper(), s.capitalize(), s.title())
print(s.count("like"), s.find("like"), s.rfind("like"))
print(s.strip(), s.lstrip(), s.rstrip())

s1 = s.split() # 공백을 기준으로 문자열 나눠줌
print(s1)
print(mline.splitlines())

s = "안녕 하세요 미스터"
print(s.replace("안녕 하세요", "반갑습니다")) # 문자열 치환
print(s.endswith("미스터"), s.startswith("하이"))

print("알파벳ABC".isalpha(), "-", "알파벳123".isalpha()) # 문자열이 숫자를 제외한 알파벳, 한글로 되어있는지 여부

# 문자열 포맷팅
print("name=%s, age=%s"%("홍길동", "12"))
print("%10d, %10f, %10s"%(123, 123, 123))
print("%3.5f, %3.3f, %1.15f" % (123, 123.555555, 123))

# dict 사전
print("%(이름)s"%{"이름":"홍길동", "등급":"A"})

msg = """
안녕하세요 %s님
Python 공부 열심히!
열공!
%s 드림
"""

names = ["김유신", "강감찬", "이순신"]
to = "을지문덕"

for name in names:
    print(msg % (name, to))
    print("=" * 30)
    print()

# 새로운 포맷팅
print("현재{2}의 최신버전은 {0}이고 오늘은 {1} 입니다".format("v3.9.0", "10/14", "Python"))
print("{name}님은 {age}세이고 {gender}입니다".format(age=30, name = "홍길동", gender = "남성"))

### 리스트 list

L  = [1, 2, 3, 4, 5]
print(L[3], L[:-1], L[:], L[::2])
print(L*2)

L[0:2] = []
print(L)
L[5:] = [100, 200, 300]
print(L)

# 중첩리스트
L = [1, 2, 3, 4, 5]
L2 = [6, 7, 8, 9, 10]
L[0] = L2
print(L[0][2])

a, b = 100, 200
sun, mon, tue, wed, thu, fri, sat = range(7)
print(sun, mon, sat)

# 리스트 관련 함수
L3 = ["b", "c", "a", "e", "d", "a"]
L3.append("F")
print(L3)
L4 = sorted(L3)
print(L4, L3)
L4 = reversed(L3)
print(L4)

L5 = L3.copy()
L3[0] = 10
print(L5, L3.count("a"))

# 리스트 요소 꺼내온 뒤 리스트에서 제거 pop
print(L3.pop(0))
print(L3)

### 튜플 (tuple)
## 시퀀스 자료형 : 데이터를 저장한 순서대로 관리 -> 수정 및 삭제 불가능
# list -> [] // tuple -> ()
months = ('Jan', 'Feb', 'Mar', 'Apr', "May", 'Jun', 'Jul', "Aug", 'Sep', 'Oct', 'Nov', 'Dec')

# 인덱싱 및 슬라이싱은 가능
print(months[0], months[-1], len(months), type(months))
print(months[::2])

L = list(months)
print(L)
T = tuple(L)
print(T)

print(months * 2)

# 리스트 안에 리스트 / 튜플 저장 가능
# 튜플 안에 리스트 / 튜플 저장 가능
t1 = (1, 2, 3, 4, 5)
l1 = [1, 3, 5]

t = (7, 8 , t1, l1)
print(t)
print(t[2][2:5])

# packing
gu = ("강서구", "양천구", "구로구")
print(gu)

# unpacking
a, b, c = gu
print(a, b, c)

# 튜플의 정렬
gu2 = sorted(gu)
print(gu2)

### 사전 dictionary - dict
## 키 - 값 으로 구성
## {키:값, k1:v1, k2:v2} -> java의 json과 비슷
## 키로 사용할 수 있는 데이터 형 - 변경할 수 없는 데이터형(문자열, 숫자, 튜플)
d = {"name":"홍길동", "age":"25", "gender":"남성"}
print(d)
print(d['name'])
d["grade"] = 4
print(d, len(d))
d["name"] = '이순신'
print('이순신' in d)

# 리스트 또는 튜플 -> dictionary 데이터로 변환
# 키:값 형식의 데이터로 변환
m1 =[["name","홍길동"],["age", 25],["gender","남성"]]
m2 =(("name","홍길동"),("age", 25),("gender","남성"))
print(m1);print(m2)
t1 = dict(m1);t2 = dict(m2)
print(t1, t2)

## zip : 두개의 시퀀스 자료형을 순서대로 쌍으로 묶어 튜플로 반환
keys = ["one", "two", "three"]
values = (1, 2, 3)
print(dict(zip(keys, values)))

## dict의 메서드
# dict의 키 리스트
print(list(d.keys()))
for key in d.keys():
    print(key)
# dict의 값 리스트
print(list(d.values()))
# dict 내의 키값을 하나의 튜플로 묶어 전체를 리스트로 반환하는 메서드
print(d.items())

# 식별자를 비교
d2 = d.copy()
print(id(d), "===", id(d2))

# dict 데이터
print(d["name"], "==", d.get("Name"))
d["add"] = "서울 구로구"
print(d)

phone = {"홍길동":"010-1234-1234", "이순신":"010-3525-5253"}
phone1 = {"강감찬":"010-6345-4512"}
phone.update(phone1)
print(phone)
del(phone["이순신"])
print(phone)
phone.clear()
print(phone)






