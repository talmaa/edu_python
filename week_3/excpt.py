'''
n = int(input("반지름 입력 > "))
print("반지름 :", n)
print("둘레 :", n * 2 * 3.14)
print("넓이 :", n ** 2 * 3.14)
'''
'''
n = input("반지름 입력 > ")
# n의 값이 정수로 바뀔수 있으면
if n.isdigit() :
    n = int(n)
    print("반지름 :", n)
    print("둘레 :", n * 2 * 3.14)
    print("넓이 :", n ** 2 * 3.14)
else :
    print("정수만 입력가능합니다.")
'''
'''
try :
    n = int(input("반지름 입력 > "))
    print("반지름 :", n)
    print("둘레 :", n * 2 * 3.14)
    print("넓이 :", n ** 2 * 3.14)
except :
    print("예외가 발생했습니다.")
'''
lst = ["52", "123", "55", "abcd", "103"]
lst2 = []
for item in lst :
    try :
        float(item)
        lst2.append(item)
    except :
        pass

print("{} 내부에 있는 숫자는 ".format(lst))
print("{} 입니다.".format(lst2))
'''
try :
    n = int(input("반지름 입력 > "))
except :
    print("예외가 발생했습니다.")
else :
    print("반지름 :", n)
    print("둘레 :", n * 2 * 3.14)
    print("넓이 :", n ** 2 * 3.14)
'''
'''
try :
    n = int(input("반지름 입력 > "))
    print("반지름 :", n)
    print("둘레 :", n * 2 * 3.14)
    print("넓이 :", n ** 2 * 3.14)
except :
    print("예외가 발생했습니다.")
else :
    print("예외가 발생하지 않았습니다.")
finally :
    print("무조건 실행되는 finally 영역")
'''

'''
try :
    f = open("info.txt", "w", encoding='utf-8')
    예외발생
    f.close()
except Exception as e:
    print(e)
print("file closed :", f.closed)
'''

try :
    f = open("info.txt", "w", encoding='utf-8')
    예외발생
except Exception as e:
    print(e)
finally :
    f.close()
print("file closed :", f.closed)

def test() :
    print("test() 함수 시작")
    try :
        print("try문 시작")
        return
        print("try문 종료")
    except :
        print("except문 시작")
    else :
        print("else문 시작")
    finally :
        # 함수가 종료되어도 실행됨
        print("finally문 시작")
    print("test() 함수 종료")

test()

i = 1
while True :
    print("while 시작")
    try :
        print("try 시작", i)
        i += 1
        if i > 3 :
            break
        print("break 뒤")
    except :
        print("except문 시작")
    finally :
        # break 이후에도 실행됨
        print("finally문 시작")