### 이름공간

# 변수 g, a는 전역변수
g = 50
a = 10

# 변수 a, x, h는 함수 안에서 정의 -> 지역변수
def func1(x):
    h = x + 100
    a = h + x + g  # 함수 내의 a는 함수 내부에서 정의된 지역 변수
    return a

print(func1(5))

# global 키워드 -> 전역영역에서 변수 참음
def func2(x):
    global a
    h = x + 100
    a = h + x + g
    return a
print(func2(5))
print(a)



