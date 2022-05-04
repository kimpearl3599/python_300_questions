# 51 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']

# 52 051의 movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank.append('배트맨')
print(movie_rank)

# 53 movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)

# 54 movie_rank 리스트에서 '럭키'를 삭제하라.
print(movie_rank.pop(3))
print(movie_rank)

# 55 movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 56 lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 57 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
nums = [1, 2, 3, 4, 5, 6, 7]
max_num = max(nums)
min_num = min(nums)
print('max: ', max_num)
print('min: ', min_num)

# 58 다음 리스트의 합을 출력하라.
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 59 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 60 다음 리스트의 평균을 출력하라.
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))

# 61 price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 62 슬라이싱을 사용해서 홀수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 63 슬라이싱을 사용해서 짝수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# 64 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 65 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 Naver
print(interest[0], interest[2])

# 66 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
print(" ".join(interest))
# join의 역할 : 리스트안의 문자열을 합쳐줌(int 타입은 합칠 수 없음)

# 67 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
print("/".join(interest))

# 68 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우
print("\n".join(interest))

# 69 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장하라.
interest = string.split('/')
print(interest)

# 70 리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))
# sort는 원본이 바뀌고, sorted는 원본이 바뀌지 않음

# 71 my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()
print(type(my_variable))

# 72 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')

# 73 숫자 1 이 저장된 튜플을 생성하라.
num = (1, )
print(type(num))
# 하나의 데이터가 저장되는 경우 쉼표를 입력해야한다.

# 74 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
#
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment

# 풀이 : 튜플은 데이터(원소)를 변경할 수 없기 때문에

# 75 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
t = 1, 2, 3, 4
print(type(t))
# 풀이 : 튜플 (원칙적으로 괄호로 정의해야하지만, 괄호 없이도 동작)

# 76 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
t = ('a', 'b', 'c')
# 튜플의 값은 변경할 수 없기 때문에 새로운 튜플을 만들어서 덮어씌워줌
t = ('A', 'b', 'c')
print(t)

# 77 다음 튜플을 리스트로 변환하라.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))

# 78 다음 리스트를 튜플로 변경하라.
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest))

# 79 다음 코드의 실행 결과를 예상하라.
#
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# 풀이 : apple banana cake

# 80 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
nums = ()
print(tuple(range(2,100,2)))
# 2부터 100까지 오프셋 2만큼 띄워서 튜플리스트를 생성