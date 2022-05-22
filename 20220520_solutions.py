# 261 주식 종목에 대한 정보를 저장하는 Stock 클래스를 정의해보세요. 클래스는 속성과 메서드를 갖고 있지 않습니다.
# class Stock:
#     pass

# 262 Stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록 생성자를 정의해보세요.
#
# 삼성 = Stock("삼성전자", "005930")
# class Stock:
#     def __init__(self, company, code):
#         self.company = company
#         self.code = code

# 263 객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.
#
# a = Stock(None, None)
# a.set_name("삼성전자")
# class Stock:
#     def __init__(self, company, code):
#         self.company = company
#         self.code = code
#
#     def set_name(self, company):
#         self.company = company
#
#
# a = Stock(None, None)
# print(a.company)
# a.set_name("삼성전자")
# print(a.company)

# 264 객체에 종목코드를 입력할 수 있는 set_code 메서드를 추가해보세요.
#
# a = Stock(None, None)
# a.set_code("005930")
# class Stock:
#     def __init__(self, company, code):
#         self.company = company
#         self.code = code
#
#     def set_name(self, company):
#         self.company = company
#
#     def set_code(self, code):
#         self.code = code
#
# a = Stock(None, None)
# print(a.code)
# a.set_code("005930")
# print(a.code)

# 265 종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력해보세요.
#
# 삼성 = Stock("삼성전자", "005930")
# class Stock:
#     def __init__(self, company, code):
#         self.company = company
#         self.code = code
#
#     def set_name(self, company):
#         self.company = company
#
#     def set_code(self, code):
#         self.code = code
#
#     def get_name(self):
#         print(self.company)
#
#     def get_code(self):
#         print(self.code)
#
#
# a = Stock("삼성전자", "005930")
# a.get_name()
# a.get_code()

# 266 생성자에서 종목명, 종목코드, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요. PER, PBR, 배당수익률은 float 타입입니다.
# class Stock:
#     def __init__(self, company, code, per, pbr, rate):
#         self.company = company
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.rate = rate
#
#     def set_name(self, company):
#         self.company = company
#
#     def set_code(self, code):
#         self.code = code
#
#     def get_name(self):
#         print(self.company)
#
#     def get_code(self):
#         print(self.code)

# 267 266번에서 정의한 생성자를 통해 다음 정보를 갖는 객체를 생성해보세요.
#
# 항목	정보
# 종목명	삼성전자
# 종목코드	005930
# PER	15.79
# PBR	1.33
# 배당수익률	2.83
# samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# samsung.get_code()
# samsung.get_name()
# print(samsung.per, samsung.pbr, samsung.rate)

# 268 PER, PBR, 배당수익률은 변경될 수 있는 값입니다. 이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가하세요.
import csv


class Stock:
    def __init__(self, company, code, per, pbr, rate):
        self.company = company
        self.code = code
        self.per = per
        self.pbr = pbr
        self.rate = rate

    def set_name(self, company):
        self.company = company

    def set_code(self, code):
        self.code = code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, rate):
        self.rate = rate

    def get_name(self):
        print(self.company)

    def get_code(self):
        print(self.code)


# samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# samsung.get_code()
# samsung.get_name()
# print(samsung.per)

# 269 267번에서 생성한 객체에 set_per 메서드를 호출하여 per 값을 12.75로 수정해보세요.
# samsung.set_per(12.75)
# print(samsung.per)

# 270 아래의 표를 참조하여 3종목에 대해 객체를 생성하고 이를 파이썬 리스트에 저장하세요. 파이썬 리스트에 저장된 각 종목에 대해 for 루프를 통해 종목코드와 PER을 출력해보세요.
#
# 종목명	종목코드	PER	PBR	배당수익률
# 삼성전자	005930	15.79	1.33	2.83
# 현대차	005380	8.70	0.35	4.27
# LG전자	066570	317.34	0.69	1.37
samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
hyundal = Stock("현대차", "005380", 8.70, 0.35, 4.27)
lg = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

stock_list = [samsung, hyundal, lg]

for i in stock_list:
    print(i.code, i.per)

# 271 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. Account 클래스를 생성한 후 생성자를 구현해보세요. 생성자에서는 예금주와 초기 잔액만 입력 받습니다. 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
#
# 은행이름: SC은행
# 계좌번호: 111-11-111111
from random import random, randint
# class Account:
#     def __init__(self, name, credit):
#         self.name = name
#         self.credit = credit
#         self.bank = "SC은행"
#         num1 = randint(0,999)
#         num2 = randint(0,99)
#         num3 = randint(0,999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3

# def create(self):
#     print('은행이름: SC은행')
#     account_address = ''
#     for i in range(12):
#         num = randint(1,10)
#         account_address += str(num)
#     print(account_address[:3],'-',account_address[4:6],'-',account_address[6:])


# a = Account("김진주", 2000)
# print(a.bank, a.account_number)

# 272 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.
# 클래스 변수?
from random import random, randint
# class Account:
#
#     account_count = 0
#
#     def __init__(self, name, credit):
#         self.name = name
#         self.credit = credit
#         self.bank = "SC은행"
#         num1 = randint(0,999)
#         num2 = randint(0,99)
#         num3 = randint(0,999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3
#
#         Account.account_count += 1
#
# a = Account("김진주", 2000)
# print(Account.account_count)
# b = Account("박라담", 10000)
# print(Account.account_count)

# 273 Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.
from random import random, randint
# class Account:
#
#     account_count = 0
#
#     def __init__(self, name, credit):
#         self.name = name
#         self.credit = credit
#         self.bank = "SC은행"
#         num1 = randint(0,999)
#         num2 = randint(0,99)
#         num3 = randint(0,999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3
#
#         Account.account_count += 1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)
#
#
# a = Account("김진주", 2000)
# a.get_account_num()
# b = Account("박라담", 10000)
# b.get_account_num()

# 274 Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.
from random import random, randint
# class Account:
#
#     account_count = 0
#
#     def __init__(self, name, credit):
#         self.name = name
#         self.credit = credit
#         self.bank = "SC은행"
#         num1 = randint(0,999)
#         num2 = randint(0,99)
#         num3 = randint(0,999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3
#
#         Account.account_count += 1
#
#     def deposit(self, cash):
#         if cash >= 1:
#             self.credit += cash
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)
#
#
# a = Account("김진주", 2000)
# b = Account("박라담", 10000)
# b.get_account_num()
# print(a.credit)
# a.deposit(2000)
# print(a.credit)

# 275 Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.
from random import random, randint
# class Account:
#
#     account_count = 0
#
#     def __init__(self, name, credit):
#         self.name = name
#         self.credit = credit
#         self.bank = "SC은행"
#         num1 = randint(0,999)
#         num2 = randint(0,99)
#         num3 = randint(0,999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3
#
#         Account.account_count += 1
#
#     def deposit(self, cash):
#         if cash >= 1:
#             self.credit += cash
#
#     def withdraw(self, draw):
#         if draw <= self.credit:
#             self.credit -= draw
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)
#
#
# a = Account("김진주", 2000)
# b = Account("박라담", 10000)
# b.get_account_num()
# print(a.credit)
# a.deposit(2000)
# print(a.credit)
# a.withdraw(4000)
# print(a.credit)

# 276 Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요.
#
# 은행이름: SC은행
# 예금주: 파이썬
# 계좌번호: 111-11-111111
# 잔고: 10,000원
from random import random, randint
# class Account:
#
#     account_count = 0
#
#     def __init__(self, name, credit):
#         self.name = name
#         self.credit = credit
#         self.bank = "SC은행"
#         num1 = randint(0,999)
#         num2 = randint(0,99)
#         num3 = randint(0,999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3
#
#         Account.account_count += 1
#
#     def deposit(self, cash):
#         if cash >= 1:
#             self.credit += cash
#
#     def withdraw(self, draw):
#         if draw <= self.credit:
#             self.credit -= draw
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)
#
#     def display_info(self):
#         print(self.bank)
#         print(self.name)
#         print(self.account_number)
#         print(self.credit)
#
#         # 3자리마다 ',' 가 insert 되도록 작성하는 코드 필요
#
# a = Account("김진주", 2000)
# b = Account("박라담", 10000)
# b.deposit(20000)
#
# b.display_info()

# 277 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.
from random import random, randint


class Account:
    account_count = 0

    def __init__(self, name, credit):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.credit = credit
        self.bank = "SC은행"
        num1 = randint(0, 999)
        num2 = randint(0, 99)
        num3 = randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1

    def deposit(self, cash):
        if cash >= 1:
            self.deposit_log.append(cash)
            self.credit += cash

        self.deposit_count += 1
        if self.deposit_count % 5 == 0:
            self.credit = self.credit * 1.01

    def withdraw(self, draw):
        if draw <= self.credit:
            self.withdraw_log.append(draw)
            self.credit -= draw

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def display_info(self):
        print(self.bank)
        print(self.name)
        print(self.account_number)
        print(f'잔고:{self.credit:,}원')

        # 3자리마다 ',' 가 insert 되도록 작성하는 코드 필요

    def deposit_history(self):
        for i in self.deposit_log:
            print("입금:", i)

    def withdraw_history(self):
        for i in self.withdraw_log:
            print("출금", i)


# 278 Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.
a = Account("김진주", 3000)
b = Account("박지환", 5000)
c = Account("박라담", 50000000000)

customer_list = []
customer_list.append(a)
customer_list.append(b)
customer_list.append(c)

# 279 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.
for i in customer_list:
    if i.credit >= 1000000:
        i.display_info()

# 280 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.
a.deposit(2000)
a.deposit(3000)
a.deposit(10000)
a.deposit_history()


# 281 다음 코드가 동작하도록 차 클래스를 정의하세요.
#
# >> car = 차(2, 1000)
# >> car.바퀴
# 2
# >> car.가격
# 1000
class 차:
    def __init__(self, wheel, price):
        self.바퀴 = wheel
        self.가격 = price


car = 차(2, 1000)
print(car.바퀴)
print(car.가격)


# 282 차 클래스를 상속받은 자전차 클래스를 정의하세요.
# class 자전차(차):
#     pass

# 283 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
# >> bicycle = 자전차(2, 100)
# >> bicycle.가격
# 100
# class 자전차(차):
#     pass
#
# bicycle = 자전차(2, 100)
# print(bicycle.가격)

# 284 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
#
# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.구동계
# 시마노
# class 자전차(차):
#     def __init__(self, wheel,price,name):
#         super().__init__(wheel,price)
#         self.구동계 = name
#
# bicycle = 자전차(2, 100, "시마노")
# print(bicycle.바퀴)
# print(bicycle.구동계)

# 285 다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.
#
# >> car = 자동차(4, 1000)
# >> car.정보()
# 바퀴수 4
# 가격 1000
class 자동차(차):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)

    def 정보(self):
        print(self.바퀴)
        print(self.가격)


car = 자동차(4, 1000)
car.정보()


# 286 다음 코드가 동작하도록 차 클래스를 수정하세요.
#
# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.정보()
# 바퀴수 2
# 가격 100
# 위에꺼랑 똑같은것 같은데...

# 287 자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.
#
# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.정보()
# 바퀴수 2
# 가격 100
# 구동계 시마노
class 자전차(차):
    def __init__(self, wheel, price, name):
        super().__init__(wheel, price)
        self.구동계 = name

    def 정보(self):
        print(self.바퀴)
        print(self.가격)
        print(self.구동계)


bicycle = 자전차(2, 100, "시마노")
bicycle.정보()

# 288 다음 코드의 실행 결과를 예상해보세요.
#
# class 부모:
#   def 호출(self):
#     print("부모호출")
#
# class 자식(부모):
#   def 호출(self):
#     print("자식호출")
# 나 = 자식()
# 나.호출()
# 오버라이딩 : 부모 클래스에서 상속받은 특정 메소드를 자식 클래스에서 재정의하는 작업
# 호출이라는 메소드를 상속받은 자식 클래스의 메소드가 우선되고 부모 클래스의 호출 메소드는 무시된다.
# 풀이
# 자식호출

# 289 다음 코드의 실행 결과를 예상해보세요.
#
# class 부모:
#   def __init__(self):
#     print("부모생성")
#
# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
# 나 = 자식()
# 풀이
# 자식생성

# 290 다음 코드의 실행 결과를 예상해보세요.
#
# class 부모:
#   def __init__(self):
#     print("부모생성")
#
# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
#     super().__init__()
#
# 나 = 자식()
# 풀이
# 자식생성
# 부모생성

# 291  바탕화면에 '매수종목1.txt' 파일을 생성한 후 다음과 같이 종목코드를 파일에 써보세요.
#
# 005930
# 005380
# 035420
f = open("매수종목1.txt", mode="wt", encoding="utf-8")
f.write("005930\n")
f.write("005380\n")
f.write("035420\n")
f.close()

# 292 바탕화면에 '매수종목2.txt' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요.
#
# 005930 삼성전자
# 005380 현대차
# 035420 NAVER
f = open("매수종목2.txt", mode="wt", encoding="utf-8")
f.write("005930\t삼성전자\n")
f.write("005380\t현대차\n")
f.write("035420\tNAVER\n")
f.close()

# 293 바탕화면에 '매수종목.csv' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요. 인코딩은 'cp949'를 사용해야합니다.
f = open("/Users/pearl/desktop/매수종목.csv", mode="wt", encoding="cp949", newline='')
writer = csv.writer(f)
writer.writerow(["종목명", "종목코드", "PER"])
writer.writerow(["삼성전자", "005930", 15.59])
writer.writerow(["NAVER", "035420", 55.82])
f.close()

# 294 바탕화면에 생성한 '매수종목1.txt' 파일을 읽은 후 종목코드를 리스트에 저장해보세요.
f = open("매수종목1.txt", encoding="utf-8")
lines = f.readlines()
print(lines)
codes = []
for line in lines:
    code = line.strip()
    codes.append(code)

f.close()
print(codes)

# 295 바탕화면에 생성한 '매수종목2.txt' 파일을 읽은 후 종목코드와 종목명을 딕셔너리로 저장해보세요. 종목명을 key로 종목명을 value로 저장합니다.
#
f = open("매수종목2.txt", encoding="utf-8")
lines = f.readlines()
print(lines)
dicts = {}
for line in lines:
    company = line.split('\t')[1].strip()
    code = line.split('\t')[0]
    dicts[company] = code

f.close()
print(dicts)

# 296 문자열 PER (Price to Earning Ratio) 값을 실수로 변환할 때 에러가 발생합니다. 예외처리를 통해 에러가 발생하는 PER은 0으로 출력하세요.
#
per = ["10.31", "", "8.00"]

# for i in per:
#     if i == '':
#         print(0)
#     else:
#         print(float(i))

for i in per:
    try:
        print(float(i))
    except:
        print(0)

# 297 문자열로 표현된 PER 값을 실수로 변환한 후 이를 새로운 리스트에 저장해보세요.
#
per = ["10.31", "", "8.00"]
new_per = []
for i in per:
    try:
        new_per.append(float(i))
    except:
        new_per.append(0)

print(new_per)

# 298 어떤 값을 0으로 나누면 ZeroDivisionError 에러가 발생합니다. try ~ except로 모든 에러에 대해 예외처리하지 말고 ZeroDivisionError 에러만 예외처리해보세요.
# 3 / 0
try:
    3 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없어요")

# 299 다음과 같은 코드 구조를 사용하면 예외 발생 시 에러 메시지를 변수로 바인딩할 수 있습니다.
#
# try:
#     실행코드
# except 예외 as 변수:
#     예외처리코드
# 리스트의 인덱싱에 대해 에러를 출력해보세요.
#
data = [1, 2, 3]


for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)

# 300 파이썬 예외처리는 다음과 같은 구조를 가질 수 있습니다.
#
# try:
#     실행 코드
# except:
#     예외가 발생했을 때 수행할 코드
# else:
#     예외가 발생하지 않았을 때 수행할 코드
# finally:
#     예외 발생 여부와 상관없이 항상 수행할 코드
# 아래의 코드에 대해서 예외처리를 사용하고 try, except, else, finally에 적당한 코드를 작성해봅시다. else와 finally는 적당한 문구를 print하시면 됩니다.
#
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환완료")



