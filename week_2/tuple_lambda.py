# tuple_lamda.py

t1 = (1, 2, 'a', 'b') # 튜플 생성
print(t1[0])
print(t1[1])
print(t1[2])
print(t1[3])

# t1[0] = 100 # 튜플은 내용 변경이 불가
# del t1[0] # 튜플은 내용 삭제 불가

print(t1[0:2])  # (1, 2)
print(t1[2:])   # ('a', 'b')
print(t1[:2])   # (1, 2)

t2 = (7, 8, 'z')
t3 = t1 + t2
print(t3) # (1, 2, 'a', 'b', 7, 8, 'z')
print(t2 * 3) # (7, 8, 'z', 7, 8, 'z', 7, 8, 'z')

t4 = ('a',) # 값이 하나인 튜플은 반드시 값 뒤에 쉼표로 끝나야 함
print(t4) # ('a',)

t5 = 10, 20, 30
print("t5 : ", t5) # t5 :  (10, 20, 30)
print("type(t5) : ", type(t5)) # type(t5) :  <class 'tuple'>

[a, b] = [10, 20] # 우측의 리스트 값들을 좌측의 변수들에 대입
(c, d) = (30, 40) # 우측의 튜플 값들을 좌측의 변수들에 대입
e, f = 50, 60 # 괄호가 생략된 튜플로 변수에 값들을 대입
print("a : ", a) # a :  10
print("b : ", b) # b :  20
print("c : ", c) # c :  30
print("d : ", d) # d :  40
print("e : ", e) # e :  50
print("f : ", f) # f :  60
e, f = f, e # e와 f변수의 값을 서로 변경
print("e : ", e) # e :  60
print("f : ", f) # f :  50

def test() :
    return (10, 20) # 튜플로 두 개의 값을 리턴
a, b = test() # 함수의 리턴값을 두 개의 변수에 담음
print("a :", a) # a : 10
print("b :", b) # b : 20

def test2() :
    return 30, 40, 50 # 괄호없는 튜플로 값을 리턴(튜플만 가능)
c = test2() # 하나의 변수로 받으면 튜플로 받음
print("c :", c) # c : (30, 40, 50)

d, e, f = test2() # 변수의 개수와 리턴값의 개수가 맞으면 각각에 들어감
print("d :", d) # d : 30
print("e :", e) # d : 40
print("f :", f) # d : 50


# 2 ~ 50 사이의 소수 구하기
def is_prime(num) :
    for i in range(2, num) :
        if num % i == 0 :
            return False
    return True
# 맞는지 여부를 검사하는 함수일 경우에는 대체적으로 틀렸는지 부터 검사해야 함
# 루프문 안에서 if문을 사용할 경우 else절이 사용되면 정말 필요한 기능인지 검토해봐야 함
#   루프문 안의 if문에서 return을 할 경우에는 else절은 사용하면 안됨

for i in range(2, 51) :
    if is_prime(i) :
        print(i)

def is_prime2(num) :
    for i in range(2, num / 2) :
        if num % i == 0 :
            return False
    return True

# 정수를 하나 받아 짝수인지 여부를 리턴하는 is_even() 함수를 작업
def is_even(num) :
    if num % 2 == 0 :
        return True
    else :
        return False


for i in range(5) :
    if is_even(i) :
        print(i, "는 짝수")
    else :
        print(i, "는 홀수")


def test(func) :
    for i in range(3) :
        func()

def print_str() :
    print("str")

test(print_str) # 함수를 매개변수로 보냄

def power(item) :
    return item * item

def under3(item) :
    return item < 3

lst = [1, 2, 3, 4]
result = map(power, lst)
print(result) # <map object at 0x0000023EDF5CE340>
print(list(result)) # [1, 4, 9, 16]

result2 = filter(under3, lst)
print(result2) # <filter object at 0x0000014164C8E310>
print(list(result2)) # [1, 2]

power2 = lambda x : x * x
under32 = lambda x : x < 3
result = map(power2, lst)
print(result) # <map object at 0x000001DC15D3E340>
print(list(result)) # [1, 4, 9, 16]

result2 = filter(under32, lst)
print(result2) # <filter object at 0x000001DC15D3E2B0>
print(list(result2)) # [1, 2]

lst2 = [2, 2, 2, 2]
multiply = lambda x, y : x * y
result = map(multiply, lst, lst2)
print(list(result)) # [2, 4, 6, 8]

result = map(lambda x : x * x, lst)
print(list(result)) # [1, 4, 9, 16]