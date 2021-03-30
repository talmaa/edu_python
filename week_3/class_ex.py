# class_ex.py

class FirstClass :
    def __init__(self, name) :
        self.name = name
        print("인스턴스 생성", self.name)

    def __del__(self) :
        print("인스턴스 소멸", self.name)

FirstClass("AA")

class Student :
    # 학번
    num = ""
    # 이름
    name = ""
    # 국어 점수
    korean = 0
    # 수학 점수
    math = 0
    # 영어 점수
    english = 0

    def __init__(self, num, name, korean, math, english) :
        self.num = num
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english

    def get_sum(self) :
        total = self.korean + self.math + self.english
        return total

    def get_avg(self) :
        avg = (self.korean + self.math + self.english) / 3
        return avg

h = Student("123456", "홍길동", 99, 98, 55)
print("홍길동의 시험점수 총합 :", h.get_sum())
print("홍길동의 시험점수 평균 :", h.get_avg())

j = Student("223456", "전우치", 89, 78, 65)
print("전우치의 시험점수 총합 :", j.get_sum())
print("전우치의 시험점수 평균 :", j.get_avg())

# 가로와 세로의 길이를 받아 저장하고 넓이와 둘레를 구하여 리턴하는 메소드를 가진 클래스 제작
# 클래스 명 : CalRect / 변수명 : weidth, height / 넓이 : get_area() 둘레 : get_peri()

class CalRect :
    weidth = 0
    height = 0

    def __init__(self, weidth, height) :
        self.weidth = weidth
        self.height = height

    def get_area(self) :
        return self.weidth * self.height

    def get_peri(self) :
        return (self.weidth + self.height) * 2

c = CalRect(10, 20)
print("넓이 :", c.get_area())
print("둘레 :", c.get_peri())