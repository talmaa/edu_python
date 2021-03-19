lst = [1, 2, 3, 4, 5]
# 리스트의 가장 뒤에 10을 추가
lst.append(10)
print(lst)
# [1, 2, 3, 4, 5, 10]

# 3번 인덱스 자리에 22를 삽입
lst.insert(3, 22)
print(lst)
# [1, 2, 3, 22, 4, 5, 10]

# lst의 뒤에 지정한 리스트 추가
# lst += [4, 5, 6] 과 결과가 같아 보이나, +=는 새로운 리스트를 생성하므로 속도가 더 느림
lst.extend([4, 5, 6])
print(lst)
# [1, 2, 3, 22, 4, 5, 10, 4, 5, 6]

# 데이터 10의 인덱스 검색
print(lst.index(10))
# 6

# lst 3번 인덱스 자리의 데이터 삭제
del lst[3]
print(lst)
# [1, 2, 3, 4, 5, 10, 4, 5, 6]

a = lst.pop(4)
print(a, lst)
# 5 [1, 2, 3, 4, 10, 4, 5, 6]

# lst에서 마지막 요소를 뽑아 a에 저장
a = lst.pop()
print(a, lst)
# 6 [1, 2, 3, 4, 10, 4, 5]

# lst에서 3이라는 값을 삭제
lst.remove(3)
print(lst)
# [1, 2, 4, 10, 4, 5]

# lst의 모든 요소 삭제
lst.clear()
print(lst)
# []

lst = ["ab", "cd", "ef", "gh", "ij"]
print("cd" in lst)
# True

if "ij" in lst : 
    print("성공")
else :
    print("실패")

# 오 3항 연산자 쌉가능
print("성공" if ("ij" in lst) else "실패")

# lst에 "ij"와 "zz"가 있으면 "성공" 없으면 "실패"
if "ij" in lst and "zz" in lst : 
    print("성공")
else :
    print("실패")

# 3항 연산자
print("성공" if ("ij" in lst and "zz" in lst) else "실패")


# lst에 "ij"와 "zz"가 있으면 "성공" 없으면 "실패"
if "ij" in lst or "zz" in lst : 
    print("성공")
else :
    print("실패")

# 3항 연산자
print("성공" if ("ij" in lst or "zz" in lst) else "실패")

for i in range(1, 5) : # i의 값이 0부터 5가 될 때 까지 루프를 돔
    print(i)
    # 0 1 2 3 4

print("----------------------------------")
# lst 리스트이 모든 데이터를 차례대로 출력(for문 이용) 1
for i in range(len(lst)) : 
    print(lst[i])
    # ab cd ef gh ij

print("----------------------------------")
# lst 리스트이 모든 데이터를 차례대로 출력(for문 이용) 2
# lst 데이터들을 끝가지 차례대로 tmp에 저장함
for tmp in lst : 
    print(tmp)
    # ab cd ef gh ij

dic = {"키1":"값1", "키2":"값2", "키1":"aa", "키3":"값2"}
print(dic)
print(dic["키1"])
# print(dic["키"])
# 존재하지 않는 키를 호출할 경우 KeyError 발생

for tmp in dic : 
    # 키 호출
    print(tmp)
    # 값 호출
    print(dic[tmp])
    # 키1, aa, 키2, 값2, 키3, 값2

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