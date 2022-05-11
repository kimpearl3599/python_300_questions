# 131 for문의 실행결과를 예측하라.
#
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)
# 풀이 :
# 사과
# 귤
# 수박

# 132 for문의 실행결과를 예측하라.
#
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#   print("#####")
# 풀이 :
# #####
# #####
# #####

# 133 다음 for 문과 동일한 기능을 수행하는 코드를 작성하세요.
#
# for 변수 in ["A", "B", "C"]:
#   print(변수)
print('A')
print('B')
print('C')

# 134 for문을 풀어서 동일한 동작을하는 코드를 작성하라.
#
# for 변수 in ["A", "B", "C"]:
#   print("출력:", 변수)
print('출력:', 'A')
print('출력:', 'B')
print('출력:', 'C')

# 135 for문을 풀어서 동일한 동작을 하는 코드를 작성하라.
#
# for 변수 in ["A", "B", "C"]:
#   b = 변수.lower()
#   print("변환:", b)
alpha = 'A'
print('변환:', alpha.lower())
alpha = 'B'
print('변환:', alpha.lower())
alpha = 'C'
print('변환:', alpha.lower())

# 136 다음 코드를 for문으로 작성하라.
#
# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)
for 변수 in [10, 20, 30]:
    print(변수)

# 137 다음 코드를 for문으로 작성하라.
#
# print(10)
# print(20)
# print(30)
for 변수 in [10, 20, 30]:
    print(변수)

# 138 다음 코드를 for문으로 작성하라.
#
# print(10)
# print("-------")
# print(20)
# print("-------")
# print(30)
# print("-------")
for 변수 in [10, 20, 30]:
    print(변수)
    print("-------")

# 139 다음 코드를 for문으로 작성하라.
#
# print("++++")
# print(10)
# print(20)
# print(30)
print("++++")
for 변수 in [10, 20, 30]:
    print(변수)

# 140 다음 코드를 for문으로 작성하라.
#
# print("-------")
# print("-------")
# print("-------")
# print("-------")
for i in [10, 20, 30, 40]:
    print("-------")

# 141 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라. 단 부가세는 10원으로 가정한다.
#
리스트 = [100, 200, 300]
# 110
# 210
# 310
for i in 리스트:
    print(i+10)

# 142 for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.
#
리스트 = ["김밥", "라면", "튀김"]
# 오늘의 메뉴: 김밥
# 오늘의 메뉴: 라면
# 오늘의 메뉴: 튀김
for i in 리스트:
    print('오늘의 메뉴: ', i)

# 143 리스트에 주식 종목이름이 저장돼 있다.
#
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# 저장된 문자열의 길이를 다음과 같이 출력하라.
#
# 6
# 4
# 4
for i in 리스트:
    print(len(i))

# 144 리스트에는 동물이름이 문자열로 저장돼 있다.
#
리스트 = ['dog', 'cat', 'parrot']
# 동물 이름과 글자수를 다음과 같이 출력하라.
#
# dog 3
# cat 3
# parrot 6
for name in 리스트:
    print(name, len(name))

# 145 리스트에 동물 이름 저장돼 있다.
#
리스트 = ['dog', 'cat', 'parrot']
# for문을 사용해서 동물 이름의 첫 글자만 출력하라.
#
# d
# c
# p
for name in 리스트:
    print(name[0])

# 146 리스트에는 세 개의 숫자가 바인딩돼 있다.
#
리스트 = [1, 2, 3]
# for문을 사용해서 다음과 같이 출력하라.
#
# 3 x 1
# 3 x 2
# 3 x 3
for num in 리스트:
    print('3 *', num)

# 147 리스트에는 세 개의 숫자가 바인딩돼 있다.
#
리스트 = [1, 2, 3]
# for문을 사용해서 다음과 같이 출력하라.
#
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 정답확인
for num in 리스트:
    print('3 *', num, '=', 3*num)

# 148 리스트에는 네 개의 문자열이 바인딩돼 있다.
#
리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.
#
# 나
# 다
# 라
for word in 리스트[1:]:
    print(word)

# 149 리스트에는 네 개의 문자열이 바인딩돼 있다.
#
# 리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.
#
# 가
# 다
for word in 리스트[::2]:
    print(word)

# 150 리스트에는 네 개의 문자열이 바인딩돼 있다.
#
리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.
#
# 라
# 다
# 나
# 가
for word in 리스트[::-1]:
    print(word)

# 151 리스트에는 네 개의 정수가 저장돼 있다.
#
리스트 = [3, -20, -3, 44]
# for문을 사용해서 리스트의 음수를 출력하라.
#
# -20
# -3
for num in 리스트:
    if num < 0:
        print(num)

# 152 for문을 사용해서 3의 배수만을 출력하라.
#
리스트 = [3, 100, 23, 44]
# 3
for num in 리스트:
    if num % 3 == 0:
        print(num)

# 153 리스트에서 20 보다 작은 3의 배수를 출력하라
#
리스트 = [13, 21, 12, 14, 30, 18]
# 12
# 18
for num in 리스트:
    if num % 3 == 0 and num < 20:
        print(num)

# 154 리스트에서 세 글자 이상의 문자를 화면에 출력하라
#
리스트 = ["I", "study", "python", "language", "!"]
# study
# python
# language
for word in 리스트:
    if len(word) >= 3:
        print(word)

# 155 리스트에서 대문자만 화면에 출력하라.
#
리스트 = ["A", "b", "c", "D"]
# A
# D
for alpha in 리스트:
    if alpha.isupper():
        print(alpha)

# 156 리스트에서 소문자만 화면에 출력하라.
#
리스트 = ["A", "b", "c", "D"]
# b
# c
for alpha in 리스트:
    if alpha.islower():
        print(alpha)

# 157 이름의 첫 글자를 대문자로 변경해서 출력하라.
#
리스트 = ['dog', 'cat', 'parrot']
# Dog
# Cat
# Parrot
for word in 리스트:
    if word[0].isupper():
        print(word)
    else:
        print(word.capitalize())

# 158 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)
#
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# hello
# ex01
# intro
for file in 리스트:
    print(file.split('.')[0])

# 159 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.
#
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# define.h
for file in 리스트:
    if file.endswith('h') == True:
        print(file)

# 160 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.
#
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# intra.c
for file in 리스트:
    if file.endswith(('h', 'c')):
        print(file)