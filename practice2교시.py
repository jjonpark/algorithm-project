#리스트[]
subway = [10, 20, 30]
subway = ["유재석", "조세호", "박명수"]

print(subway)
print(subway.index("조세호")) 

subway.append("하하") #append 의 경우 맨 뒤에 붙히게 된다.
print(subway)

#정형돈을 유재석 / 조세호 사이에 태워보자 
subway.insert(1,"정형돈")
print(subway)

#지하철에 있는 사람을 한명씩 뒤에서 꺼냄 
print(subway.pop())
print(subway)

#유재석을 1명 더 추가하고 사람이 몇명 있는지 확인 
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능하다 
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#순서 뒤집기도 가능
num_list.reverse()
print(num_list) 

#사전 자료형 안에 값 사용하기 
cabinet = {3:"유재석", 100: "김태호"}
print(3 in cabinet)

#캐비넷 안에 신기한 변수 넣기 
cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새손님
cabinet["C-20"] = "조세호"
#간 손님
del cabinet["A-3"]
print(cabinet)
#목용탕 폐점 
cabinet.clear()
print(cabinet)

#튜플?
menu = ("돈까스", "치즈까스")
print(menu[0])

#set
my_set={1,2,3,3,3}

java = {"유재석", "김태호" , "양세형"}
python = set(["유재석", "박명수"])
#교집합
print(java& python)
print(java.intersection(python))
#합집합
print(java | python)
print(java.union(python))
#python 을 할 수 있는 사람이 늘어남
python.add("김태호")

# 당첨자 예제
from random import*
from select import kevent
from tkinter.tix import Balloon
users = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#users = range(1,21) #1 부터 20 까지의 숫자를 생성 → 타입이 range로 형성 되기 떄문에, users = list(users) 라는 코드 필요
shuffle(users)
print(users)

winners = sample(users, 4)

print("--당첨자발표--")
print("치킨 당첨자 : {0}" .format(winners[0]))
print("커피 당첨자 : {0}" .format(winners[1:3]))
print("--축하합니다--")

# weather = input("오늘 날씨는 어떄요? ")
# if weather == "비" or "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else :
#     print("오늘은 준비물 필요없어요")

# temp = int(input("기온은 어떄요? ")) #input 은 항상 str 으로 문자를 저장
# if 30 <= temp :
#     print("너무 더워요, 나가지 마세요")
# elif 10 <= temp and temp < 30 :
#     print("괜찮은 날씨에요")
# elif 0<= temp and temp <10:
#     print("외투를 챙기세요")
# else :
#     print("너무 추워요, 나가지 마세요")

# for waiting_no in[0,1,2,3,4]: #range(5) : 0,1,2,3,4
#     print("대기번호 : {0}".format(waiting_no))

#while

# custmer = "토르"
# index = 5
# while index >=1 :
#     print("{0}, 커피가 준비 되었씁니다. {1}번 남았어요." .format(custmer, index))
#     index -=1
#     if index == 0 :
#         print("커피가 폐기처분 되었습니다.")

# continue

# absent = [2,5]
# no_book = [7]
# for student in range(1,11) :
#     if student in absent :
#         continue
#     elif student in no_book :
#         print("오늘 수업은 여기까지 {0}번은 교무실로 따라와,".format(student))
#         break
#     print ("{0}번, 책을 읽어줘".format(student))

#반복문을 문장 안에서 사용해보기
# student = ["Iron man", "Thor", "i am groot"]
# student = [len(i) for i in student]
# print(student)

# count= 0 #총 탑승 승객수

# k=1

# for i in range(1,51): #1~50 이라는수
#     time = randrange(5,51) #5분 부터 50분사이
#     if 5<= time <= 15 :
#         print("[O] {0}번쨰 손님 (소요시간 : {1})".format(i, time))
#         count +=1
#     else :
#         print("[ ] {0}번쨰 손님 (소요시간 : {1})".format(i, time))   

# print ("총 탑승승객 수 : {0}".format(count))

# def open_account() :
#     print("새로운 계좌가 생성되었습니다.")
    
# def deposit(balance, money) :
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다" .format(balance+money))
#     return balance + money

# def withdraw(balance, money) :
#     if balance >= money :
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다." .format(balance-money))

# balance = 0 
# balance = deposit(balance, 1000)

#가변 인자 *
# def profile(name,age,*language) :
#     print("이름 : {0}\t, 나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "python","C","C++")
# profile("김태호", 27, "JAVA")

#퀴즈 표준 체중으 구하는 프로그램 
def std_weight(height, gender):
    k=1 
    if(gender=="남"):
        k=height*height*22
    elif(gender=="여"):
        k=height*height*21
    else :
        print("성별이 잘못입력되었습니다")
    return k

height = 175
gender = "남"
m=round(std_weight(height/100,gender),2)
print("키 {0}cm {2}자의 표준 체중은{1}kg 입니다. ".format(height,m,gender))
