#func.py

s = "{}세기는 {}년 부터 {}년 {}입니다.".format(20, 1901, 2000, "까지")
print(s)
#output -> 20세기는 1901년 부터 2000년 까지입니다.
print(type(s))

s = "abCD가나다efGH"
print(s.upper())
print(s.lower())
print(s)

# 대문자로 변경된 값을 s1에 대입
s1 = s.upper()
print(s1)

# 소문자로 변경된 값을 s2에 대입
s2 = s.lower()
print(s2)

s = "   abc   def   "
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s)

# 문자열이 글자과 숫자로만 구성되었는지 여부를 리턴
print("abc123".isalnum())
# True

# 문자열이 글자로만 구성되었는지 여부를 리턴
print("abc...123".isalnum())
# False

print("abc가나다".isalpha())
# True

print("-123".isdecimal())
# False

print("123456".isdigit())
# Ture

print("   ".isspace())
# Ture

print("abc".islower())
# Ture

print("ABC".isupper())
# Ture

s = "abcdabcd"
print(s.find("bcd"))
print(s.rfind("bcd"))

print("abc" in s)
print("zzz" in s)

a = "ab:cd:ef:gh".split(":")
print(a)
# ['ab', 'cd', 'ef', 'gh']

a = (10 > 3)
b = (10 < 3)
print(a, b)

a = ("abc" > "zzz")
b = ("azz" > "bbb")
c = ("Z" > "a")
d = ("가" < "힣")
print(a, b, c, d)

num = int(input("숫자입력 > "))
if num % 2 == 0 :
    print("짝수입니다.")
else :
    print("홀수입니다.")

if   num % 3 == 0 :
    print("나머지가 0입니다.")
elif num % 3 == 1 :
    print("나머지가 1입니다.")
else :
    print("나머지가 2입니다.")

score = int(input("점수입력 > "))
# 점수가 70 이상 'C', 80 이상 'B', 90 이상 'A', 60 이상 'D', 60 미만이면 'F'
# 각 학점 별 5이상은 '+'를 줌
if score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")
elif score >= 60 :
    print("D")
else :
    print("F")

if 90 <= score <= 100 :
    print("A")
elif 80 <= score < 90 :
    print("B")
elif 70 <= score < 80 :
    print("C")
elif 60 <= score < 70 :
    print("D")
else :
    print("F")


x = 10
y = 5

if x > 5: 
    if y> 3 :
        print("yes")
    else :
        print("??")
else :
    print("no")

lst_a = [273, 32, 103, "문자열", True, False]
print(lst_a)