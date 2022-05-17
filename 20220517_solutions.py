# 181 아래 표에서 하나의 행을 하나의 리스트로, 총 3개의 리스트를 갖는 이차원 리스트 apart를 정의하라.
#
# 101호	102호
# 201호	202호
# 301호	302호
apart = [['101호', '102호'], ['201호', '202호'], ['301호', '302호']]

# 182 아래 표에서 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의하라.
#
# 시가	종가
# 100	80
# 200	210
# 300	330
stock = [['시가', 100, 200, 300], ['종가', 80, 210, 320]]

# 183 아래 표를 stock 이름의 딕셔너리로 표현하라.시가를 key로 저장하고, 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다. 종가 역시 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.
#
# 시가	종가
# 100	80
# 200	210
# 300	330
stock = {'시가':[100, 200, 300], '종가':[80, 210, 330]}

# 184 아래 표를 stock 이라는 이름의 딕셔너리로 표현하라. 날짜를 key로 저장하고, 나머지 같은 행의 데이터를 리스트로 저장해서 value로 저장한다. 첫 열이 날짜이다.
#
# 10/10	80	110	70	90
# 10/11	210	230	190	200
stock = {'10/10':[80, 110, 70, 90], '10/11':[210, 230, 190, 200]}

# 185 리스트에 저장된 데이터를 아래와 같이 출력하라.
#
apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호
for flour in apart:
    for i in flour:
        print(i)

# 186 리스트에 저장된 데이터를 아래와 같이 출력하라.
#
apart = [ [101, 102], [201, 202], [301, 302] ]
# 301 호
# 302 호
# 201 호
# 202 호
# 101 호
# 102 호
for flour in range(len(apart)):
    r_i = len(apart)-1-flour
    for i in apart[r_i]:
        print(i)

# 187 리스트에 저장된 데이터를 아래와 같이 출력하라.
#
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 302 호
# 301 호
# 202 호
# 201 호
# 102 호
# 101 호
for flour in range(len(apart)):
    r_f = len(apart)-1-flour
    for i in range(len(apart[r_f])):
        r_i = len(apart[r_f])-1-i
        print(apart[r_f][r_i])

# 188 리스트에 저장된 데이터를 아래와 같이 출력하라.
#
apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# -----
# 102 호
# -----
# 201 호
# -----
# 202 호
# -----
# 301 호
# -----
# 302 호
# -----
for flour in apart:
    for i in flour:
        print(i, '호')
        print('-----')

# 189 리스트에 저장된 데이터를 아래와 같이 출력하라.
#
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# -----
# 201 호
# 202 호
# -----
# 301 호
# 302 호
# -----
for flour in apart:
    for i in flour:
        print(i, '호')
    print('-----')

# 190 리스트에 저장된 데이터를 아래와 같이 출력하라.
#
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호
# -----
for flour in apart:
    for i in flour:
        print(i, '호')
print('-----')

# 191 data에는 매수한 종목들의 OHLC (open/high/low/close) 가격 정보가 바인딩 되어있다.
#
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
#
# 수수료를 0.014 %로 가정할 때, 각 가격에 수수료를 포함한 가격을 한라인에 하나씩 출력하라.
#
# 2000.28
# 3050.427
# 2050.2870000000003
# ...
for company in data:
    for i in company:
        print(i*1.00014)

# 192 191번의 출력 결과에 행단위로 "----" 구분자를 추가하라.
#
# 2000.28
# 3050.427
# 2050.2870000000003
# 1980.2772
# ----
# 7501.05
# 2050.2870000000003
# 2050.2870000000003
# 1980.2772
# ----
# 15452.163
# 15052.107
# 15552.177
# 14902.086000000001
# ----
for company in data:
    for i in company:
        print(i*1.00014)
    print('----')

# 193 192 번 문제의 결괏값을 result 이름의 리스트에 1차원 배열로 저장하라.
#
# >> print(result)
# [2000.28, 3050.427, 2050.2870000000003, 1980.2772, 7501.05, 2050.2870000000003, 2050.2870000000003, ...]
result = []
for company in data:
    for i in company:
        charge = i*1.00014
        result.append(charge)
print(result)

# 194 191번 문제의 결괏값을 result 이름의 리스트에 2차원 배열로 저장하라. 저장 포맷은 아래와 같다. 각 행에 대한 데이터끼리 리스트에 저장되어야 한다.
#
# >> print(result)
# [
#  [2000.28, 3050.427, 2050.2870000000003, 1980.2772],
#  [7501.05, 2050.2870000000003, 2050.2870000000003, 1980.2772],
#  [15452.163, 15052.107, 15552.177, 14902.086000000001]
# ]
result = []
for company in data:
    company_list = []
    for i in company:
        charge = i*1.00014
        company_list.append(charge)
    result.append(company_list)
print(result)

# 195 ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 화면에 종가데이터를 출력하라.
#
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
# 100
# 190
# 310
for price in ohlc[1:]:
    print(price[-1])

# 196 ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 150원보다 큰경우에만 종가를 출력하라.
#
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 190
# 310
for price in ohlc[1:]:
    if price[-1] > 150:
        print(price[-1])

# 197 ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 시가 보다 크거나 같은 경우에만 종가를 출력하라.
#
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 100
# 310
for price in ohlc[1:]:
    if price[0] <= price[-1]:
        print(price[-1])

# 198 ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 고가와 저가의 차이를 변동폭으로 정의할 때 변동폭을 volatility 이름의 리스트에 저장하라.
#
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# >> print(volatility)
# [40, 30, 10]
volatility = []
for price in ohlc[1:]:
    gap = price[1] - price[2]
    volatility.append(gap)
print(volatility)

# 199 리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 종가가 시가보다 높은 날의 변동성 (고가 - 저가)을 화면에 출력하라.
#
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 종가가 시가보다 높은 거래일의 OHLC는 [300, 310, 300, 310] 이다. 따라서 이 거래일의 변동성은 10 (310 - 300)이다.
#
# 10
for price in ohlc[1:]:
    if price[-1] - price[0] > 0:
        gap = price[1] - price[2]
        print(gap)

# 200 리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산하라.
#
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 1일차 수익 0원 (100 - 100), 2일차 수익 -10원 (190 - 200), 3일차 수익 10원 (310 - 300) 이다.
#
# 0
total = 0
for price in ohlc[1:]:
    charge = price[-1] - price[0]
    print(charge)
    total += charge
    print(total)
print(total)

# 201 "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.

def print_coin():
    print('비트코인')

# 202 201번에서 정의한 함수를 호출하라.
print_coin()

# 203 201번에서 정의한 print_coin 함수를 100번 호출하라.
for i in range(0,100):
    print_coin()

# 204 "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
def print_coins():
    for i in range(0, 100):
        print('비트코인')

# 205 아래의 에러가 발생하는 이유에 대해 설명하라.
#
# hello()
# def hello():
#     print("Hi")
# 실행 예
#
# NameError: name 'hello' is not defined
# 풀이 : 함수가 정의되기 전에 함수가 호출되었기 때문에

# 206 아래 코드의 실행 결과를 예측하라.
#
# def message() :
#     print("A")
#     print("B")
#
# message()
# print("C")
# message()
# 풀이 :
# A
# B
# C
# A
# B

# 207 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
#
# print("A")
#
# def message() :
#     print("B")
#
# print("C")
# message()
# 풀이 :
# A
# C
# B

# 208 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
#
# print("A")
# def message1() :
#     print("B")
# print("C")
# def message2() :
#     print("D")
# message1()
# print("E")
# message2()
# 풀이 :
# A
# C
# B
# E
# D

# 209 아래 코드의 실행 결과를 예측하라.
#
# def message1():
#     print("A")
#
# def message2():
#     print("B")
#     message1()
#
# message2()
# 풀이 :
# B
# A

# 210 아래 코드의 실행 결과를 예측하라.
#
# def message1():
#     print("A")
#
# def message2():
#     print("B")
#
# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()
#
# message3()
# 풀이 :
# B
# C
# B
# C
# B
# C
# A

# 211 함수의 호출 결과를 예측하라.
#
# def 함수(문자열) :
#     print(문자열)
#
# 함수("안녕")
# 함수("Hi")
# 풀이 :
# 안녕
# Hi

# 212 함수의 호출 결과를 예측하라.
#
# def 함수(a, b) :
#     print(a + b)
#
# 함수(3, 4)
# 함수(7, 8)
# 풀이 :
# 7
# 15

# 213 아래와 같은 에러가 발생하는 원인을 설명하라.
#
# def 함수(문자열) :
#     print(문자열)
# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'
# 풀이 : 문자열을 인자로 받는 함수를 호출할때 인자(파라미터)를 입력하지 않았기 때문에

# 214 아래와 같은 에러가 발생하는 원인을 설명하라.
#
# def 함수(a, b) :
#     print(a + b)
#
# 함수("안녕", 3)
# TypeError: must be str, not int
# 풀이 : 함수의 파라미터간의 타입이 달라서 연산이 되지 않기 때문에

# 215 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
def print_with_smile(str):
    print(str, ':D')

# 216 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.
print_with_smile('안녕하세요')

# 217 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
def print_upper_price(price):
    print(price*1.3)

# 218 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
def print_sum(a,b):
    print(a + b)

# 219 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
#
# print_arithmetic_operation(3, 4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75
def print_arithmetic_opearation(a,b):
    print(a,'+',b,'=',a+b)
    print(a,'-',b,'=',a-b)
    print(a,'*',b,'=',a*b)
    print(a,'/',b,'=',a/b)

# 220 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.
def print_max(a,b,c):
    print(max(a,b,c))
