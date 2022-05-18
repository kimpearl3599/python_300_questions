# 221 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
#
# print_reverse("python")
# nohtyp
def print_reverse(str):
    new_str = ''
    for i in range(len(str)):
        r_i = len(str)-1-i
        new_str += str[r_i]
    print(new_str)


print_reverse('python')

# 222 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
#
# print_score ([1, 2, 3])
# 2.0
def print_score(score_list):
    total = 0
    for i in score_list:
        total += i
    print(total/len(score_list))

print_score([1,2,3])

# 223 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
#
# print_even ([1, 3, 2, 10, 12, 11, 15])
# 2
# 10
# 12
def print_even(list):
    for i in list:
        if i % 2 == 0:
            print(i)

print_even ([1, 3, 2, 10, 12, 11, 15])

# 224 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
#
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# 이름
# 나이
# 성별
def print_keys(dict):
    for i in dict.keys():
        print(i)

print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 225 my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.
#
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.
#
# print_value_by_key  (my_dict, "10/26")
# [100, 130, 100, 100]
def print_value_by_key(dict,date):
    for i in dict:
        if i == date:
            print(dict[i])

print_value_by_key(my_dict, "10/26")

# 226 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
#
# print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸
def print_5xn(str):
    print(str[:5])
    print(str[5:])

print_5xn("아이엠어보이유알어걸")

# 227 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
#
# printmxn("아이엠어보이유알어걸", 3)
# 아이엠
# 어보이
# 유알어
# 걸
def print_mxn(str, num):
    repeat_num = int(len(str)/num)+1
    for i in range(0,repeat_num):
        print(str[num*i:num*(i+1)])

print_mxn("아이엠어보이유알어걸", 3)

# 228 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
#
# calc_monthly_salary(12000000)
# 1000000
def calc_monthly_salary(annual):
    salary = int(annual/12)
    print(salary)

calc_monthly_salary(12000000)

# 229 아래 코드의 실행 결과를 예측하라.
#
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(a=100, b=200)
# 풀이 :
# 왼쪽: 100
# 오른쪽: 200

# 230 아래 코드의 실행 결과를 예측하라.
#
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(b=100, a=200)
# 풀이 :
# 왼쪽: 200
# 오른쪽: 100

# 231 아래 코드를 실행한 결과를 예상하라.
#
# def n_plus_1 (n) :
#     result = n + 1
#
# n_plus_1(3)
# print (result)
# 풀이 : 4가 나올꺼라고 생각했지만, result라는 변수가 함수 내에
# 정의되어있기 때문에 함수 밖에서 호출할 수 없다.

# 232 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
#
# make_url("naver")
# www.naver.com
def make_url(url):
    return 'www.'+url+'.com'

make_url("naver")

# 233 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
#
# make_list("abcd")
# ['a', 'b', 'c', 'd']
def make_list(str):
    return list(str)

print(make_list("abcd"))

# 234 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
#
# pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]
def pickup_even(list):
    new_list = []
    for i in list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

print(pickup_even([3, 4, 5, 6, 7, 8]))

# 235 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
#
# convert_int("1,234,567")
# 1234567
def convert_int(str_with_num):
    transfer_num = str_with_num.replace(',','')
    return int(transfer_num)

print(convert_int("1,234,567"))

# 236 아래 코드의 실행 결과를 예측하라.
#
# def 함수(num) :
#     return num + 4
#
# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)
# 풀이 :
# 22

# 237 아래 코드의 실행 결과를 예측하라.
#
# def 함수(num) :
#     return num + 4
#
# c = 함수(함수(함수(10)))
# print(c)
# 풀이 :
# 22

# 238 아래 코드의 실행 결과를 예측하라.
#
# def 함수1(num) :
#     return num + 4
#
# def 함수2(num) :
#     return num * 10
#
# a = 함수1(10)
# c = 함수2(a)
# print(c)
# 풀이 :
# 140

# 239 아래 코드의 실행 결과를 예측하라.
#
# def 함수1(num) :
#     return num + 4
#
# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)
#
# c = 함수2(10)
# print(c)
# 풀이 :
# 16

# 240 아래 코드의 실행 결과를 예측하라.
#
# def 함수0(num) :
#     return num * 2
#
# def 함수1(num) :
#     return 함수0(num + 2)
#
# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)
#
# c = 함수2(2)
# print(c)
# 풀이 :
# 28