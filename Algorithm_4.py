#백준 문제 <수 찾기> ->이분탐색은 재귀가 아니네..?
    # N=int(input())
    # array=list(map(int,input().split()))
    # array.sort()
    # def check(K,start,end):
    #     mid=int((start+end)/2)
    #     ans=0
    #     if(array[mid]==K):
    #         ans=1
    #         return
    #     if(K>array[mid]):
    #         check(K,mid+1,end)
    #     elif(K<array[mid]):
    #         check(K,start,mid-1)
    #     return ans

    # M=int(input())
    # check_list=list(map(int,input().split()))
    # for i in range(M):
    #     print(check(check_list[i],0,N-1))

#백준 문제 < 수찾기 >
    # N=int(input())
    # a=list(map(int,input().split()))
    # a.sort()

    # def binartSearch(target):
    #     start=0
    #     end=N-1
    #     while start<=end:
    #         mid=(start+end)//2
    #         if a[mid]==target:
    #             print(1)
    #             return
    #         elif a[mid]<=target:
    #             start=mid+1
    #         else:
    #             end=mid-1
    #     print(0)
    #     return
    # M=int(input())
    # check_list=list(map(int,input().split()))
    # for i in range(M):
    #     binartSearch(check_list[i])

#백준 문제 < 랜선 자르기 > -> 이게 이분탐색 문제??? 많은 문제를 풀어보자 
    # k,n=map(int,input().split())
    # lanson =[]
    # for i in range(k):
    #     lanson.append(int(input()))
    # start, end = 0, 100000000000
    # answer=0
    # while start<=end:
    #     mid=(start+end)//2
    #     num=0
    #     for len in lanson:
    #         num +=len//mid
    #     if num >=n:
    #         start=mid+1
    #         if mid>answer:
    #             answer=mid
    #     else:
    #         end=mid-1
    # print(answer)

#백준 문제 < 개똥벌레 > -> 정렬을 생각하기 어렵고, 구현이 힘들었다.
    # N,H=map(int(input().split()))
    # a_list=[]
    # b_list=[]
    # for i in range(N):
    #     k=int(input())
    #     if((i%2)==0):
    #         a_list.append(k)
    #     else:
    #         b_list.append(k)
    # a_list.sort()
    # b_list.sort()

#백준 문제 < 개똥 벌레 >  풀이 
    # def lower_bound(s,e,d,l):
    #     while (e-s>0):
    #         m=(s+e)//2
    #         if(l[m]<d):
    #             s=m+1
    #         else:
    #             e=m
    #     return e
    # up=[]
    # down=[]
    # result=[0]*500001
    # n,h=map(int,input().split())
    # for i in range(n):
    #     obstacle=int(input())
    #     if i%2==1:
    #         up.append(obstacle)
    #     else:
    #         down.append(obstacle)

    # up.sort()
    # down.sort()
    # answer=0
    # mx=2147483647
    # for i in range(1,h+1):
    #     idxd=lower_bound(0,len(down),i,down)
    #     idxu=lower_bound(0,len(up),h-i+1,up)
    #     result[i]=n//2-idxd+n//2-idxu
    #     mx=min(mx,result[i])
    # for i in range(1,h+1):
    #     if result[i]==mx:
    #         answer+=1
    # print(mx,answer)


#백준 문제 <수 정렬하기>
    # M=int(input())
    # array=[]
    # for i in range(M):
    #     k=int(input())
    #     array.append(k)
    # array.sort()
    # for i in range(M):
    #     print(array[i])

#백준 문제 <저울> -> 저번에 시험본 그 유형이랑 좀 비슷한거 같다. 풀이를 보고 빠져보자
    # import itertools
    # N=int(input())
    # array=list(map(int,input().split()))
    # array.sort()
    # print(array)
    # array=[1,2,3]
    # combi=list(itertools.combinations(array,2))
    # print(combi)

#백준 문제 < 저울 > 풀이 -> 특이한..방법이네?
    # N=int(input())
    # array=list(map(int,input().split()))
    # array.sort()
    # answer=1
    # for i in range(N):
    #     if answer>=array[i]:
    #         answer+=array[i]
    #     else: 
    #         break
    # print(answer)

#백준 문제 < 계수 정렬 > 
    # import sys
    # n=int(input())
    # count_sort=[0]*10001
    # for i in range(n):
    #     count_sort[int(sys.stdin.readline())]+=1
    # for i in range(10001):
    #     if count_sort[i]!=0:
    #         for _ in range(count_sort[i]):
    #             print(i)

#백준 문제 < 나이순 정렬 >
    # N=int(input())
    # array=[]
    # for i in range(N):
    #     k_1,k_2=input().split()
    #     k_1=int(k_1)
    #     array.append([k_1,k_2])

    # answer=sorted(array,key=lambda x:x[0])

    # for i in range(N):
    #     print(f"{answer[i][0]} {answer[i][1]}")

#백준 문제 <숫자의 합>
    # n=int(input())

    # x=list(str(input()))
    # answer=0
    # for i in range(n):
    #     answer+=(ord(x[i])-48)    
    # print(answer)

#백준 문제 < 백대열 >
    # a,b=map(int,input().split(':'))

    # def GCD(a,b):
    #     if b%a:
    #         return GCD(b%a,a)
    #     else:
    #         return a

    # k=GCD(a,b)
    # a_1=a//k
    # b_1=b//k
    # print(f"{a_1}:{b_1}")

#백준 문제 < 문자열 폭발 > ->하나씩 보면서 스택의 개념으로 지워주는
    # s=str(input())
    # bomb=str(input())
    # left=[]
    # start=0
    # end=len(s)-1
    # while start<=end:
    #     tof=True
    #     left.append(s[start])
    #     start+=1
    #     if(len(left)>=len(bomb)):
    #         for i in range(len(bomb)):
    #             if bomb[i]!=left[len(left)-len(bomb)+i]:
    #                 tof=False
    #                 break
    #         if tof==True:
    #             for i in range(len(bomb)):
    #                 left.pop()
    # if len(left)==0:
    #     print("FRULA")
    # else:
    #     for i in range(len(left)):
    #         print(left[i], end='')

#백준 문제 <포도주 시식> ->이게 왜 런타임 오류지..?
    # N=int(input())
    # array=[0]
    # for i in range(N):
    #     k=int(input())
    #     array.append(k)

    # def solve(n):
    #     if(n==0):
    #         return array[0]
    #     elif(n==1):
    #         return array[1]
    #     elif(n==2):
    #         return (array[1]+array[2])
    #     else:
    #         return max(solve(n-3)+array[n-1]+array[n], solve(n-2)+array[n],solve(n-1))  
    # print(solve(N))

#백준 문제 < 포도주 시식 >
    # dp=[0]*10001
    # array=[0]*10001

    # N=int(input())
    # for i in range(1,N+1):
    #     array[i]=int(input())

    # dp[1]=array[1]
    # dp[2]=(array[1]+array[2])


    # for i in range(3,N+1):
    #     dp[i]= max(dp[i-3]+array[i-1]+array[i], dp[i-2]+array[i],dp[i-1])
    # print(dp[N])

#백준 문제 < 가장 긴 증가하는 부분 수열 > 
# N=int(input())
# array=list(map(int,input().split()))
# dp=[0]*1001
# for i in range(N):
#     dp[array[i]]=1
# print(dp.count(1))

#백준 문제 < 가장 긴 증가하는 부분 수열 > ->2번째 부터 선택해서 가장 큰 수열이 될수도 있겠다.
    # N=int(input())
    # array=list(map(int,input().split()))
    # dp=[]
    # for i in range(N):
    #     if(i>0):
    #         if dp[-1]<array[i]:
    #             dp.append(array[i])
    #     else:
    #         dp.append(array[0])
    # print(len(dp))

#백준 문제 < 가장 긴 증가하는 부분 수열>
    # N=int(input())
    # array=list((map(int,input().split())))
    # array.insert(0,0)
    # dp=[0]*1001
    # answer=0
    # for i in range(1,N+1):
    #     for j in range(0,i):
    #         if array[i]>array[j]:
    #             dp[i]=max(dp[i],dp[j]+1)
    #     answer=max(answer,dp[i])
    # print(answer)

#백준 문제 <내리막길> ->완전 탐색으로 잘 풀었는데, 시간초과 남 
    # from collections import deque
    # M,N=map(int,input().split())
    # graph=[]
    # for i in range(M):
    #     k=list(map(int,input().split()))
    #     graph.append(k)
    # dx=[0,0,-1,1]
    # dy=[1,-1,0,0]

    # queue=deque()
    # answer=[]
    # def BFS(x,y):
    #     queue.append((x,y))
    #     while queue:
    #         x,y=queue.popleft()
    #         if x==M-1 and y==N-1:
    #             answer.append(1) 
    #         for i in range(4):
    #             nx=x+dx[i]
    #             ny=y+dy[i]
    #             if(nx<0 or nx>=M or ny<0 or ny>=N):
    #                 continue
    #             else:
    #                 if(graph[x][y]>graph[nx][ny]):
    #                     queue.append((nx,ny))

    # BFS(0,0)
    # print(len(answer))

#백준 문제 < 내리막길 >
    # m,n=map(int,input().split())
    # map=[list(map(int,input().split())) for _ in range(m)]
    # dp=[[-1]*n for _ in range(m)]
    # move=[[0,1],[1,0],[0,-1],[-1,0]]

    # def dp_bruteForce(y,x):
    #     if dp[y][x]!=-1:
    #         return dp[y][x]
    #     if y==m-1 and x==n-1:
    #         return 1
    #     dp[y][x]=0
    #     for i in range(0,4):
    #         dy=y+move[i][0]
    #         dx=x+move[i][1]
    #         if 0 <=dy <m and 0<=dx<n and map[y][x]>map[dy][dx]:
    #             dp[y][x]+=dp_bruteForce(dy,dx)
    #     return dp[y][x]
    # print(dp_bruteForce(0,0))

# 백준 문제 <내리 막길>
    # N,M=map(int,input().split())
    # graph=[]
    # for i in range(N):
    #     k=list(map(int,input().split()))
    #     graph.append(k)
    # dp=[[-1]*M for _  in range(N)]
    # dx=[0,0,-1,1]
    # dy=[-1,1,0,0]

    # def check(x,y):
    #     if dp[x][y]!=-1:
    #         return dp[x][y]
    #     if(x==N-1 and y==M-1):
    #         return 1
    #     dp[x][y]=0
    #     for i in range(4):
    #         nx=x+dx[i]
    #         ny=y+dy[i]
    #         if(0<=nx<N and 0<=ny<M and graph[x][y]>graph[nx][ny]):
    #             dp[x][y]+=check(nx,ny)

    #     return dp[x][y]

    # print(check(0,0))

#코드포스 문제 < Flying sort >
    # dp=[0]*3001

    # for _ in range(int(input())):
    #     n=int(input())
    #     for i in range(n):
    #         dp[i]=1
    #     tmp=list(map(int,input().split()))
    #     a=[]
    #     mx=1
    #     for i in range(n):
    #         a.append([tmp[i],i])
    #     a.sort()
    #     for i in range(1,n):
    #         if a[i-1][1]<a[i][1]:
    #             dp[i]=dp[i-1]+1
    #         mx=max(mx,dp[i])
    #     print(n-mx)

# 백준 문제 < 스타트와 링크 >
# k=[0,1,2,3]
# k_1=[0,1]
# k_2=list(set(k)-set(k_1))
# print(k_2)
# from itertools import combinations
# import copy
# N=int(input())
# graph=[]
# for i in range(N):
#     k=list(map(int,input().split()))
#     graph.append(k)

# def sumation(array):
#     answer=0
#     for i in range(N//2):
#         for j in range(N//2):
#             if(i<j):
#                 answer+=(graph[array[i]][array[j]]+graph[array[j]][array[i]])
#     return answer
# origin_list=[0]*(N)
# for i in range(N):
#     origin_list[i]=i

# tmp_list=list(combinations(range(N),N//2))
# ans=1e9
# ans_1=0
# ans_2=0
# for i in range(len(tmp_list)):
#     tmp2_list=list(set(origin_list)-set(tmp_list[i]))
#     ans_1=sumation(tmp2_list)
#     ans_2=sumation(tmp_list[i])
#     ans=min(ans,abs(ans_1-ans_2))
# print(ans)

#백준 문제 < 스도쿠 >
sudoku=[]
for i in range(9):
    k=list(map(int,input().split()))
    sudoku.append(k)
zeros=[]
for i in range(9):
    for j in range(9):
        if(sudoku[i][j]==0):
            zeros.append((i,j))

def is_programming(x,y):
    num=[1,2,3,4,5,6,7,8,9]
    for i in range(9):
        if sudoku[i][y] in num:
            num.remove(sudoku[i][y])
        if sudoku[x][i] in num:
            num.remove(sudoku[x][i])

    x//=3
    y//=3
    for i in range(x*3,(x+1)*3):
        for j in range(y*3,(y+1)*3):
            if sudoku[i][j] in num:
                num.remove(sudoku[i][j])
    return num
flag=False 
def dfs(x):
    global flag
    if flag:
        return
    if x==len(zeros):
        for row in sudoku:
            print(*row)
        flag=True
        return

    else:
        (i,j)=zeros[x]
        promising=is_programming(i,j)

        for num in promising:
            sudoku[i][j]=num
            dfs(x+1)
            sudoku[i][j]=0
dfs(0)    