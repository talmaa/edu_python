from math import *

# math.ceil(1.3)
print(ceil(1.3))

import random as r

print(r.random())
print(r.uniform(10, 15))
print(r.randrange(10))
print(r.randrange(10, 15))
print(r.choice([1, 2, 3, 4, 5]))
print(r.sample([1, 2, 3, 4, 5], k = 2))
lst = [1, 2, 3, 4, 5]
print(r.shuffle(lst))
print(lst)

# 1~45 사이의 정수 6개를 중복되지 않게 출력

lst = []
i = 0
while i < 6 :
    flag = True
    v = r.randrange(1, 46)
    for item in lst :
        if v == item :
            flag = False
    if flag :
        lst.append(v)
        i += 1

lst.sort()
print(lst)

# 1~45 사이의 정수 6개를 중복되지 않게 출력 set 사용
s1 = set()
while len(s1) != 6 :
    s1.add(r.randrange(1, 46))
l1 = list(s1)
l1.sort()
print(l1)

import datetime as d

now = d.datetime.now()
print(now)

after = now + d.timedelta(days=5)
print(after)

before = now - d.timedelta(weeks=2)
print(before)

re1 = now.replace(year = 2022)
print(re1)

# now의 날짜에서 1년 후의 날짜를 출력
re2 = now.replace(year = now.year + 1)
print(re2)

import time
print("지금부터 5초간 멈춤")
time.sleep(5)
print("다시 시작")

import urllib.request as req

target = req.urlopen("http://www.naver.com/")
output = target.read()
#print(output)

