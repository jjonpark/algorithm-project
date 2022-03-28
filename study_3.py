#백준 알고리즘 1번
    # print("Hello World!")

#백준 알고리즘 2번
    # print("강한친구 대한육군")
    # print("강한친구 대한육군")

#백준 알고리즘 3번
    # print("\    /\\")
    # print(" )  ( ')")
    # print("(  /  )")
    # print(" \(__)|")
    
#백준 알고리즘 4번
    # print("|\_/|")
    # print("|q p|   /}")
    # print('( 0 )"""\\')
    # print('|"^"`    |')
    # print("||_/=\\\\__|")

#백준 알고리즘 5번,6번,7번,8번
    # x,y=map(int,input().split())
    # print(x+y)
    # print(x-y)
    # print(x*y)
    # print(x//y)
    # print(x%y)

#백준 알고리즘 9번
    # x=input()
    # print(f"{x}??!")

#백준 알고리즘 10번
    # y=int(input())
    # print(y-543)

#백준 알고리즘 11번
    # a,b,c=map(int,input().split())
    # print((a+b)%c)
    # print(((a%c)+(b%c))%c)
    # print((a*b)%c)
    # print(((a%c)*(b%c))%c)
#백준 알고리즘 12번
    # a=int(input())
    # b=int(input())
    # c=[]
    # n=b
    # while n>=1:
    #     c.append(int(n%10))
    #     n/=10
    # result=0
    # for i in range(3):
    #     print(c[i]*a)
    #     if(i==0):
    #         result+=(c[i]*a)
    #     else:
    #         result+=(c[i]*a*10**i)
    # print(result)
#백준 알고리즘 2-1번
    # x,y =map(int,input().split())
    # if(x>y):
    #     print(">")
    # elif(x<y):
    #     print("<")
    # else:
    #     print("==")
#백준 알고리즘 2-2번
    # x=int(input())
    # if(90<=x<=100):
    #     print("A")
    # elif(80<=x<90):
    #     print("B")
    # elif(70<=x<90):
    #     print("C")
    # elif(60<=x<70):
    #     print("D")
    # else:
    #     print("F")
#백준 알고리즘 2-3번
    # x=int(input())
    # result=0
    # if(x%4==0and x%100!=0):
    #     result=1
    # elif(x%4==0and x%400==0):
    #     result=1
    # print(f"{result}")
#백준 알고리즘 2-4번
    # x=int(input())
    # y=int(input())
    # if(x<0 and y<0):
    #     print(3)
    # if(x>0 and y<0):
    #     print(4)
    # if(x>0 and y>0):
    #     print(1)
    # if(x<0 and y>0):
    #     print(2)

#백준 알고리즘 2-5번

    # x,y=map(int,input().split())
    # x_new=x
    # y_new=y
    # if(x>0):
    #     if(y-45>=0):
    #         x_new=x
    #         y_new=y-45
    #     else:
    #         x_new-=1
    #         y_new=60+(y-45)
    # else:
    #     if(y-45>=0):
    #         x_new=x
    #         y_new=y-45
    #     else:
    #         x_new=23
    #         y_new=60+(y-45)
    # print(f"{x_new} {y_new}")
#백준 알고리즘 2-6번
    # x,y=map(int,input().split())
    # m=int(input())
    # x_new=x
    # y_new=y+m
    # mx_new=x+((y+m)//60)
    # my_new=(y+m)%60
    # if(mx_new>=24):
    #     mx_new-=24

    # print(f"{mx_new} {my_new}")
#백준 알고리즘 2-7번
    # x,y,z=map(int,input().split())
    # result=0
    # if(x==y==z):
    #     result=10000+(x*1000)
    # elif(x==y):
    #     result=1000+(x*100)
    # elif(y==z):
    #     result=1000+(y*100)
    # elif(x==z):
    #     result=1000+(x*100)
    # else:
    #     result=100*max(x,y,z)
    # print(result)
#백준 알고리즘 3-1번
    # x=int(input())
    # for j in range(1,10):
    #     print(f"{x} * {j} = {x*j}")

#백준 알고리즘 3-2번
    # T=int(input())
    # for i in range(1,T+1):
    #     x,y=map(int,input().split())
    #     print(f"{x+y}")
#백준 알고리즘 3-3번
    # x=int(input())
    # result=0
    # for i in range(1,x+1):
    #     result+=i
    # print(f"{result}")
#백준 알고리즘 3-4번
    # import readline
    # import sys
    # for _ in range(int(sys.stdin.readline())):
    #     print(sum(map(int,sys.stdin.readline().split())))
#백준 알고리즘 3-5번
    # import readline
    # import sys
    # for i in range(1,int(sys.stdin.readline())+1):
    #     print(f"{i}")
#백준 알고리즘 3-6번
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # for i in range(x):
    #     print(x-i)
#백준 알고리즘 3-7번,3-8번
    # import sys
    # import readline
    # T=int(sys.stdin.readline())
    # for test_case in range(1,T+1):
    #     x,y=map(int,sys.stdin.readline().split())
    #     print(f"Case #{test_case}: {x} + {y} = {x+y}")
#백준 알고리즘 3-9번
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # for i in range(1,x+1):
    #     print(" "*(x-i),end="")
    #     print("*"*i)
#백준 알고리즘 3-10번
    # import sys
    # import readline
    # x,y=map(int,sys.stdin.readline().split())
    # z=list(sys.stdin.readline().split())

    # for i in range(x):
    #     if(int(z[i])<y):
    #         print(z[i],end=" ")
#백준 알고리즘 4-1번, 4-2번
    # import sys
    # import readline

    # while True:
    #     try:
    #         x,y=map(int, input().split())
    #         print(x+y)
    #     except EOFError:
    #         break
#백준 알고리즘 4-3번
import sys
import readline
x=int(sys.stdin.readline())
result=x
cnt=0
while(True):
    a=result//10
    b=result%10
    c=(a+b)%10
    result=(b*10)+c
    cnt+=1
    if(result==x):
        break
print(f"{cnt}")