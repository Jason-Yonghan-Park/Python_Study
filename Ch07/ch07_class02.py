### 클래스

## 클래스 정의
class Human:
    name = "홍길동"

Human.age = 25
print(Human, "=", Human.name, "=", Human.age)

del(Human.age)
print(dir(Human))

## 인스턴스
# 클래스와 독립적으로 이름공간을 가짐
# 인스턴스 -> 생성될때마다 각각의 이름 공간을 가짐
h = Human() # 인스턴스 생성
h.age = 30

h1 = Human() # 같은 클래스를 참조하는 인스턴스라 하더라도 h와 h1의 이름공간은 다름
h1.gender = "남성"
print(h, "-", h.name, "-", h.age)
print(h1, "-", h1.name, "-", h1.gender)
# 즉, h와 h1은 같은 클래스를 참조하여 name이라는 이름에는 접근 가능하지만
# h와 h1이라는 각각의 인스턴스 내의 age와 gender라는 이름에는 서로 접근이 불가

## 몸체 없는 클래스
# pass 사용
class Animal:
    pass

Animal.age = 10

a = Animal()
a.kind = "고양이"
a.name = "야옹이"
a.age = 5

print(a.name, "-", a.age, "-", a.kind, "-", Animal.age)
print(dir(Animal))
print(dir(a))

### 생성자와 소멸자

## 생성자: 인스턴스가 생성될 때 딱 한번 초기화 작업을 수행
## 소멸자: 인스턴스가 소멸될 때 딱 한번 마지막으로 처리해야할 작업을 수행

from time import sleep
class Human:
    # 클래스 안에는 변수, 메서드 등이 있음
    def __init__(self):
        self.name = "$홍길동$"

    # 소멸자
    def __del__(self):
        print("Human 인스턴스 소멸됨")

def test():
    h = Human()
    print(h.name)
    sleep(3)

test()

## 클래스 정의
class Human1:
    # 생성자
    def __init__(self, *args):
        print(len(args))
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]

    # 소멸자
    def __del__(self):
        print("Human1 인스턴스 소멸")

h1 = Human1("홍길동", 25)
print(h1.name, "-", h1.age)

class Human:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age

h = Human()
h.setName("이순신")
h.setAge(35)
print(h.getName(), "-", h.getAge())

# 클래스 이름을 가지고 인스턴스에 접근
h1 = Human()
Human.setName(h1, "강감찬")
h1.gender = "남성"

### 클래스와 전역함수

## 전역함수

def setNum(num):
    print("전역함수", num + 1)

# 클래스 정의
class MyClass:
    def setNum(self, num):
        self.num = num
    def getNum(self):
        return self.num
    def increment(self):
        self.setNum(self.num + 1)
    def outIncr(self):
        setNum(self.num + 10)

c = MyClass()
c.setNum(10)
c.increment()
print("인스턴스 변수: ", c.getNum())
c.outIncr()

## 정적 메서드, 클래스 메서드
class M:
    @staticmethod # staticmethod라는 장식자(Decorator)가 붙음
    def staticMessage(x):
        print("정적 메서드: ", x)

    @classmethod # classmethod라는 장식자가 붙음
    def classMessage(cls, x):
        print("클래스 메서드: ", cls, "-", x)

sm = M()
sm.staticMessage("안녕 파이썬")
sm.classMessage("Hello Python")

# 정적 메서드와 클래스 메서드는 클래스를 통해 접근 가능
M.staticMessage("파이썬")
M.classMessage("Python")

# 상속 과정에서의 동작
class SM(M):
    pass

SM.staticMessage("상속받은 SM")
SM.classMessage("상속받은 SM")

## 클래스 멤버 / 인스턴스 멤버
class Score:
    # 클래스 멤버
    min = 0
    max = 100
    score = 50

    def setScore(self, score):
        if score < 0 or score > 100:
            print("점수는 0 ~ 100점 사이의 값")
            self.score = 0
        else:
            self.score = score

    def getScore(self):
        return self.score

s1 = Score()
s1.setScore(101)
print(s1.score)

##########
### 상속
## 부모 클래스의 모든 기능(메서드, 변수)을 자식 클래스가 물려받는 것
## 상속해주는 클래스: 부모/슈퍼/베이스 클래스
class Car:
    def drive(self):
        print("자동차를 운전함")

## 상속을 받는 클래스: 자식/서브/파생 클래스
class Bus(Car):
    pass

bus1 = Bus()
bus1.drive()

# 객체의 타입 비교
print(Bus, "-", Car, "-", bus1)
print(type(bus1) == Bus, "-", type(bus1) == Car)
print(isinstance(bus1, Bus), "-", isinstance(bus1, Car))
print(issubclass(Bus, Bus), "-", issubclass(Bus, Car))
print(type(bus1), "-", Bus)

# Car 클래스를 상속받는 Truck 클래스 정의
class Truck(Car):
    def drive(self):
        print("Truck을 운전함")

c = Car()
t = Truck()
c.drive()
t.drive()

class Super():
    def __init__(self, name):
        self.name = name
        print("Super 생성자 호출")

# Super 클래스 상속받는 클래스
class Sub1(Super):
    pass

# 자식 클래스에 생성자 정의되어있지 않으면
# 부모의 생성자가 자식 객체 생성할때 자동으로 호출
s = Sub1("강감찬")
print(s.name)

# Super 클래스 상속받는 클래스
class Sub2(Super):
    # 생성자가 오버라이드 되면 부모의 생성자는 자동 호출 x
    # 자식의 생성자에서 명시적으로 호출해야함
    def __init__(self, name):
        Super.__init__(self, name)
        #super().__init__(name)
        print("Sub2 생성자 호출됨")

s1 = Sub2("이순신")
print(s1.name)

print(s1)
print(Sub2)

# 클래스 정의
class Human:
    def __init__(self, name, age, gender=None):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return "<Human {} {} {}>".format(self.name, self.age, self.gender)

h1 = Human("홍길동", 25, "남성")
print(h1)
print(Human)

# Human 클래스를 상속 받는 클래스
class Student(Human):
    # 생성자 오버라이딩
    def __init__(self, name, age, gender, grade):
        # 부모의 생성자를 호출
        Human.__init__(self, name, age, gender)
        # super()메서드는 부모 클래스의 정의를 얻는 메서드
        # super().__init__(name, age, gender)
        self.grade = grade

s1 = Student("홍길동", 35, "남자", 2)
print(s1.name, "-", s1.grade, "-", s1)

