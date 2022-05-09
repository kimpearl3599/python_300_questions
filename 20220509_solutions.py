# 101 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
# 풀이 : boolean 타입

# 102 아래 코드의 출력 결과를 예상하라
print(3 == 5)
# 풀이 : False

# 103 아래 코드의 출력 결과를 예상하라
print(3 < 5)
# 풀이 : True

# 104 아래 코드의 결과를 예상하라.
x = 4
print(1 < x < 5)
# 풀이 : True

# 105 아래 코드의 결과를 예상하라.
print ((3 == 3) and (4 != 3))
# 풀이 : True

# 106 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
print('106', 3 >= 4)
# 풀이 : 3이 4보다 같거나 크다로 비교할때는 부등호가 앞, 등호가 뒤로 와야함

# 107 아래 코드의 출력 결과를 예상하라
if 4 < 3:
    print("Hello World")
# 풀이 : 아무것도 출력되지 않는다.

# 108 아래 코드의 출력 결과를 예상하라
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
# 풀이 : Hi, there.

# 109 아래 코드의 출력 결과를 예상하라
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
# 풀이 : 4(라고 생각했는데 정답이 아니다.왜지? if 조건에 True가 들어가면 무조건 실행)
# 1
# 2
# 4

# 110 아래 코드의 출력 결과를 예상하라
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
# 풀이
# 3
# 5

# 111 사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.
# >> 안녕하세요
# 안녕하세요안녕하세요
# print(input(str())*2)

# 112 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
# >> 숫자를 입력하세요: 30
# 40
# num = input('숫자를 입력하세요: ')
# print(int(num) + 10)
# 풀이 : input안의 문자열은 placeholder 역할인건가...

# 113 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
# >> 30
# 짝수
# user = int(input())
# if user % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# 114 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라. 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.
# >> 입력값: 200
# 출력값: 220
# >> 입력값: 240
# 출력값: 255
# user = int(input('입력값: '))
# if user+20 > 255:
#     user = 255
#     print('출력값:', user)
# else:
#     print('출력값:', user+20)

# 115 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 출력 값의 범위는 0~255이다. 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.
# >> 입력값: 200
# 출력값: 180
# >> 입력값: 15
# 출력값: 0
# user = int(input('입력값: '))
# if user-20 < 0:
#     print('출력값:', 0)
# elif user-20 > 255:
#     print('출력값:', 255)
# else:
#     print('출력값:', user-20)

# 116 사용자로부터 입력 받은 시간이 정각인지 판별하라.
# >> 현재시간:02:00
# 정각 입니다.
# >> 현재시간:03:10
# 정각이 아닙니다
# user = str(input('현재시간: '))
# min = user.split(':')[1]
# if min != '00':
#     print('정각이 아닙니다.')
# else:
#     print('정각 입니다.')

# 117 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = ["사과", "포도", "홍시"]
# # >> 좋아하는 과일은? 사과
# # 정답입니다.
# user = str(input('좋아하는 과일은?'))
# if user in fruit:
#     print('정답입니다.')
# else:
#     print('오답입니다.')
# 리스트 안에 있는 것을 확인할때는 in 을 사용한다.

# 118 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# user = str(input('투자종목을 입력하세요: '))
# if user in warn_investment_list:
#     print('투자 경고 종목입니다.')
# else:
#     print('투자 경고 종목이 아닙니다.')

# 119 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = str(input('제가 좋아하는 계절은: '))
# print(fruit.keys())
# if user in fruit.keys():
#     print('정답입니다.')
# else:
#     print('오답입니다.')

# 120 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = str(input('좋아하는 과일은? '))
# if user in fruit.values():
#     print('정답입니다.')
# else:
#     print('오답입니다.')

# 121 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
# user = str(input())
# if user.isupper() == True:
#     print(user.lower())
# else:
#     print(user.upper())

# 122 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
#
# 점수	학점
# 81~100	A
# 61~80	B
# 41~60	C
# 21~40	D
# 0~20	E
# score = int(input('score: '))
# if score > 80:
#     print('A')
# elif score > 60:
#     print('B')
# elif score > 40:
#     print('C')
# elif score > 20:
#     print('D')
# else:
#     print('E')

# 123 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
#
# 통화명	환율
# 달러	1167
# 엔	1.096
# 유로	1268
# 위안	171
# user = input('입력: ')
# money, currency = user.split(' ')
# if str(currency) == '달러':
#     print(int(money)*1167)
# elif str(currency) == '엔':
#     print(int(money)*1.096)
# elif str(currency) == '유로':
#     print(int(money)*1268)
# elif str(currency) == '위안':
#     print(int(money)*171)

# 124 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
#
# >> input number1: 10
# >> input number2: 9
# >> input number3: 20
# 20
# first = int(input('input number1: '))
# second = int(input('input number2: '))
# third = int(input('input number3: '))
# print(min(first, second, third))

# 125 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
#
# 번호	통신사
# 011	SKT
# 016	KT
# 019	LGU
# 010	알수없음
# >> 휴대전화 번호 입력: 011-345-1922
# 당신은 SKT 사용자입니다.
# user = input('휴대전화 번호 입력: ')
# company = user.split('-')[0]
# if company == '011':
#     print('당신은 SKT 사용자')
# elif company == '016':
#     print('당신은 KT 사용자')
# elif company == '019':
#     print('당신은 LGU 사용자')
# else:
#     print('알수없음')

# 126 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.
#
# -	0	1	2	3	4	5	6	7	8	9
# 01	강북구	강북구	강북구	도봉구	도봉구	도봉구	노원구	노원구	노원구	노원구
# 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라
#
# >> 우편번호: 01400
# 도봉구
# user = input('우편번호: ')
# num = user[1:3]
# if int(num) < 13:
#     print('강북구')
# elif int(num) < 16:
#     print('도봉구')
# elif int(num) < 20:
#     print('노원구')

# 127 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다. 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
#
# >> 주민등록번호: 821010-1635210
# 남자
# user = input('주민등록번호:')
# gender = user.split('-')[1][0]
# if int(gender) == 2:
#     print('여자')
# else:
#     print('남자')

# 128 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
#
# 지역코드	출생지
# 00 ~ 08	서울
# 09 ~ 12	부산
# >> 주민등록번호: 821010-1635210
# 서울이 아닙니다.
# >> 주민등록번호: 861010-1015210
# 서울 입니다.
# user = input('주민등록번호: ')
# region = user.split('-')[1][1:3]
# if int(region) > 8:
#     print('서울이 아닙니다.')
# elif int(region) >= 0:
#     print('서울 입니다.')

# 129 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다. 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다. 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.
#
#   8 2 1 0 1 0 - 1 6 3 5 2 1 0
# x 2 3 4 5 6 7   8 9 2 3 4 5
# -----------------------------
# 1차 계산: (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) = (128 % 11) = 7
# 2차 계산: 11 -7 = 4
# 위와 같이 821010-1635210에 대해서 계산을 해보면 마지막 자리는 4가 되어야 함을 알 수 있다. 즉, 821010-1635210은 유효하지 않은 주민등록번호임을 알 수 있다.
#
# 다음과 같이 사용자로부터 주민등록번호를 입력받은 후 주민등록번호가 유효한지를 출력하는 프로그램을 작성하라.
#
# >> 주민등록번호: 821010-1635210
# 유효하지 않은 주민등록번호입니다.
# user = input('주민등록번호:')
# num = user.split('-')[0]+user.split('-')[1][:-1]
# array = [2,3,4,5,6,7,8,9,2,3,4,5]
# total = 0
# for i in range(len(num)):
#     total += int(num[i])*array[i]
# last_num = 11 - (total % 11)
# num_end = user.split('-')[1][-1]
# if last_num == int(num_end):
#     print('유효한 주민등록번호 입니다.')
# else:
#     print('유효하지 않은 주민등록번호 입니다.')


# 130 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.
#
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.
#
# Key Name	Description
# opening_price	최근 24시간 내 시작 거래금액
# closing_price	최근 24시간 내 마지막 거래금액
# min_price	최근 24시간 내 최저 거래금액
# max_price	최근 24시간 내 최고 거래금액
change = int(btc['max_price']) - int(btc['min_price']) + int(btc['opening_price'])
if change > int(btc['max_price']):
    print('상승장')
else:
    print('하락장')




