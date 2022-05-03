# 21 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'python'
first = letters[0]
third = letters[2]
print(first, third)

# 22 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
print(license_plate[-4:])

# 23 아래의 문자열에서 '홀' 만 출력하세요.
string = "홀짝홀짝홀짝"
# for i in string:
#     if i == '홀':
#         print(i, end='', sep='')
print(string[::2])
# 시작인덱스:끝인덱스:오프셋

# 24 문자열을 거꾸로 뒤집어 출력하세요.
string = "PYTHON"
print(string[::-1])

# 25 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
print(phone_number.replace('-', ' '))

# 26 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
phone_number = "010-1111-2222"
print(phone_number.replace('-', ''))

# 27 url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
url = "http://sharebook.kr"
print(url.split('.')[-1])

# 28 아래 코드의 실행 결과를 예상해보세요.
lang = 'python'
# lang[0] = 'P'
print(lang)
# 풀이 : Error msg (문자열은 immutable)

# 29 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))

# 30 아래 코드의 실행 결과를 예상해보세요.
string = 'abcd'
string.replace('b', 'B')
print(string)
# 풀이 : abcd (문자열은 변경할 수 없는 자료형. 원본은 그대로 둔채 새로운 문자열 객체 리턴)


# 31 아래 코드의 실행 결과를 예상해보세요.
a = "3"
b = "4"
print(a + b)
# 풀이 : 34

# 32 아래 코드의 실행 결과를 예상해보세요.
print("Hi" * 3)
# 풀이 : HiHiHi

# 33 화면에 '-'를 80개 출력하세요.
print('-'*80)

# 34 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
t1 = 'python'
t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
# python java python java python java python java
print((t1 + '\t' + t2)*4)

# 35 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13

test1 = '이름: %s' % name1 + '\t' + '나이: %i' % age1
test2 = '이름: %s' % name2 + '\t' + '나이: %i' % age2
print(test1)
print(test2)
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 36 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.
test1 = '이름: {} 나이: {}'.format(name1, age1)
test2 = '이름: {} 나이: {}'.format(name2, age2)
print(test1)
print(test2)

# 37 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
test1 = f'이름: {name1} 나이: {age1}'
test2 = f'이름: {name2} 나이: {age2}'
print(test1)
print(test2)

# 38 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
상장주식수 = "5,969,782,550"
print(int(상장주식수.replace(',','')), type(int(상장주식수.replace(',',''))))

# 39 다음과 같은 문자열에서 '2020/03'만 출력하세요.
분기 = "2020/03(E) (IFRS연결)"
print(분기.split('(')[0])

# 40 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
data = "   삼성전자    "
print(data.strip())

# 41 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
ticker = "btc_krw"
print(ticker.upper())

# 42 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
ticker = "BTC_KRW"
print(ticker.lower())

# 43 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
text = 'hello'
print(text.capitalize())

# 44 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))

# 45 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
file_name = "보고서.xls"
print(file_name.endswith(('xlsx', 'xls')))

# 46 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

# 47 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "hello world"
print(a.split(' '))

# 48 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker = "btc_krw"
print(ticker.split('_'))

# 49 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
date = "2020-05-01"
print(date.split('-'))

# 50 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
data = "039490     "
print(data.rstrip())



