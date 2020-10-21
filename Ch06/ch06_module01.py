import Ch06.MyCalc as my_calc

print(my_calc.MyPi)
print(my_calc.area(10))

from Ch06.MyCalc import area as a, MyPi as pi, multiple as mul
print(a(30))
print(pi)

import Ch06.MyCalc as my
print(__name__)
print(my.__name__)

if __name__ == "__main__":
    print("현재 모듈이 최상위에서 실행 됨")