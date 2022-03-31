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
N = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

minVal = cities[0]
sum = 0
for i in range(N-1):
    if minVal > cities[i]:
        minVal = cities[i]
    sum += (minVal * roads[i])
    
print(sum)
