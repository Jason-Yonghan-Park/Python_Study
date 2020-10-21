### 함수 - 하나의 기능을 만들기 위해 관련있는 코드를 묶어 놓은 단위

## 함수 정의 - defined
def add(a, b):
    return a + b

'''
정의부 함수이름():
    실행부
'''

## 함수 호출
print(add(10, 10))
print(add((1,2,3),(4,5,6)))
f = add
print(f(1,2))

# 빈 함수 (empty function)
def no_body():
    pass # 수행할 내용이 없음
print(no_body()) # None

# 콤마로 구분해 반환하면 튜플로 반환
def t_swap(a, b):
    return b, a

print(t_swap(10,30)) # (30, 10)

# 함수에 인수나 초기값을 지정하여 정의 가능
def divide(a, b):
    return a/b

print(divide(10, 2))
print(divide(b=2, a=10)) # 위 아래 같은 결과

def multiple(a, b=1):
    return a*b

print(multiple(10))

# 가변인수는 변수 앞에 *를 붙여 지정 -> 데이터 타입은 튜플
def str_sum(*strs):
    print(type(strs))
    L = []
    for item in strs:
        L.append(item)
    return L
print(str_sum("파이썬은", "쉽고", "재미있다"))

# 숫자 문자열 -> 값이 그대로 전달
# 리스트, 튜플, 딕트 등의 객체는 객체의 참조값 전달
def func(x):
    if type(x) == type(0):
        x = 100
    elif type(x) == type(""):
        x = "abc"
    elif type(x) == type(()):
        pass
    elif type(x) == type([]):
        x[0] = 100
    elif type(x) == type({}):
        x["id"] = "1234"
n = 1000; s = "def"
t = (100, 200, 300); l = [1000, 2000, 3000]
d = {"id":"ㅎㅎㅎ"}
func(n);func(s);func(t);func(l);func(d)
print(n, s, t, l, d)

### 람다 lambda 함수 : 1줄짜리 함수 정의
f = lambda x, y: x + y
print(f(10, 2))

# 선언과 동시에 호출 가능
print((lambda x, y: x*y)(100, 200))

# 인수 기본값을 가지거나 가변인수 가질 수 있음
# 람다 함수 사용 안했을 때
def list_func(func):
    return [func(i) for i in range(1, 11)]
def f1(x):
    return x + x
print(list_func(f1))
# 람다 함수 사용할 때
print(list_func(lambda x: x + x))

## 람다와 함께 사용할 수 있는 내장함수
# map()
def f(x):
    return x + x
l = [10, 20, 30, 40, 50]
# 두번째 인수로 지정한 시퀀스 데이터의 각각의 요소를 첫번째 지정한 함수를 적용하여
# 그 결과를 같은 데이터 타입으로 반환
result = map(f, l)
print(list(result))
print([i for i in result])

result = map(lambda x: x+x, l)
print([i for i in result])

result = map(lambda x: len(x), ["단어", "길이", "리스트"])
print([i for i in result])

# filter()
# 두번째 인수로 지정한 시퀀스형 데이터의 각 요소에
# 첫번째 인수로 지정한 함수가 True를 반환하는 요소만 추출해서
# 같은 데이터 타입으로 반환해주는 함수
l = [1, 6, 3, 10, 5, 8, 9, 2, 4, 7]
result = filter(lambda x: x % 2 == 0, l)
print(list(result))
result = filter(lambda x: x > 5, l)
print(list(result))

# reduce()
# import functools
from functools import reduce
# 반드시 2개의 인수를 지정
result = reduce(lambda x, y: x + y, [1, 2, 3], 100)
print(result) # 1: x = 100, y = 1 -> 101 / 2: x = 101, y = 2 -> 103 / 3: x = 103, y = 3 -> 106

result = reduce(lambda x, y: x+y, range(1, 11))
print(result)

#################################################################################################
## 연습 문제 1






















