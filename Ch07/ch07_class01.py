### 클래스

## 클래스 정의
class Human:
    name = "홍길동"

Human.age = 25
print(Human, "-", Human.name, "-", Human.age)
print(dir(Human))

## 인스턴스 생성
h = Human()
h.age = 30
print(h, "=", h.name, "==", h.age)

h2 = Human()
h2.age = 50
print(h2, "=", h2.name, "-", h2.age)