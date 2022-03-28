print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? ture")
 
animal= "강아지"
name = "연탄이"
age = 4

print("우리집 "  + animal+  " 의 이름은 " + name + "에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? ture")
 
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")

print(2**3) #2의 3승
print(4>= 7) #false
print(1 != 3)
print((3>0) or (3<5)) #true

print((2+3)*4)
number = 14
number += 2
number *=2 
print(number)  
# % 는 나머지를 구하는 수식 
# abs는 절대값 
# pow (4,2) 은 4의 2승
# max (a,b,c) 는 a,b, c 중 가장 큰 값
# round(3.14) 는 반올림 하는 함수

from math import* # 파이썬에서 제공하는 숫자 변수들을 사용하겠다 라는 뜻
from random import*

print(random()) #0.0~1.0 미만의 임의의 값을 생성
print(int(random()*10)) #int 로 감싸게 될 경우 정수 값만 반환
print(int(random()*10))
print(int(random()*10))

print(randrange(1,46)) #1~46미만의 임의의 값 생성
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
# randint 양끝의 숫자를 포함

num = randint(4,28) 
print("오프라인 스터디 모임 날짜는 매월" +str(num)+ "일로 선정되었습니다")

sentence = '나는 소년입니다'
sentence2 = "파이썬은 쉬워요"
print(sentence)
print(sentence2)
sentence3 = """"""
print(sentence3)
jumin= "950404-1234567"
print("성별 : " + jumin[7]) #문자를 카운팅 할떄 첫번쨰는 0 부터 시작한다.
print("연 : " +jumin[0:2]) #0:2 라고 적으면 0부터 2직전까지의 값을 가져온다.
print("월: " +jumin[2:4]) 
print("생년월일 : " +jumin[ :6])
print("뒤 7자리 : " +jumin[7:]) 

python = 'python is Amazing'
print(python.lower()) #pyhon 의 문자열을 모두 소문자로 반환
print(len(python)) #python의 길이를 출력
print(python.replace("python" , "java"))
index = python.index("n") # n이 몇번쨰 포함이 되어있는지 반환

print("나는 %d살 입니다." % 20)
print("나는 %s을 좋아해요" %"파이썬") #s 는 문자 퍼센트 뒤에 있는 문자를 출력
print("나는 {}살 입니다." .format(20))

age = 20 
color = "빨간"
print(f"나는{age}살이며, {color}색을 좋아해요")

#\n :줄바꿈
print("백문이 불여일견\n백견이 불여일타")
print("저는 \"나도코딩\" 입니다") # "" 를 문장내에서 나오게 하는 방법 : \
#\r 커서를 맨 앞으로 이동후 재작성
print("Red APPLE\rPine")

url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")] 
print(my_str)
password = my_str[:3] + str(len(my_str)) +str(my_str.count("e")) +"!"
print("{0} 의 비밀번호는 {1} 입니다." .format(url,password))
