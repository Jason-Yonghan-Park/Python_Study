import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
a = 100; b = 1000; a = a + b
print(b)
c, d = 100, 200
print(c,d)

# 변수에 값을 대입 -> 할당 연산자 =
x = y = z = 1000
print(x, y, z)

# 복합 할당 연산자 -> +=, *=, -=, /=
c += 100 # c = c + 100
print(c)

x = 100

a = [1, 2, 3]; b = ["A", "B", "C", a]
print(b)
a[1] = 100
print(b)

## 내장함수
print(abs(-8))
print(min([3, 6, 7, 12]), max([12, 7, 8, 18]), max("PythonTop"))
print(pow(2, 2))
print(chr(65), chr(97))
print(str(object), str(123), str([]), str(()), str(chr(65)))

# range([start,] stop[, step])
print(range(10))
for i in range(1, 10, 2):
    print(i)

# 콘솔 입력받는 함수 input
name = input("name : ")
print(name)

# 문자열 -> 정수로 변환하는 함수 int
sum = int(input("1 + 2 ="))
if sum == 3:
    print("맞음")
else:
    print("틀림")

# 연속적으로 콘솔 입력
name = input("name : ")
age = input("age : ")
gender = input("gender : ")
print("{}님은 {}세이며 {}이군요".format(name,age,gender)

r1 = range(1, 11)
l1 = list(r1)
print(l1)
l1[9] = "하하"
print(l1)