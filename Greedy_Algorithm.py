#그리디 알고리즘 공부
#백준 알고리즘 - 동전 
    # import sys
    # import readline
    # n,m=map(int,sys.stdin.readline().split())
    # y=[]
    # for i in range(n):
    #     y.append(int(sys.stdin.readline()))
    # y.sort(reverse=True)
    # result=0
    # for j in range(n):
    #     if m==0:
    #         break
    #     if(m>=y[j]):
    #         result+=(m//y[j])
    #         m-=((m//y[j])*y[j])
    # print(result)

#백준 알고리즘 -문제풀이 회의실
    # N = int(input())
    # time = []

    # for _ in range(N):
    # start, end = map(int, input().split())
    # time.append([start, end])
    # time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
    # time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순
    # last = 0 # 회의의 마지막 시간을 저장할 변수
    # conut = 0 # 회의 개수를 저장할 변수
    # for i, j in time:
    # if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    #     conut += 1
    #     last = j

    # print(conut)

#백준 알고리즘 - ATM
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=list(map(int,sys.stdin.readline().strip().split()))
    # y.sort()
    # answer=[y[0],]
    # result=y[0]
    # for i in range(1,len(y)):
    #     answer.append(y[i]+answer[i-1])
    #     result+=answer[i]
    # print(result)

#백준 알고리즘 - 잃어버린 괄호
    # x=input().split('-')
    # num=[]
    # for i in x:
    #     cnt=0
    #     s=i.split('+')
    #     for j in s:
    #         cnt+=int(j)
    #     num.append(cnt)
    # result=num[0]
    # for i in range(1,len(x)):
    #     result-=num[i]
    # print(result)

#백준 알고리즘 - 주유소 ->17점?
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # km=list(map(int,sys.stdin.readline().strip().split()))
    # won=list(map(int,sys.stdin.readline().strip().split()))
    # del won[len(km)]
    # won_min=min(won)
    # result=0
    # def remain_km(x:list, a:int):
    #     num=0
    #     for i in range(a,len(x)):
    #         num+=x[i]
    #     return num
    # for i in range(len(won)):
    #     if(won[i]==won_min):
    #         k=remain_km(km,i)
    #         result+=(k*won[i])
    #         break
    #     else:
    #         result+=(won[i]*km[i])
    # print(result)

#백준 알고리즘 주유소 풀이
    # N = int(input())
    # roads = list(map(int, input().split()))
    # cities = list(map(int, input().split()))

    # minVal = cities[0]
    # sum = 0
    # for i in range(N-1):
    #     if minVal > cities[i]:
    #         minVal = cities[i]
    #     sum += (minVal * roads[i])
        
    # print(sum)

#백준 알고리즘 문제 보물
    # x=int(input())
    # y_1=list(map(int,input().split()))
    # y_2=list(map(int,input().split()))
    # y_1.sort()
    # y_2.sort(reverse=True)
    # result=0
    # for i in range(x):
    #     result+=(y_1[i]*y_2[i])

    # print(result)

#백준 알고리즘 문제 - 거스름돈
    # import sys
    # import readline
    # def cnt_remain(x:int):
    #     k=1000-x
    #     result=0
    #     if(k>=500):
    #         result+=(k//500)
    #         k=int(k%500)
    #     if(k>=100):
    #         result+=(k//100)
    #         k=int(k%100)
    #     if(k>=50):
    #         result+=(k//50)
    #         k=int(k%50)
    #     if(k>=10):
    #         result+=(k//10)
    #         k=int(k%10)
    #     if(k>=5):
    #         result+=(k//5)
    #         k=int(k%5)
    #     if(k>=1):
    #         result+=(k//1)
    #         k=int(k%1)
    #     return result
    # x=int(sys.stdin.readline())
    # answer=cnt_remain(x)
    # print(answer)

#백준 알고리즘 - 로프
import sys
import readline
x=int(sys.stdin.readline())
y=[]
result=0
ans=0
for i in range(x):
    y.append(int(sys.stdin.readline()))
y.sort()
for i in range(x):
    result=y[i]*(x-i)
    if(ans<=result):
        ans=result
print(ans)
#백준 알고리즘 - 전자레인지
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # result=0
    # k_1=0
    # k_2=0
    # k_3=0
    # if((x%10)!=0):
    #     result=-1
    # else:
    #     if(x>=300):
    #         k_1=(x//300)
    #         x=int(x%300)
    #     if(x>=60):
    #         k_2=(x//60)
    #         x=int(x%60)
    #     if(x>=10):
    #         k_3=(x//10)
    # if(result==-1):
    #     print(-1)
    # else:
    #     print(f"{k_1} {k_2} {k_3}")

#백준 알고리즘 - 수들의 합
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # num=0
    # result=0
    # for i in range(1,x):
    #     num=(i*(i+1))
    #     if(num>(2*x)):
    #         result=i
    #         break
    # if(x<=2):
    #     print(1)
    # elif(x==3):
    #     print(2)
    # else:
    #     print(result-1)

#<삼성 SW expert> -암호생성기
    # T=10
    # for test_case in range(1,T+1):
    #     x=int(input())
    #     y=list(map(int,input().split()))
    #     i=1
    #     while True:
    #         if(i>5):
    #             i=1
    #         y[0]-=i
    #         y.append(y[0])
    #         if(y[0]<=0):
    #             y[-1]=0
    #             del y[0]
    #             break
    #         del y[0]
    #         i+=1
    #     print(f"#{test_case}",end=" ")
    #     for i in range(len(y)):
    #         print(y[i],end=" ")