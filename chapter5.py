#함수의 종류
# 매개변수(0), 반환값(0)
def add(a,b):
    return a + b

print(add(1,1))
# 2. 매개변수(0), 반환값(x)
print("hello, world")
# 3. 매개변수(x), 반환값(o)
def pi():
    return 3.14
pi()
radius=2
print(radius**2*pi())
# 4. 매개변수(x), 반환값(x)
def display_menu():
    print(" # 게임 메뉴 # ")
    print("1. 시작하기")
    print("2. 불러오기")
    print("3. 저장하기")

display_menu()

#변수의 종류 
x=10 #전역 변수 : 함수나 클래스 외부에서 정의된 변수 
def foo(a): #매개변수도 지역변수 입니다.
    y= 20+a #지역변수 : 함수 내부에서 정의된 변수
    return y

foo(10)
# print(y) → 오류가 실행된다. 이유? y는 매개변수이기 떄문

# 가시성
s="global"
def foo() :
    s='local'
    print(s)
foo()
print(s)
#지역변수 s를 전역변수로 해석하는 방법 
s="global"
def foo() :
    global s
    s='local'
    print(s)
foo()
print(s)

#변수를 가장 먼저 지역변수에서 찾고, 그다음 전역에서 찾고, 그다음 파이썬 내부에 심볼에서 찾음
l=[1,2,3,4]
def long(x):
    print(len(x))
long(l)

def square(x):
    return x**2
#일반 함수 : 이름이 있음, 프로그램이 종료될 떄까지 유지됨, 람다함수 : 이름이 없음, 문장의 끝을 만나면 파괴됨.
lambda x: x**2
result = square(2)
print(result)
result = (lambda x: x**2)(3)
print(result)
c=(lambda a,b : a+b)(1,1)
print(c)
# filter : 집합 전체 요소에 대하여 특정 조건이 참인 요소만 통과 시키는 함수
#filter(필터링함수, 집합) → 필터링 함수는 요소를 인자로 받고 그 값에 대하여 참 거짓을 반환하면 됩니다.
scores=[10,20,30,40,50,60,70]

def is_failed(score):
    return score <= 30
#람다 함수는 잠깐 쓰고 버리고 싶을떄 사용한다.
for score in filter(is_failed, scores):
    print(score, "failed")

for score in filter(lambda score: score <= 30, scores) :
    print(score, "failed")
# 모드 : t -> 현재 파일을 텍스트 파일로 열겠다는 의미 // r -> 읽기모드로 열겠다는 의미 
f= open("hello.txt","tr")

contents=f.read() #파일의 모든 내용을 읽어와 문자열로 반환합니다.
f.close() #파일의 사용이 끝나면 반드시 닫아 주어야 합니다.

print(contents)

#모든 행을 읽어와 리스트로 반환
f= open("hello.txt","tr")
contents=f.readlines()
f.close
print(contents)

#파일쓰기
f= open("hello.txt","tw")

for num in range(1,10):
    s=f"2X{num}={2*num}\n"
    f.write(s)
f.close()
#주의! w 모드로 파일을 열떄, 기존 파일에 대하여 쓰기를 수행하면 파일의 모든 내용이 삭제됩니다.
# a(append) : 기존 파일에 내용을 추가합니다.
# X(exclusive) : 기존 파일이 존재할 경우, 오류를 발생시킨다.
#존재하지 않는 파일에 대하여 쓰기 
f= open("world.txt","tw")

for num in range(1,10):
    s=f"2X{num}={2*num}\n"
    f.write(s)
f.close()

#모듈과 패키지
# 모듈 : 클래스나 함수 또는 변수들을 모아놓은 파일 
import math
from tracemalloc import DomainFilter # python.org

# 모듈의 요소를 모듈명 없이 사용할 수 있습니다. 
# from 모듈명 import*

print(math.pi)
print(math.factorial(5))
from math import*
print(pi)

#학생의 점수를 관리하는 학사 관리 프로그램을 생각해 봅니다.
def total(a,b,c):
    return a+b+c
def average(tot, cnt):
    return tot/cnt 

name1="daniel"
kor1=10
eng1=20
math1=30
tot1=total(kor1,eng1,math1)
avg1=average(tot1,3)
print(name1, tot1, avg1)

name2="susan"
kor2=20
eng2=30
math2=40
tot2=total(kor2,eng2,math2)
avg2=average(tot2,3)
print(name2, tot2, avg2)

#객체 안에 저장된 변수를 사용하는 방법 : .변수명

class Student :
    #클래스 안에 정의된 함수들은 반드시 첫 번쨰 매개변수를 예약석으로 남겨두어야 합니다.
    def total(student):
        return student.kor + student.eng +student.math
    def average(student):
        return(student.kor + student.eng +student.math) / student.cnt

    pass # 그냥 지나가 달라는 의미
# 클래스는 제품의 설계도 // 객체 설계도로부터 생산된 제품
daniel=Student()

daniel.name ="daniel"
daniel.kor=10
daniel.eng=20
daniel.math=30
daniel.cnt=3
tot1=daniel.total()
avg1=daniel.average()
print(daniel.name, tot1, avg1)

print("A"+"A")
print(1%2)
print(0b10*0o10+0x10-10)
age=2
++age
print(age)