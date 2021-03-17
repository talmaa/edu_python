#string.py
print("'안녕하세요' 라고 말했습니다.")
print('"안녕하세요" 라고 말했습니다.')
print("\"안녕하세요\" 라고 말했습니다.")

print("이름\t나이\t지역")
print("홍길동\t35\t울릉도")
print("전우치\t30\t함경도")

print("동해물과 백두산이 마르고 닳도록\n하느님이 보우하사 우리 나라만세\n")

print("""\
동해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리 나라만세\
""")

print("abc" + "def" + "  " + "zzz")
print("test" * 3)

print("abcd efg"[3])
print("abcd efg"[-1])
print("abcd efg"[4])

print("abcd efg"[1:6])
print("abcd efg"[6:1])
print("abcd efg"[3:-1])

birth = "19880515"
print(birth[:4] + "년 " + birth[4:6] + "월 " + birth[6:] + "일 생") # 1988년 05월 15일 생

print(len("abcd efg"))