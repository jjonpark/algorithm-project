#list 

l= [11,22,33,44,55,66,77,88]
print(l[1:6])
print(l[1:6:2])
print(l[0:8:]) #간격이 1이라면 이를 생략할수 있다.
print(l[0:8]) #각격이 1이라면 콜론도 생략할수 있다 
print(l[0:]) #마지막 원소가 포함된 경우, 마지막 인덱스를 생략할수 있다.
print(l[::-1]) #역순으로 출력가능 
#음수 인덱스의 경우 맨 끝은 -1 이다.
print(l[4:6])
# 리스트의 수정 끝에 추가 : append
l.append(100)
print(l)
# 임의의 위치에 삽입 : insert
l= [11,22,33,44]
l.insert(1,999)
print(l)
# 새로운 리스트를 뒤에 붙혀 확장 
l.extend([1111,2222,3333])
print(l)
# 값을 삭제 하고 싶다면 del
del l[0]
print(l)
#원하는 값을 삭제 하고 싶다면? remove
l.remove(1111)
print(l)
#추출
l= ["apple","banana","cherry","durian","apple"]
data =l.pop()
print(data,l)

data=l.pop(2)
print(data, l)

# 정렬 
l = [1,3,4,6,7,8,5,10,2,9]
# l.sort() #오름차순 정렬
# print(l)
# l.reverse()
# print(l)

#비어있는 튜플 생성
t1=tuple()
print(t1, type(t1))
t2=()
print(t2,type(t2))
#초기값을 사용한 생성
t3= tuple([1,2,3,4])
print(t3)
#튜플은 삭제나 추가 등 수정이 불가능하다.

#t=(0) 이 튜플이 되면 안되는 이유 (2+2) *2 의 출력 값이 4,4 가 됩니다.
#원소가 1개인 튜플을 생성하는 방법
t=(0,)
print(type(t),t)
#즉, 쉼표를 사용하여 원소가 여러개인 튜플을 생성할 수 있다. 
t1=1,2,3,4
print(t1)
x,y,z,q = t1
print(x,y,z,q)

#딕셔너리 생성 키와 밸류 키는 주로 문자열//밸류는 모든 형식의 데이터 값
d2={}
d1=dict()
d3={"kor":10, "eng":20, "math":30}
print(d3)
#함수를 사용하여 초기화할 경우, 변수를 생성하는 방식으로 입력해야 한다 키는 자동으로 문자열로 전환
d4=dict(kor=10, eng=20, math=30)
print(d4)
#인덱싱
print(d4["kor"])
#for 문을 사용하여 반복도 가능
for a in d4 :
    print(a)
#실행을 해보면 키가 추출 된다. 밸류를  확인해보고 싶을경우
print(d4.values())
#키-밸류 정보를 확인해보고 싶을 경우
print(d4.items())

#수정
d4["kor"]=100
#추가
d4["art"]=50
print(d4)
#삭제
del d4["eng"]
print(d4)
#추출
value=d4.pop("math")
print(value, d4)
#딕셔너리 안의 모든 항목을 삭제
d4.clear()
# 한번에 딕셔너리 안의 밸류값을 일괄적으로 업데이트 하고 싶을떄
d4.update(dict(kor=90, art=90))
print(d4)
print(d4,type(d4))
#set 은 중복을 허용하지 않는다.
#[] 리스트 {} 딕셔너리 () 튜플 // 셋은 없습니다..
s2= set([1,2,3,4])
print(s2,type(s2))

l1=[1,2,3,4,5,6,7,8,9,10]
l2=[]
for i in range(1,11) :
    l2.append(i**2)

print(l2)
#리스트 컴프리헨션 : 수식과 반복문을 사용하여 리스트를 초기화하는 문법
l=[num**2 for num in range(1,11)]
print(l)
l2=[num**2 for num in range(2,11,2)]
print(l2)
#문자열 처리 
s = "apple banana cherry durian" #이 문자열을 쪼개고 싶다. 
result = s.split(" ")
print(result) #분리된 문자열은 리스트에 저장되어 반환됩니다.
#공백이나 개행문자가 혼용되어 작성되어있을 경우 split()으로 깔끔하게 정리 가능
s="apple      banana    cherry  \n\n durian"
result1=s.split()
print(result1) 
#maxsplit 을 통해 얼만큼 쪼갤건지 작성가능
#불필요한 문자 제거 (일치하지 않는 문자가 나올때까지 실행.)
print("aaaaaaaaaaaaaaPythonaaaaaaaaaaaaa".lstrip("a"))
print("aaaaaaaaaaaaaaPythonaaaaaaaaaaaaa".rstrip("a"))
print("aaaaaaaaaaaaaaPythonaaaaaaaaaaaaa".strip("a"))
# 문자열 연결
fruit = ["apple", "banana", "cherry", "durian"]
print("".join(fruit))
print(" " .join(fruit))

#검색 find = 처음으로 일치하는 패턴의 시작 인덱스를 반황
str_f="python code"
print("찾는 문자열의 위치 : ", str_f.find("python"))
print("찾는 문자열의 위치 : ", str_f.find("code"))
print("찾는 문자열의 위치 : ", str_f.find("o"))
print("찾는 문자열의 위치 : ", str_f.find("easy"))
#특정 패턴으로 시작 또는 끝나는지를 확인 → 그 값을 논리값으로 실행
str_se="python is funny"
print("python으로 시작? ", str_se.startswith("python"))

print(str_se.replace("python", "java"))

def print_hello(count):
    for _ in range(count):
        print("hello world")

print_hello(3)

def add(a,b) :
    return a+b

print(add(3,4))
#return 은 함수 안을 끝낼때도 사용가능

def your_age(a):
    if a<1:
        print("잘못 입력하셨습니다.")
        return
    else :
        print(f"당신의 나이는 {a}입니다.")

your_age(20)
your_age(-3)
    