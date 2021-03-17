# number.py

print(type(123))
print(type(3.14))

print("3 + 2 = ", 3 + 2)
print("3 - 2 = ", 3 - 2)
print("3 * 2 = ", 3 * 2)
print("3 / 2 = ", 3 / 2)
print("3 % 2 = ", 3 % 2)
print("3 // 2 = ", 3 // 2)
print("3 ** 2 = ", 3 ** 2)

test = 3.141592
test1 = test2 = test
print(test)
print(test1)
print(test2)

num = 100
num += 10
print("num : ", num)
num -= 20
print("num : ", num)
num *= 2
print("num : ", num)
num /= 2
print("num : ", num)

# input()을 통해 받은 값은 무조건 'str' 문자열
st = input("아무 숫자나 입력해 보세요 ->")
print(st)
print(type(st))
# st에 있는 문자열을 int로 변환한 후 st에 저장
st = int(st)
# 변환된 st의 값에 10을 더함
print(st + 10)
# int로 형변환을 했으므로 'int'로 나옴
print(type(st))
