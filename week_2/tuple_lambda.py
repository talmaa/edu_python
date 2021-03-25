# tuple_lambda.py

# 튜플 생성
t1 = (1, 2, 'a', 'b')

print(t1[0])
print(t1[1])
print(t1[2])
print(t1[3])
print(t1)

# t1[0] = 100
# TypeError: 'tuple' object does not support item assignment

print(t1[0:2])
print(t1[2:])
print(t1[:2])

t2 = (7, 8, 'z')
t3 = t1 + t2
print(t3)

print(t2 * 3)

# 값이 하나인 튜플은 반드시 ',' 로 끝나야 함
t4 = ('a',)
print(t4)
#('a',)

t5 = 10, 20, 30
print("t5 :", type(t5))

# 우측의 리스트 값들을 좌측의 변수에 대입
[a, b] = [10, 20]
# 우측의 튜플 값들을 좌측의 변수에 대입
(c, d) = (30, 40)
# 괄호가 생략된 튜플
e, f = 50, 60
print("a :", a)
print("b :", b)
print("c :", c)
print("d :", d)
print("e :", e)
print("f :", f)
# e, f 값의 스위칭
e, f = f, e
print("e :", e)
print("f :", f)

def test() :
    # 괄호 없는 튜플로 값을 리턴
    return 10, 20

a, b = test()
print(a, b)

# 2 ~ 50 사이의 소수 구하기
def is_prime(i) :
    for j in range (2, i) :
        if i % j == 0 :
            return False

    return True

for i in range(2, 51) :
    if is_prime(i) : 
        print(i, "는 소수입니다.")

print("--------------------")
def is_prime2(s, e) :
    for i in range(s, e + 1) :
        if(i == 1) :
            continue
        flag = True
        for j in range(2, i) :
            if(i % j == 0) :
                flag = False
        
        if flag :
            print(i, "는 소수입니다.")

is_prime2(2, 50)

# 정수를 하나 받아 홀짝 계산

def is_even(num) :
    return num % 2 == 0

for i in range(5) :
    if is_even :
        print(i, "는 짝수")
    else :
        print(i, "는 홀수")