# 두정수를 입력받아 사이의 값을 구하는 코딩

    # a= int(input("정수 하나를 입력해주세요 : "))
    # b= int(input("정수 다른 하나를 입력해주세요 :"))

    # i=0
    # k=0
    # if(a>b) :
    #     i=a
    #     k=b
    # elif(a<b):
    #     i=b
    #     k=a
    # else :
    #     i= a

    # result =0
    # for j in range(k,i+1):
    #     print(j, end=",")
    #     result += j 

    # print()
    # print(result)

# n개와 w 가 있다 * 을 n 만큼 출력하나, w개 만큼 줄바꿈

    # n=int(input("몇개의 별을 출력 할까요? "))
    # w=int(input("별 몇개마다 줄바꿈 할까요? "))

    # for i in range(1,n+1) :
    #     print("*", end="")
    #     if(i%w==0):
    #         print()
    # print()

# 직사각형의 넓이를 통해 가로세로 길이를 구하는 식

    # k = int(input("직사각형의 넓이를 입력해주세요 :"))

    # for i in range(1,k+1):
    #     if i * i > k :
    #         break
    #     elif k%i :
    #         continue
    #     print(f"{i} X {k//i}")

# 직각 이등변 삼각형 출력하기 

    # k= int(input("짧은 변의 길이를 입력해주세요 : "))
    # for i in range(1,k+1):
    #     for k in range(0,i) :
    #         print("*",end="")
    #     print("")
# 오른쪽 아래가 직각 이등변 삼각형 출력하기 

    # k= int(input("이등변 삼각형 변이 길이를 입력하세요: "))

    # for i in range(1,k+1):
    #     for _ in range(0,k-i) :
    #         print(" ", end="")
    #     for _ in range(0,i) :
    #         print("*", end="")
    #     print("")
#list 개념 이해 
    # list5=list("ABC")
    # print(list5) #> 의외네..? ABC 가 출력될주 알았는데 A,B,C 가 출력되네?
#리스트를 생성하고 원소값이 홀수인 경우에 그 원소에 *2를 해하여 새 리스트를 작성
    # numbers=[1,2,3,4,5,6,7]
    # twise= [num*2 for num in numbers if num%2==1]
    # print(twise)  

#0~1000까지 소수를 나열하는 프로그램

result = []

# for i in range(2,1000):
#     num=0
#     for j in range(2,i):
#         if(i%j==0) :
#             break 
#         else :
#             num+=1
#         if(num==(i-2)):
#             print(f"{i}")
        
