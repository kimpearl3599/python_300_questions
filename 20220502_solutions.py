# 화면에 Hello World 문자열을 출력하세요.
print('Hello World')

# 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)
print('Mary\'s cosmetics')

# 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)
print('신씨가 소리질렀다. "도둑이야".')

# 화면에 "C:\Windows"를 출력하세요.
print('"C:\Windows"')

# 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
print("안녕하세요.\n만나서\t반갑습니다.")
# 풀이 : \t는 띄어쓰기, \n은 줄바꿈

# print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
print ("오늘은", "일요일")
# 풀이 : 오늘은 일요일
# 자동으로 띄어쓰기됨

# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver;kakao;sk;samsung
print('naver', 'kakao', 'samsung', sep=";")
# 출력되는 값을 사이에 한칸의 공백마다 출력되는 값을 sep의 인자로 정해줌

# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver/kakao/sk/samsung
print('naver', 'kakao', 'samsung', 'sk', sep="/")

# 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
print("first");print("second")
print('first', end='');print('second')

# 5/3의 결과를 화면에 출력하세요.
print(5/3)

# 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
# 바인딩? 프로그램에 사용된 구성요소의 실제값 또는 프로퍼티를 결정짓는 행위
SamsungElectronics = 50000
print(SamsungElectronics * 10)

# 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
# 항목	값
# 시가총액	298조
# 현재가	50,000원
# PER	15.79
total = 298 * 1000 * 1000 * 1000
CurrentPrice = 50000
per = 15.79
print(total, type(total))
print(CurrentPrice, type(CurrentPrice))
print(per, type(per))

# >> s = "hello"
# >> t = "python"
# 두 변수를 이용하여 아래와 같이 출력해보세요.
#
# 실행 예:
# hello! python
s = "hello"
t = "python"
print(s + '!\t' + t)

# 아래 코드의 실행 결과를 예상해보세요.
#
# >> 2 + 2 * 3
print(2 + 2 * 3)
# 풀이 : 8

# type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
#
# >> a = 128
# >> print (type(a))
# <class 'int'>
# 아래 변수에 바인딩된 값의 타입을 판별해보세요.
#
a = "132"
print(type(a))

# 문자열 '720'를 정수형으로 변환해보세요.
num_str = "720"
print(int(num_str), type(int(num_str)))

# 정수 100을 문자열 '100'으로 변환해보세요.
num = 100
print(str(num), type(str(num)))

# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
num = 15.79
print(float(num), type(float(num)))

# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
#
year = "2020"
print(int(year), int(year)-1, int(year)-2, int(year)-3, type(int(year)))

# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
cost_per_month = 48584
installment = 36
total_cost = cost_per_month * installment
print(total_cost)

