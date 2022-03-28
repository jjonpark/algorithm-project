#백준 알고리즘 10-1번
    # def factorial(a:int)->int:
    #     if(a==1or a==0):
    #         return 1
    #     result=a*factorial(a-1)
    #     return result
    # x=int(input())
    # print(factorial(x))

#백준 알고리즘 10-2번 -> 시간초과
    # x=int(input())
    # while True:
    #     y=[0,1,1]
    #     for i in range(3,x+1):
    #         y.append(int(y[i-1])+int(y[i-2]))
    #     if(len(y)==x+1):
    #         print(y[x])
    #         break

#백준 알고리즘 10-2번 풀이
    # def fibonacci(n):
    #     if n<=1:
    #         return n
    #     return fibonacci(n-1) +fibonacci(n-2)
    # x=int(input())
    # print(fibonacci(x))

#백준 알고리즘 10-3번 풀이
    # def star(n:int, x:list)->list:
    #     out=[]
    #     if n==3 :
    #         return x
    #     else:
    #         for i in x:
    #             out.append(i*3)
    #         for i in x:
    #             out.append(i+' '*len(x)+i)
    #         for i in x:
    #             out.append(i*3)
    #         return star(n//3,out)
    # n=int(input())
    # first=['***', '* *', '***']
    # final= star(n,first)
    # for i in final:
    #     print(i)

#백준 알고리즘 10-4번 문제
    # def hanoi(n,a,b,c):
    #     if(n==1):
    #         print(f"{a} {c}")
    #     else:
    #         hanoi(n-1,a,c,b)
    #         print(f"{a} {c}")
    #         hanoi(n-1,b,a,c)
    # x=int(input())
    # print((2**x)-1)
    # hanoi(x,1,2,3)

#백준 알고리즘 11-1번 문제
    # import sys
    # import readline
    # x,answer=map(int,sys.stdin.readline().split())
    # x_list=list(sys.stdin.readline().split())
    # x_list_int=[None]*len(x_list)
    # for i in range(len(x_list)):
    #     x_list_int[i]=int(x_list[i])
    # x_list_int.sort()
    # def blackjack(a:list,x,y) -> int:
    #     result=0
    #     for i in range(x-2):
    #         for j in range(i+1,x-1):
    #             for k in range(i+2,x):
    #                 if(a[i]+a[j]+a[k]>y):
    #                     continue
    #                 else:
    #                     result=max(result,(a[i]+a[j]+a[k]))
    #     return result
    # result=blackjack(x_list_int,x,answer)
    # print(result)

#백준 알고리즘 11-2번 문제
    # import sys
    # import readline
    # x=int(sys.stdin.readline())

    # def new_num(x):
    #     x_list=list(str(x))
    #     result=x
    #     for i in range(len(x_list)):
    #         result+=int(x_list[i])
    #     return result
    # y=[]
    # if((x-55)<0):
    #     start=0
    # else:
    #     start=x-55
    # for i in range(start,x):
    #     if(new_num(i)==x):
    #         y.append(i)
    # if(y==[]):
    #     result=0
    # else:
    #     result=min(y)
    # print(result)

#백준 알고리즘 11-3번 문제 
    # import sys
    # import readline
    # x=int(sys.stdin.readline())

    # y=[]
    # y_num=[]
    # for i in range(x):
    #     x_list=list(sys.stdin.readline().split())
    #     y.append(x_list)
    #     y_num.append(1)
    # for j in range(x):
    #     for k in range(x):
    #         if(int(y[j][0])<int(y[k][0]) and int(y[j][1])<int(y[k][1])):
    #             y_num[j]+=1
    # for i in range(x):
    #     print(f"{y_num[i]}" , end=" ")

#백준 알고리즘 11-4번
    # N, M = map(int, input().split())
    # board = list()
    # for i in range(N):
    #     board.append(input())
    # repair = list()

    # for i in range(N-7):
    #     for j in range(M-7):
    #         first_W = 0
    #         first_B = 0
    #         for k in range(i,i+8):
    #             for l in range(j,j + 8):
    #                 if (k + l) % 2 == 0:
    #                     if board[k][l] != 'W':
    #                         first_W = first_W+1
    #                     if board[k][l] != 'B':
    #                         first_B = first_B + 1
    #                 else:
    #                     if board[k][l] != 'B':
    #                         first_W = first_W+1
    #                     if board[k][l] != 'W':
    #                         first_B = first_B + 1
    #         repair.append(first_W)
    #         repair.append(first_B)
    # print(min(repair))
#백준 알고리즘 11-5번 -> 시간 초과
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # def continu_num(x:int):
    #     x_str=str(x)
    #     x_str_list=list(x_str)
    #     result=False
    #     for i in range(len(x_str_list)-2):
    #         if(int(x_str_list[i])==int(x_str_list[i+1])==int(x_str_list[i+2])==6):
    #             result= True
    #             break
    #         else:
    #             continue
    #     return result
    # y=[]
    # for i in range(1,5999667):
    #     if(continu_num(i)==True):
    #         y.append(i)
    # y.sort()
    # print(y[x-1])  
#백준 알고리즘 11-5번 풀이 
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # num=666
    # cnt=0
    # while True:
    #     if '666' in str(num):
    #         cnt+=1 
    #     if(cnt==x):
    #         print(num)
    #         break
    #     num +=1

#나코딩 강의 
    # import sys
    # import readline
    # n,k=map(int,sys.stdin.readline().split())
    # a_list=list(sys.stdin.readline().split())
    # b_list=list(sys.stdin.readline().split())
    # a_list_int=[None]*n
    # b_list_int=[None]*n
    # for i in range(n):
    #     a_list_int[i]=int(a_list[i])
    #     b_list_int[i]=int(b_list[i])
    # a_list_int.sort()
    # b_list_int.sort(reverse=True)
    # result=0
    # for j in range(k):
    #     if(a_list_int[j]<b_list_int[j]):
    #         a_list_int[j],b_list_int[j]=b_list_int[j],a_list_int[j]
    # for k in range(n):
    #     result+=a_list_int[k]
    # print(result)

#백준 알고리즘 12-1번,12-2번
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=[]
    # for i in range(x):
    #     k=int(sys.stdin.readline())
    #     y.append(k)
    # y.sort()
    # for i in range(x):
    #     print(y[i])

#백준 알고리즘 12-3번
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # count=[0]*10001
    # for i in range(x):
    #     count[int(sys.stdin.readline())]+=1
    # for i in range(len(count)):
    #     for j in range(count[i]):
    #         print(i)

#백준 알고리즘 12-4번
    # import sys
    # import readline
    # from collections import Counter
    # x=int(sys.stdin.readline())
    # y=[]
    # result=0
    # for i in range(x):
    #     y.append(int(sys.stdin.readline()))
    #     result+=y[i]
    # mid_1=result/x
    # y_clean=y.copy()
    # y_clean.sort()
    # mid_2=y_clean[(x-1)//2]
    # count=Counter(y_clean).most_common() #[(1,3),(2,3)] 이런식으로 담기게 된다. 많은것부터
    # if(-0.5<mid_1<0):
    #     print(0)
    # else:
    #     print(f"{mid_1:.0f}")
    # print(mid_2)
    # if(len(count)>1):
    #     if count[1][1]==count[0][1]:
    #         print(count[1][0])
    #     else:
    #         print(count[0][0])
    # else:
    #     print(count[0][0])
    # print(max(y)-min(y))

#백준 알고리즘 12-5번
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # x_list=list(str(x))
    # x_int_list=[None]*len(x_list)
    # for i in range(len(x_list)):
    #     x_int_list[i]=int(x_list[i])
    # x_int_list.sort(reverse=True)
    # for j in range(len(x_int_list)):
    #     print(x_int_list[j],end="") 

#백준 알고리즘 12-6번-> 틀림 이론공부 필요 sorted(), sort()
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=[]
    # for i in range(x):
    #     k_1,k_2=map(int,sys.stdin.readline().split())
    #     k_list=[k_1,k_2]
    #     y.append(k_list)
    # y=sorted(y,key=lambda x : (x[0],x[1]))
    # for j in range(x):
    # print(y[j])

#백준 알고리즘 12-6번 풀이 
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=[]
    # for i in range(x):
    #     k_1,k_2=map(int,sys.stdin.readline().split())
    #     k_list=[k_1,k_2]
    #     y.append(k_list)
    # y=sorted(y,key=lambda x : (x[0],x[1]))
    # for j in range(x):
    #     print(f"{y[j][0]} {y[j][1]}")

#백준 알고리즘 12-7번 풀이 
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=[]
    # for i in range(x):
    #     k_1,k_2=map(int,sys.stdin.readline().split())
    #     k_list=[k_1,k_2]
    #     y.append(k_list)
    # y=sorted(y,key= lambda x : (x[1],x[0]))
    # for j in range(x):
    #     print(f"{y[j][0]} {y[j][1]}")

#백준 알고리즘 12-8번 
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=[]
    # for i in range(x):
    #     k=str(sys.stdin.readline().strip())
    #     y.append(k)
    # y=list(set(y))
    # y.sort()
    # y=sorted(y,key= len)
    # for j in range(len(y)):
    #     print(y[j])

#백준 알고리즘 12-9번
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=[]
    # for i in range(x):
    #     k_1,k_2=map(str,sys.stdin.readline().strip().split())
    #     k_1=int(k_1)
    #     y.append((k_1,k_2))
    # y=sorted(y,key= lambda x: x[0])
    # for j in range(len(y)):
    #     print(f"{y[j][0]} {y[j][1]}")

#백준 알고리즘 12-10번 -> 시간 초과
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y_list=list(sys.stdin.readline().split())
    # y_list_int=[None]*x
    # for i in range(len(y_list)):
    #     y_list_int[i]=int(y_list[i])
    # y_rank=[0]*x
    # for i in range(x):
    #     for j in range(x):
    #         if(y_list_int[i]>y_list_int[j]):
    #             y_rank[i]+=1
    # for k in range(x):
    #     print(y_rank[k],end=" ")

#백준 알고리즘 12-10번 풀이 
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # arr= list(map(int,sys.stdin.readline().split()))
    # arr2 = sorted(list(set(arr)))
    # dic={arr2[i] : i for i in range(len(arr2))}
    # for i in arr:
    #     print(dic[i],end=' ')