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