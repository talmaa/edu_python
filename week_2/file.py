#file = open("test.txt", "w")
# 현 파일과 같은 위치에 있는 'test.txt'파일을 쓰기 모드로 열라는 명령(없으면 생성)
#file.write("새로 입력하는 글입니다.")
#file.close()

file = open("test.txt", "a", encoding='utf-8')
# 현 파일과 같은 위치에 있는 'test.txt'파일을 이어 쓰기 모드로 열라는 명령(없으면 생성)
file.write("\n두번째 줄 입니다.")
file.close()

# 현 위치에 'new.txt'파일을 만들고 안에 글을 입력
# 글은 총 10줄로 "1번째 줄입니다." ~ "10번째 줄입니다." 까지 입력
f = open("new.txt", "w", encoding='utf-8')
for i in range(1, 11) :
    line = str(i) + "번째 줄입니다.\n"
    f.write(line)
f.close()

f = open("new.txt", "r", encoding='utf-8')
line = f.readline() # f객체의 파일에서 첫번째 줄을 읽어 들임
print(line)
line = f.readline() # f객체의 파일에서 두번째 줄을 읽어 들임
print(line)
f.close()

f = open("new.txt", "r", encoding='utf-8')
print("readline() 함수 이용")
while True :
    line = f.readline() # f객체에서 한 줄을 읽어들임
    if not line : # 마지막 줄이 지났으면
        break # 무한루프 빠져나옴
    print(line)
f.close()

f = open("new.txt", "r", encoding='utf-8')
print("readlines() 함수 이용")
lines = f.readlines() # f객체의 내용을 한 줄에 한 요소씩 리스트로 저장
for line in lines :
    print(line)
f.close()

f = open("new.txt", "r", encoding='utf-8')
print("read() 함수 이용")
data = f.read() # f객체의 내용을 모두 data에 담음
print(data)
f.close()

with open("new.txt", "r", encoding='utf-8') as f :
    print(f.readline())
# with문이 끝나는 순간 자동을 f객체는 close()됨

f = open("xl.csv","w", encoding='utf-8')
f.write("이름,나이\n")
f.write("홍길동,35\n")
f.write("전우치,33\n")
f.write("합계,=b2+b3\n")
f.close()