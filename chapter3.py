#if 문

# num=int(input("정수 입력 : "))

# if num==0 :
#     print("0입니다.")
# else :
#     print("0이 아닙니다")

#비교연산자는 산술 연산자보다 우선 순위가 낮다.
# num=int(input("자연수 입력 :"))

# if (num%2)==0 :
#     print("짝수 입니다.")
# else :
#     print("홀수 입니다.")

#연습문제 
# age=int(input("나이를 입력해주세요 : "))

# if age<=0 :
#     print("나이를 다시 입력해주세요")
# elif age>=151 :
#     print("나이를 다시 입력해주세요")
# else :
#     print(f"당신의 나이는 {age}입니다.")

#중복을 방지 하기 위해 (age<1) or (age> 150) → comparison chaining

# if 1<= age <=150 :
#     print(f"당신의 나이는 {age}입니다.")
# else :
#     print("잘못 입력하셨습니다.")

#자료구조 : 리스트, 튜플, 딕셔너리, 셋
#리스트 : 추가된 순서가 유지되고 중복을 허용하는 자료
#생성 방법 : 변수명 = [값1,값2, ...]
l=[1,2,3,4]
m=[1,1,1,1]
print(l)
print(m)

for i in [1,2,3,4,5] :
    print(i,"hello world")

#range(start, stop, step) : 정수 집합을 생성하는 함수, 시작값, 끝값, 간격 //끝값은 포함되지 않는다.
# for i in range(1,10,1) :
#     print(i,end = " ")
#현실과 다르게 컴퓨터 공학에서는 보통 시작을 0으로 한다.
#간격이 생략되어있고, 시작값이 0이라면 이를 생략할수 있다.
print()

for cnt in range(3) :
    print(cnt, "hello world")

#연습문제  사용자로부터 구구단의 단 수를 입력 받아 해당 단을 출력하는 프로그램
# num2 = int(input("원하는 구구단의 단수는..? : "))

# for i in range(9):
#     result= num2*(i+1)
#     print(f"{num2}X{i+1} ={result}")

#연습문제 
print()
# 0 → 0 1 2 3
# 1 → 0 1 2 3
# 2 → 0 1 2 3
for i in range(2,10) :
    print(f"< {i}단 >")
    for k in range(1,10) :
        result = i*k
        print(f"{i} X {k} ={result}")
    print()

#while 문
#반복을 제어 하기 위한 2가지 1. break 2. continue
cnt =0 
while True :
    if cnt >3:
        break
    print(f"{cnt} hello, world")
    cnt +=1

for num in range(1,11):
    if (num %2) != 0 :
        continue
    print(num, end = " ")

# 반복의 횟수가 명확하게 정해진 경우 → for 문// 반복희 횟수가 정확하지 않을떄 → while문

from operator import truediv
from random import*
import random
print()

num2= random.randint(1,10)
# k=0

# while True :
#     num3=int(input(" 숫자를 맞춰보세요~ : ")) 
#     if(num3 < num2) :
#         print("정답은 입력 하신 숫자보다 커요~")
#         k+=1
#     elif(num3 >num2):
#         print("정답은 입력 하신 숫자보다 작아요~")
#         k+=1
#     else :
#         print(f"정답 입니다. {k+1}번 만에 맞추셨네요.")
#         break

for i in range(1,6) :
    for k in range(i):
        print("*", end=" ")
    print()

