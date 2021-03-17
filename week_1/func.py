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