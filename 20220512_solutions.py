# 161 for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.
for i in range(0,100):
    print(i)

# 162 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.
#
# 2002
# 2006
# 2010
# ...
# 2042
# 2046
# 2050
# 참고) range의 세번 째 파라미터는 증감폭을 결정합니다.
#
# >> print(list(range(0, 10, 2)))
# [0, 2, 4, 6, 8]
for n in range(2002, 2051, 4):
    print(n)

# 163 1부터 30까지의 숫자 중 3의 배수를 출력하라.
#
# 3
# 6
# 9
# 12
# 15
# 18
# 21
# 24
# 27
# 30
for i in range(3, 31, 3):
    print(i)

# 164 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.
for n in range(0, 100):
    print(99 - n)

# 165 for문을 사용해서 아래와 같이 출력하라.
#
# 0.0
# 0.1
# 0.2
# 0.3
# 0.4
# 0.5
# ...
# 0.9
for i in range(0, 10):
    print(i/10)

# 166 구구단 3단을 출력하라.
#
# 3x1 = 3
# 3x2 = 6
# 3x3 = 9
# 3x4 = 12
# 3x5 = 15
# 3x6 = 18
# 3x7 = 21
# 3x8 = 24
# 3x9 = 27
for n in range(3, 30, 3):
    print('3*',int(n/3),'=',n)

# 167 구구단 3단을 출력하라. 단 홀수 번째만 출력한다.
#
# 3x1 = 3
# 3x3 = 9
# 3x5 = 15
# 3x7 = 21
# 3x9 = 27
for n in range(3, 30, 3):
    if n % 2 != 0:
        print('3*',int(n/3),'=',n)

# 168 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
#
# 합 : 55
total = 0
for i in range(1, 11):
    total += i
print(total)

# 169 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.
#
# 합: 25
total = 0
for i in range(1, 11, 2):
    total += i
print(total)

# 170 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
mutiple = 1
for i in range(1, 11):
    mutiple *= i
print(mutiple)

# 171 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
#
price_list = [32100, 32150, 32000, 32500]
# 32100
# 32150
# 32000
# 32500
for price in price_list:
    print(price)

# 172 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
#
# price_list = [32100, 32150, 32000, 32500]
# 0 32100
# 1 32150
# 2 32000
# 3 32500
for i, price in enumerate(price_list):
    print(i, price)

# 173 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
#
# price_list = [32100, 32150, 32000, 32500]
# 3 32100
# 2 32150
# 1 32000
# 0 32500
for i in range(len(price_list)):
    print((len(price_list)-1)-i, price_list[i])

# 174 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
#
# price_list = [32100, 32150, 32000, 32500]
# 100 32150
# 110 32000
# 120 32500
new_price_list = []
for i in range(len(price_list)):
    if price_list[i] % 100 == 0:
        new_price_list.append(price_list[i])
for n in range(len(new_price_list)):
    print((n+10)*10, new_price_list[n])

# 175 my_list를 아래와 같이 출력하라.
#
my_list = ["가", "나", "다", "라"]
# 가 나 // 0 1
# 나 다 // 1 2
# 다 라 // 2 3
for n in range(len(my_list)):
    if n+1 < len(my_list):
        print(my_list[n], my_list[n+1])

# 176 리스트를 아래와 같이 출력하라.
#
my_list = ["가", "나", "다", "라", "마"]
# 가 나 다
# 나 다 라
# 다 라 마
for n in range(len(my_list)):
    if n+2 < len(my_list):
        print(my_list[n], my_list[n+1], my_list[n+2])

# 177 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
#
my_list = ["가", "나", "다", "라"]
# 라 다
# 다 나
# 나 가
for n in range(len(my_list)):
    r_n = len(my_list)-1-n
    if r_n > 0:
        print(my_list[r_n], my_list[r_n-1])

# 178 리스트에는 네 개의 정수가 저장되어 있다. 각각의 데이터에 대해서 자신과 우측값과의 차분값을 화면에 출력하라.
#
my_list = [100, 200, 400, 800]
# 예를들어 100을 기준으로 우측에 위치한 200과의 차분 값를 화면에 출력하고, 200을 기준으로 우측에 위치한 400과의 차분값을 화면에 출력한다. 이어서 400을 기준으로 우측에 위치한 800과의 차분값을 화면에 출력한다.
#
# 100
# 200
# 400
for n in range(len(my_list)):
    if n+1 < len(my_list):
        print(my_list[n+1]-my_list[n])

# 179 리스트에는 6일 간의 종가 데이터가 저장되어 있다. 종가 데이터의 3일 이동 평균을 계산하고 이를 화면에 출력하라.
#
my_list = [100, 200, 400, 800, 1000, 1300]
# 첫 번째 줄에는 100, 200, 400의 평균값이 출력된다. 두 번째 줄에는 200, 400, 800의 평균값이 출력된다. 같은 방식으로 나머지 데이터의 평균을 출력한다.
#
# 233.33333333333334
# 466.6666666666667
# 733.3333333333334
# 1033.3333333333333
for n in range(len(my_list)):
    if n+2 < len(my_list):
        print((my_list[n]+my_list[n+1]+my_list[n+2])/3)

# 180 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
#
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(high_prices)):
    gap = high_prices[i]-low_prices[i]
    volatility.append(gap)
print(volatility)



