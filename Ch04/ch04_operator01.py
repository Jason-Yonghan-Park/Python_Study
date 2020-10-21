### 제어문

## 관계 연산자 - 객체가 같은지, 작은지, 큰지 등을 비교하는 연산자
## 연산결과 -> True, False로 반환
print(5 > 10, "--", 5 < 10) # false, true
print("abcd">"bac", "---", "abcd" < "bcd") # false, true
print((1, 5, 9) > (3, 4, 6), "---", (1, 5, 9) < (3, 4, 6)) # false, true
print([1, 5, 9] > [3, 4, 6], "---", [1, 5, 9] < [3, 4, 6]) # false, true

## 논리 연산자 - 논리값을 대상으로하는 연산 - 피연산자 -> 논리값
## or, and, not
## 비교 연산자와 연결해서 많이 사용 -> 비교 연산의 결과가 논리값
print(1 > 2 or 1 < 2) # true
print(1 > 2 and 1 < 2) # false
print(not None, "--", not 0, "--", not "", not[]) # true, true, true, true
print(True + True, "--", False + False, "--", True + False) # 2, 0, 1
print(1 and 1, 1 and 0, 0 and 0) # 1, 0, 0

## 객체 판별
## type()
a = 100; b = 100.0; c = "타입"
l = [a, b]; t = (b, c); d = {"a":a, "b":b}
print(type(a) == type(b)) # false
print(type(d) == type({})) # true

# 객체의 식별자(참조값)
l2 = l
l3 = l.copy()
print(id(l2) == id(l)) # true
print(id(l3) == id(l)) # false

# 숫자 / 문자열 -> 상수 취급
x = 1; y = 1
print(id(x) == id(y)) # true
print(x is y) # true






