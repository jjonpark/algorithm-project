print("22.2.22")
# 참과 거짓을 논할떄 숫자가 아닌 문자로 표현하기 위해선 첫문자 대문자 True, False 로표현
# 참과 거짓에 대하여 단어로 표현은 되지만, 내부적으로는 여전히 1과0으로 처리 된다. 
print(True +True)
#변수명 작성시 숫자로 변수명이 시작될수 없다. // 대소문자를 구분한다. age랑Age는 다른변수이다.

age=1
print(age)
age= age+1
age+=1
print(age)

x=20 
#변수 x의 타입이 궁금하다 
print(type(x)) # int:정수 float:실수 str:문자열 bool:논리
x,y = 10,20
print(x)
print(y)
#분리자를 sep 로 표현하고 원하는값을 넣어 표기가 가능하다.
print(10, 20, 30, sep="X")
print(10, 20, 30, sep="")
print(10,20,30,sep="XXXX")

#문자 인코딩 : 문자 인코딩은 사용자가 입력한 문자나 기호들을 컴퓨터가 이용할수 있는 수로 변환하는 개념
#아스키 코드(ASCII)
print("hello \nworld")
#end(종료자) - print() 함수 사용시 함수를 종료하게 되면 자동적으로 한줄띄어쓰기를 하게됨 이부분도 조절가능
print(1, 2, end="\t")
print(3,4)

#변환함수 어떤값을 다른 형식 또는 타입의 값으로 변환하는 함수 
x=3.14
print(type(x))
x=int(x)
print(x)

x=1
print(x+x)
x="1"
print(x+x)
x=int(x)
print(x+x)
#문자를 아스키코드 값(유니코드)로 변환하는 함수 → ord
print(ord("A"))
#bool() 0이외의 모든값을 참으로 해석 (문자의 경우 공백 제외 한가지 이상의문자 입력시)
print(bool("hello"))
print(bool(""))
print(bool(" "))

name= "홍길동"
age= 20
print("이름 : {0}, 나이 : {1}".format(name,age))
print("이름 : ", name, ", 나이 : ",age ,sep="")
print("이름 : "+name+",나이 : "+str(age))
#%사용
print("이름 : %s" %name)
#출력 형식 지정
#폭을 지정하여 정렬하기 
age=10
print("0123456789")
print("{0:10}".format(age))  #오른쪽 정렬
print("{0:>10}".format(age))  #오른쪽 정렬
print("{0:<10}".format(age)) #왼쪽정렬
print("{0:^10}".format(age)) #가운데정렬

print("{0:>010}".format(age)) #빈곳에 0을 출력해주세요

x=0.123456789
print("{0:.5f}".format(x)) #소수점 6번쨰에서 반올림

money=300000000000
print("{0:,}".format(money)) #셋째 단위로 콤마를 찍어서 출력

#f-string(format string)
name="홍길동"
age=20
print(f"이름 {name}, 나이:{age}")

# name = input()
# print("이름:",name)
# print(f"너의 이름은 {name} 이군요.")

# name= "김영준"
# print("{0}은 오바이트 쟁이 입니다.".format(name))

# #Input 함수가 직접 메시지를 출력해 줍니다. 
# name = input("이름을 입력하세요 : ")
# print("이름 : ",name)

# num1=input("정수 입력 : ")
# num1=int(num1)
# num2=int(input("정수 입력 : "))
# result = num1+num2
# print(result)  

num1=float(input("반지름의 길이는 : "))
result = num1*num1*3.14
print(f"원의 넓이 :{result}")
