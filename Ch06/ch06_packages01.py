import sys

for path in sys.path:
    print(path)

from Calculator.hello import hello, message
hello("홍길동")

import Calculator.adder.cal.MyMul as my
print(my.multiple(10, 20))


from Calculator.ext.cal import ExtAdd as a, ExtMul as m
print(a.add_list([1,2,3]))
print(m.mul_list([2,3,4]))