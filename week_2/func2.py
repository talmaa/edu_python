dic2 = {"name":"홍길동", "job":"도둑", "address":["울릉도", "제주도", "함경도"]}
# 딕셔너리 전체 출력
print(dic2)
# 주소만 출력
print(dic2["address"])
# 제주도만 출력
print(dic2["address"][1])

dic2["age"] = 33
print(dic2)

dic2["name"] = "전우치"
print(dic2)

del dic2["job"]
# dic2에서 "job"이라는 키를 가진 데이터 삭제
print(dic2)
# {'name': '전우치', 'address': ['울릉도', '제주도', '함경도'], 'age': 33}

# del dic2["job"]
# 존재하지 않는 키를 삭제할 경우 KeyError 발생

# dic2에 "address"라는 키가 존재하는지 검사 후 존재하면 그 값을 출력
# 존재하지 않으면 "존재하지 않는 키입니다."라고 출력

if "address" in dic2 :
    print(dic2["address"])
else : 
    print("존재하지 않는 키입니다.")

# 3항 연산자
print(dic2["job"] if "job" in dic2 else "존재하지 않는 키입니다.") 

print(dic2.get("job"))

#위와 같은 기능을 in 이 아닌 get() 함수로 작업
# if dic2.get("address") is not None :
if dic2.get("address") != None :
    print(dic2["address"])
else : 
    print("존재하지 않는 키입니다.")

print("-----------------------")

for key in dic2 : 
    print(key, ":", dic2[key])

lst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
print("-----------------------")
# 리스트 전체 출력 : index 0 ~ lst length -1
for i in range(len(lst)) :
    print(lst[i])
    # a b c d e f g h i j k
print("-----------------------")
# 리스트 c부터 h까지 출력 : index 2 ~ lst length -3
for i in range(2, len(lst) - 3) :
    print(lst[i])
    # c d e f g h

print("-----------------------")
# 리스트 a부터 2씩 증가하여 마지막까지 출력 : index 0, 2, 4, .. , lst length -1
for i in range(0, len(lst), 2) :
    print(lst[i])
    # a c e g i k

print("-----------------------")
# 리스트 k부터 a까지 역순으로 출력
for i in range(len(lst), 0, -1) :
    print(lst[i - 1])
    # k j i h g f e d c b a
print("-----------------------")
for i in reversed(range(len(lst))) :
          print(lst[i])
          # k j i h g f e d c b a

print("-----------------------")
import datetime
now = datetime.datetime.now()
print(now)
print(type(now))
print(now.year, "년", type(now.year))
print(now.month, "월", type(now.month))
print(now.day, "일", type(now.day))
print(now.hour, "시", type(now.hour))
print(now.minute, "분", type(now.minute))
print(now.second, "초", type(now.second))
print(now.microsecond, "마이크로초", type(now.microsecond))

# 12, 1, 2월은 "겨울" / 3, 4 ,5 월은 "봄" / 6, 7, 8 월은 "여름" / 9, 10, 11월은 "가을"
# 오늘 날자를 기준으로 계절을 출력
now = datetime.datetime.now()
month = now.month
#if month == 12 or (1 <= month <= 2) : # 요래짜니 가독성이 안좋음
#    print("겨울")
#elif 3 <= month <= 5 :
if 3 <= month <= 5 :
    print("봄")
elif 6 <= month <= 8 :
    print("여름")
elif 9 <= month <= 11 :
    print("가을")
else : 
    print("겨울")

i = 0
while i < 10 :
    print("{}번째 반복".format(i))
    i += 1
    # 0번째 반복 .. 9번째 반복

lst = [1, 2, 1, 2, 3, 4]
val = 2
while val in lst :
    lst.remove(val)
    # remove() 함수로 val을 삭제하여 루프문을 빠져나옴

print(lst)
# [1, 1, 3, 4]

import time
print(time.time())
cnt = 0
target = time.time() + 2
#while time.time() < target :
#    cnt += 1

print("2초 동안 {}번 반복".format(cnt))

# 무한루프\
'''
i = 1
while True :
    print("{}번째 반복".format(i))
    i += 1
    ipt = input("> 종료하시겠습니까? y/n :")
    if ipt.lower() == "y" :
        print("반복 종료")
        break
'''

lst = [1, 3, 12, 15, 4, 55, 9]
# lst안의 값들 중 10보다 큰 값만 출력
for item in lst :
    if item > 10 :
        print(item)

print("-----------------------")

# continue 활용
for item in lst :
    if item < 10 :
        continue

    print(item)
print("-----------------------")
# 100 이하의 자연수 중에서 5와 7의 최소공배수를 구하여 출력
for i in range(1, 100) :
    if i % 5 == 0 and i % 7 == 0 :
        print(i)
        break
print("-----------------------")
# 100 이하의 자연수 중에서 9의 배수들의 합을 출력
ret = 0
i = 0
while i <= 100 :
    ret += i
    i += 9
print(ret)

print("-----------------------")
# 1000이하의 자연수 중 8이 들어가는 수의 개수
cnt = 0
for i in range(1001) :
    if str(i).find("8") != -1 :
        cnt += 1
print(cnt)

print("-----------------------")
lst = [112, 20, 4, 34, 56]
print(min(lst))
print(max(lst))
print(sum(lst))

lst_r = reversed(lst)
print(lst_r)
print(list(lst_r))

print(enumerate(lst))
print(list(enumerate(lst)))

for i, val in enumerate(lst) :
    print(i, ":", val)

print(dic2.items())
for key, val in dic2.items() :
    print(key, ":", val)

s = "::".join(["ab", "cd", "ef", "gh", "ij"])
print(s)
# ab::cd::ef::gh::ij