# 241 datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.
from datetime import datetime, timedelta

now = datetime.now()
print(now)

# 242 datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.
print(now, type(now))

# 243 datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.
for day in range(5,0,-1):
    delta = timedelta(days=day)
    date = now - delta
    print(date)

# 244 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.
#
# 18:35:01
now = datetime.now()
time = now.strftime('%H:%M:%S')
print(time)

# 245 datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.
str = '2020-05-04'
time = datetime.strptime(str,'%Y-%m-%d')
print(time)

# 246 time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.
# import time
# from datetime import datetime
#
# while True:
#     print(datetime.now())
#     time.sleep(1)

# 247 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.
# 풀이
# import 모듈명
# from 모듈명 import 함수명
# from 모듈명 import *
# import 모듈명 as 내가 사용할 이름

# 248 os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.
import os
print(os.getcwd())

# 249 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.

# os.rename('/Users/pearl/Desktop/python study/python 300/무제.txt', '/Users/pearl/Desktop/python study/python 300/무지.txt')

# 250 numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.
import numpy

for i in numpy.arange(0,5,0.1):
    print(i)

print(numpy.arange(0,5,0.1))

# for i in range(0,5,2):
#     print(i)
# range는 마지막 인자로 float 형태의 소수가 올 수 없다.

# 251 클래스, 객체, 인스턴스에 대해 설명해봅시다.
# 풀이
# 클래스 : 객체를 만들어내기 위한 설계도 혹은 틀, 연관되어있는 변수와 메소드의 집합
# 객체 : 구현할 대상, 클래스대로 생성된 실체, 모든 인스턴스를 대표, 클래스의 인스턴스
# 인스턴스 : 구현된 실체, 실체화된 객체, 메모리에 할당됨, 객체에 포함됨, 관계를 나타낼때 사용
# 예) 객체간의 링크는 클래스 간의 연관관계의 인스턴스, 원본(추상)으로부터 생성된 복제본(실체)을 의미

# 252 비어있는 사람 (Human) 클래스를 "정의" 해보세요.
# class Human:
#     pass

# 253 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.
# class Human:
#     pass
#
# areum = Human()

# 254 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.
# class Human:
#     def __init__(self):
#         print('응애응애')
#
# areum = Human()

# 255 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.
#
# >>> areum = Human("아름", 25, "여자")
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human("아름", 25, "여자")
# print(areum.name)

# 256 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.
#
# 이름: 조아름, 나이: 25, 성별: 여자
# 인스턴스 변수에 접근하여 값을 가져오는 예
#
# >>> areum.age
# 25
# print('이름:', areum.name, '나이:', areum.age, '성별:', areum.sex)


# 257 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.
#
# >>> areum.who()
# 이름: 조아름, 나이: 25, 성별: 여자
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def who(self):
#         print('이름:', self.name, '나이:', self.age, '성별:', self.sex)
#
# areum = Human('조아름', 25, '여자')
# areum.who()

# 258 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.
#
# >>> areum = Human("모름", 0, "모름")
# >>> areum.setInfo("아름", 25, "여자")
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def who(self):
#         print('이름:', self.name, '나이:', self.age, '성별:', self.sex)
#
#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#
# areum = Human("모름", 0, "모름")
# areum.who()
# areum.setInfo("아름", 25, "여자")
# areum.who()

# 259 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.
#
# >>> areum = Human("아름", 25, "여자")
# >>> del areum
# 나의 죽음을 알리지 말라
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print('이름:', self.name, '나이:', self.age, '성별:', self.sex)

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print('나의 죽음을 알리지 말라')

areum = Human("아름", 25, "여자")
areum.who()
del areum

# 260 아래와 같은 에러가 발생한 원인에 대해 설명하세요.
#
# class OMG :
#     def print() :
#         print("Oh my god")
#
# >>> >>> myStock = OMG()
# >>> myStock.print()
# TypeError Traceback (most recent call last)
# <ipython-input-233-c85c04535b22> in <module>()
# ----> myStock.print()
#
# TypeError: print() takes 0 positional arguments but 1 was given
# 풀이 : 인스턴스에서 메소드를 호출하면 그 인스턴스 값이 파라미터로 자동 할당되기 때문에
# myStock.print() == OMG.print(myStock)

