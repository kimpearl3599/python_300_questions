# 81 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다. 하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다. 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(valid_score)

# 82 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = scores
print(valid_score)

# 83 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, *valid_score,_ = scores
print(valid_score)

# 84 temp 이름의 비어있는 딕셔너리를 만들라.
temp = {}

# 85 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
#
# 이름	희망 가격
# 메로나	1000
# 폴라포	1200
# 빵빠레	1800
icecreams = {'메로나': 1000, '폴라포':1200, '빵빠레': 1800}
print(icecreams)

# 86 085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
#
# 이름	희망 가격
# 죠스바	1200
# 월드콘	1500
new = {'죠스바': 1200, '월드콘': 1500}
icecreams.update(new)
print(icecreams)
# icecreams['죠스바'] = 1200
# icecreams['월드콘'] = 1500

# 87 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
# 실행 예:
# 메로나 가격: 1000
print('메로나 가격: ', ice['메로나'])

# 88 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice['메로나'] = 1300
print(ice)

# 89 다음 딕셔너리에서 메로나를 삭제하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice.pop('메로나')
# del ice['메로나']
print(ice)

# 90 다음 코드에서 에러가 발생한 원인을 설명하라.
# >> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# >> icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'
# 풀이 : '누가바' 라는 키값이 없기 때문에 인덱싱을 하면 에러가 발생

# 91 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.
# 이름	가격	재고
# 메로나	300	20
# 비비빅	400	3
# 죠스바	250	100
inventory = {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100]}
print(inventory)

# 92 inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
# 실행 예시:
# 300 원
print(inventory['메로나'][0], ' 원')

# 93 inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
print(inventory['메로나'][1], ' 개')

# 94 inventory 딕셔너리에 아래 데이터를 추가하라.
# 이름	가격	재고
# 월드콘	500	7
inventory['월드콘'] = [500, 7]
print(inventory)

# 95 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice_list = list(icecream.keys())
print(ice_list)

# 96 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice_value = list(icecream.values())
print(ice_value)

# 97 icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
ice_value_sum = sum(icecream.values())
print(ice_value_sum)

# 98 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

# 99 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
# for pair in zip(keys, vals):
#     print(pair)
#
# numbers = [1,2 , 3]
# letters = ["A","B","C"]
# print(type(zip(numbers, letters)))
#
# pair = zip(numbers, letters)
# print(type(pair), pair)
#
# for pair in zip(numbers, letters):
#     print(type(pair), pair)

print(zip(keys, vals), type(zip(keys, vals)))
result = dict(zip(keys, vals))
result2 = list(zip(keys, vals))
print(result)
print(result2)
# zip은 무언인가? 두 그룹의 데이터를 서로 엮어주는 역할을 가진 파이썬의 내장함수
# 객체를 인자로 받고 원소를 튜플형태의 반복자로 반환, 병렬처리 가능, unzip 가능

# 100 date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)





