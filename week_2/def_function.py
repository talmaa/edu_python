def print_3() :
    print("aa")
    print("bb")
    print("cc")

print_3()

def print_n(val, n) :
    for i in range(n) :
        print(val + str(i+1))
print("---------------------")
print_n("출력용 텍스트", 5)

def print_n2(n, *values) : 
    for i in range(n) :
        for val in values :
            print(val)
        print()

print_n2(3, "aa", "bb", "cc")
# 자료형이 달라도 입력 가능
print_n2(3, "aa", 23, False)
# 가변 매개변수 생략 가능
print_n2(3)

# 기본 매개변수를 지정하면 생략시 기본값이 적용됨
def print_n3(val, n = 2) :
    for i in range(n) :
        print(val, i+1)

print_n3("output", 3) # 지정된 문자열을 3번 출력
print_n3("output2") # 지정된 문자열을 지정된 기본값 만큼 출력

def print_n4(n = 2, *values) : 
    for i in range(n) :
        for val in values :
            print(val)
        print()

print_n4()
print("---------------------")
print_n4(3)
print("---------------------")
print_n4(4, "aa")
print("---------------------")
print_n4(4, "abc", "def", "ghij")

def print_n5(*values, n = 2) : 
    for i in range(n) :
        for val in values :
            print(val)
        print()
print("---------------------")
# 마지막 파라미터까지 가변 매개변수로 인식
print_n5("aa", "bb", "cc", 4)
# 변수 이름을 명시하면 가변 매개변수와 디폴트 파라미터를 분리할 수 있음
print_n5("aa", "bb", "cc", n = 4)

def print_sum(a, b = 10, c = 20) :
    print(a + b + c)

# 가장 일반적인 사용법
print_sum(10, 20, 30)
# 키워드로 매개변수를 지정
print_sum(10, b = 100, c = 200)
# 키워드로 매개변수의 순서를 무시하고 작업
print_sum(c = 15, a = 25, b = 10)
# 기본 매개변수를 생략하고 작업
print_sum(100, c = 50)

def return_test() :
    print("A위치")
    return
    print("B위치")

return_test()

# 두개의 숫자를 받아 서로 더한값을 리턴
def return_test2(n1, n2) :
    return n1 + n2

# 리턴 값을 변수 a에 담음
a = return_test2(10, 20)
print(a)

# 두개의 숫자를 받아 두 숫자 중 더 큰 숫자를 리턴하는 함수
def big_number(n1, n2) :
    return n1 if n1 > n2 else n2

big1 = big_number(10, 20)
big2 = big_number(40, 30)
print(big1, big2)

# 두개의 숫자를 받아 두 숫자의 차를 절대값으로 리턴하는 함수 제작
def diff_number(n1, n2) :
    return n1 - n2 if n1 - n2 > 0 else (n1 - n2) * -1

print(diff_number(30, 50))
print(diff_number(60, 20))
