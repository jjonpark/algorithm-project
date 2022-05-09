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
    # sudoku=[]
    # for i in range(9):
    #     k=list(map(int,input().split()))
    #     sudoku.append(k)
    # zeros=[]
    # for i in range(9):
    #     for j in range(9):
    #         if(sudoku[i][j]==0):
    #             zeros.append((i,j))

    # def is_programming(x,y):
    #     num=[1,2,3,4,5,6,7,8,9]
    #     for i in range(9):
    #         if sudoku[i][y] in num:
    #             num.remove(sudoku[i][y])
    #         if sudoku[x][i] in num:
    #             num.remove(sudoku[x][i])

    #     x//=3
    #     y//=3
    #     for i in range(x*3,(x+1)*3):
    #         for j in range(y*3,(y+1)*3):
    #             if sudoku[i][j] in num:
    #                 num.remove(sudoku[i][j])
    #     return num
    # flag=False 

    # def dfs(x):
    #     global flag
    #     if flag:
    #         return
    #     if x==len(zeros):
    #         for row in sudoku:
    #             print(*row)
    #         flag=True
    #         return

    #     else:
    #         (i,j)=zeros[x]
    #         promising=is_programming(i,j)

    #         for num in promising:
    #             sudoku[i][j]=num
    #             dfs(x+1)
    #             sudoku[i][j]=0
    # dfs(0)    

#백준 문제 < 피보나치 함수 > 

    # T=int(input())
    # dp=[0]*41
    # dp[0]=[1,0]
    # dp[1]=[0,1]
    # for i in range(2,41):
    #     k_0=dp[i-2][0]+dp[i-1][0]
    #     k_1=dp[i-2][1]+dp[i-1][1]
    #     dp[i]=[k_0,k_1]

    # for i in range(T):
    #     N=int(input())
    #     print(f"{dp[N][0]} {dp[N][1]}")

#백준 문제 < 신나는 재귀 함수 >
    # import sys
    # input=sys.stdin.readline

    # dp=[[[0]*(21) for _ in range(21)] for _ in range(21)]

    # def w(a,b,c):
    #     if a<=0 or b<=0 or c<=0:
    #         return 1
    #     if a>20 or b>20 or c>20:
    #         return w(20,20,20)
    #     if dp[a][b][c]:
    #         return dp[a][b][c]
    #     if a<b<c:
    #         dp[a][b][c]= w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
    #         return dp[a][b][c]
    #     dp[a][b][c] =w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    #     return dp[a][b][c]

    # while 1:
    #     a,b,c=map(int,input().split())
    #     if a==-1 and b==-1 and c==-1:
    #         break
    #     print(f"w({a}, {b}, {c}) = {w(a,b,c)}")

#백준 문제 <퇴사>
    # N=int(input())
    # array=[]
    # for i in range(N):
    #     a,b=map(int,input().split())
    #     array.append([a,b])
    # dp=[0]*N
    # def BFS(depth):
    #     if depth>=N-1:
    #         return
    #     else:
    #         dp[depth]=max(dp[depth], dp[depth]+array[depth][1])
    #         BFS(depth+array[depth][0])
    #         BFS(depth+1)
    #     return
    # BFS(0)
    # print(dp)

#백준 문제 < 퇴사 >
    # N=int(input())
    # array=[]
    # dp=[0]*N
    # for i in range(N):
    #     a,b=map(int,input().split())
    #     array.append([a,b])

    # for i in range(N-1,-1,-1):
    #     if array[i][0]+i>N and i==N-1 :
    #         dp[i]=0
    #     elif array[i][0]==1 and i==N-1:
    #         dp[i]=array[i][1]
    #         continue
    #     else:
    #         if array[i][0]+i>N:
    #             dp[i]=dp[i+1]
    #         else:
    #             dp[i]=max(dp[i+1],dp[array[i][0]+i]+array[i][1])
    # k=max(dp)
    # print(k)

#백준 문제 삼성 sw 기출 < 퇴사 >
    # n=int(input())
    # t=[]
    # p=[]
    # dp=[]
    # for i in range(n):
    #     a,b=map(int,input().split())
    #     t.append(a)
    #     p.append(b)
    #     dp.append(b)
    # dp.append(0)
    # for i in range(n-1,-1,-1):
    #     if t[i]+i>n:
    #         dp[i]=dp[i+1]
    #     else:
    #         dp[i]=max(dp[i+1],p[i]+dp[i+t[i]])
    # print(dp[0])

#백준 문제 삼성 sw 기출 < 로봇 청소기 > -> 흠.. 뭔가 한끝차이 인거 같은데 
    # dx=[-1,0,1,0]
    # dy=[0,1,0,-1]

    # N,M=map(int,input().split())
    # xs,ys,d=map(int,input().split())
    # graph=[]
    # for i in range(N):
    #     k=list(map(int,input().split()))
    #     graph.append(k)

    # def go(x,y,d):
    #     x=x+dx[d]
    #     y=y+dy[d]
    #     return x,y,d
    # def back(x,y,d):
    #     k=(d+2)%4
    #     x=x+dx[k]
    #     y=y+dy[k]
    #     return x,y,d

    # ans=0
    # def clean(x,y,d):
    #     global ans
    #     graph[x][y]=2
    #     ans+=1
    #     for i in range(4):
    #         if 0<= (x+dx[d]) <N and 0<=(y+dy[d])<N:
    #             if graph[x+dx[d]][y+dy[d]] ==0:
    #                 x,y,d=go(x,y,d)
    #                 return clean(x,y,d)
    #             else:
    #                 d=(d+3)%4
    #     k=(d+2)%4
    #     if 0<= (x+dx[k]) <N and 0<=(y+dy[k]):
    #         if graph[x+dx[k]][y+dy[k]]==2:
    #             x,y,d=back(x,y,d)
    #             return clean(x,y,d)
    #     return
    # clean(xs,ys,d)
    # print(ans)

#백준 문제 < 로봇 청소기 문제 >
    # import sys
    # input=sys.stdin.readline
    # from collections import deque

    # n,m=map(int, input().split())
    # graph=[]
    # visited=[[0]*m for _ in range(n)]
    # r,c,d= map(int,input().split())

    # dx=[-1,0,1,0]
    # dy=[0,1,0,-1]

    # for _ in range(n):
    #     graph.append(list(map(int,input().split())))

    # visited[r][c] = 1
    # cnt = 1

    # while 1:
    #     flag=0
    #     for _ in range(4):
    #         nx=r+dx[(d+3)%4]
    #         ny=c+dy[(d+3)%4]
    #         d=(d+3)%4
    #         if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
    #             if visited[nx][ny]==0:
    #                 visited[nx][ny]=1
    #                 cnt+=1
    #                 r=nx
    #                 c=ny
    #                 flag=1
    #                 break
    #     if flag==0:
    #         if graph[r-dx[d]][c-dy[d]]==1:
    #             print(cnt)
    #             break
    #         else:
    #             r,c=r-dx[d],c-dy[d]
        
#백준 문제 삼성 SW 기출 <톱니 바퀴> 
# [2]번째와 다음편 [6]이 맞닿음 
    # from collections import deque
    # topni=[]
    # for i in range(4):
    #     k=list(str(input()))
    #     topni.append(k)
    # def rotation(a,b):
    #     if b==1:
    #         tmp=topni[a].pop()
    #         topni[a].insert(0,tmp)
    #     else: 
    #         topni[a].append(topni[a][0])
    #         del topni[a][0]
    #     return 
    # def program(a,b):
    #     connet=[]
    #     tmp=a
    #     while 1:
    #         if tmp==3:
    #             break
    #         if(topni[tmp][2] != topni[tmp+1][6]):
    #             connet.append(tmp+1)
    #         else:
    #             break
    #         tmp+=1
    #     tmp=a
    #     while 1:
    #         if tmp==0:
    #             break
    #         if(topni[tmp][6] != topni[tmp-1][2]):
    #             connet.append(tmp-1)
    #         else:
    #             break
    #         tmp-=1
    #     rotation(a,b)
    #     for i in connet:
    #         if(abs(i-a)==2):
    #             rotation(i,b)
    #         else:
    #             rotation(i,b*-1)
    # T=int(input())
    # for i in range(T):
    #     a,b=map(int,input().split())
    #     program(a-1,b)
    # ans=0
    # for i in range(4):
    #     if topni[i][0]=='1':
    #         ans+=(2**i)
    # print(ans)

#백준 문제 삼성 sw 기출 <인구 이동> -> 아이디어는 떠올랐는데, 구현이 어렵네.
    # N,L,R=map(int,input().split())
    # graph=[]
    # for i in range(N):
    #     k=list(map(int,input().split()))
    #     graph.append(k)
    # dx=[0,0,-1,1]
    # dy=[-1,1,0,0]
    # ans_list=[[]*2001]
    # def open_door(x,y):

    #     for i in range(4):
    #         nx=x+dx[i]
    #         ny=y+dy[i]
    #         if 0<=nx<N and 0<=ny<N:
    #             L<=abs(graph[nx][ny]-graph[x][y])<=R
    #             k.append(())

#백준 문제 삼성 SW 기출 <인구이동>
    # import sys
    # input=sys.stdin.readline
    # from collections import deque
    # n,l,r = map(int,input().split())
    # graph=[list(map(int,input().split())) for _ in range(n)]
    # dx=[-1,0,1,0]
    # dy=[0,1,0,-1]
    # cnt=0

    # def bfs(i,j):
    #     q=deque()
    #     q.append([i,j])
    #     temp=[]
    #     temp.append([i,j])
    #     while q:
    #         x,y=q.popleft()
    #         for i in range(4):
    #             nx=x+dx[i]
    #             ny=y+dy[i]
    #             if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
    #                 if l<=abs(graph[nx][ny]-graph[x][y])<=r :
    #                     visit[nx][ny]=1
    #                     q.append([nx,ny])
    #                     temp.append([nx,ny])
    #     return temp

    # while True:
    #     visit=[[0]*n for i in range(n)]
    #     isTrue=False
    #     for i in range(n):
    #         for j in range(n):
    #             if visit[i][j]==0:
    #                 visit[i][j]=1
    #                 temp=bfs(i,j)
    #                 if len(temp)>1:
    #                     isTrue=True
    #                     num=sum([graph[x][y] for x,y in temp])// len(temp)
    #                     for x,y in temp:
    #                         graph[x][y]=num
    #     if not isTrue:
    #         break
    #     cnt+=1
    # print(cnt)

#백준 문제 삼성 SW 기출 < 괄호 추가하기 >

    # order=['+','-','*']
    # N=int(input())
    # origin = input()
    # answer = -0xfffffff
    # orders = []
    # candidates = []
    # num = ''

    # for unit in origin:
    #     if unit not in order:
    #         num += unit
    #     else:
    #         orders.append(int(num))
    #         orders.append(unit)
    #         num=''
    # orders.append(int(num))
    # def calculate(num1,order,num2):
    #     if order=='+':
    #         return num1 + num2
    #     elif order == '-':
    #         return num1-num2
    #     else:
    #         return num1 * num2

    # def move(idx, cnt, flag, orders): #괄호 사용여부를 판별 하는 함수
    #     global count
    #     if cnt == count:
    #         candidates.append(orders)
    #         return
    #     if flag: #이전에 괄호를 사용했으면 다음에는 무조건 사용 X
    #         move(idx+2,cnt+1,False,orders)
    #     else:
    #         # 1. 괄호를 사용하는 경우 (해당 연산을 미리 계산한다.)
    #         move(idx, cnt+1, True, orders[:idx-1] + [calculate(orders[idx-1], orders[idx], orders[idx+1])] + orders[idx+2:]) 
    #         move(idx+2, cnt+1, False, orders)

    # count=len(orders)//2
    # move(1,0,False,orders)

    # for candidate in candidates:
    #     target = candidate[::-1]
    #     for i in range(len(candidate)//2):
    #         target.append(calculate(target.pop(), target.pop(), target.pop()))
    #     answer = max(answer, target[0])
    # print(answer)

#백준 문제 삼성 SW 기출 <캐슬 디펜스> -> 구현 의 근처도 못가겠네 이거.. 
    # from itertools import combinations
    # N,M,D=map(int,input().split())

    # graph=[]
    # for i in range(N):
    #     k=list(map(int,input().split()))
    #     graph.append(k)

    # def move():
    #     global graph
    #     for i in range(N-1,0,-1):
    #         graph[i]=graph[i-1]
    #     for j in range(M):
    #         graph[0][j]=0
    #     return

    # def check():
    #     flag=False
    #     for i in range(N):
    #         for j in range(M):
    #             if graph[i][j]==0:
    #                 flag=True
    #     return flag

    # lst=list(combinations(range(5),3))

    # def program():
    #     while check():
    #         visited=[]

    # while lst:
    #     a,b,c=lst.pop()

#백준 문제 삼성 SW 기출 <캐슬 티펜스>
    # from itertools import combinations
    # from copy import deepcopy
    # import sys

    # N,M,D=map(int,sys.stdin.readline().split())
    # #적군의 위치를 저장하는 set
    # enemy_position=set()
    # for y in range(N):
    #     arr=list(map(int,sys.stdin.readline().split()))
    #     for x in range(M):
    #         if arr[x]==1:
    #             enemy_position.add((y,x))

    # maps=[[0 for _ in range(M)]for _ in range(N)]

    # archer_position=[(N,i)for i in range(M)]

    # candidates=combinations(archer_position,3)

    # #궁사 위치별로 사격 가능한 적군 거리를 계산하는 함수, 3명의 위치 당 사격 가능한좌표,까지의 거리를 계산
    # def get_distance(maps,candidates,D):
    #     possible_attack_area=[]
    #     for position in candidates:
    #         copied=[]
    #         for y in range(len(maps)):
    #             for x in range(len(maps[0])):
    #                 if abs(position[0]-y) +abs(position[1]-x)<=D:
    #                     copied.append([(abs(position[0]-y) + abs(position[1]-x)),y,x])
    #         possible_attack_area.append(copied)
    #     return possible_attack_area

    # #적군이 전진하는 함수 
    # def go_forward(enemy_position, N):
    #     return set([(y+1,x) for y, x in enemy_position if y+1<N])

    # #공격 가능한 '가장 가까운 적' 을 찾는 함수 
    # def find_nearest_enemy(arc, enemy_position):
    #     arc.sort(key=lambda x:(x[0],x[2]))
    #     for dist, y, x in arc:
    #         if (y,x) in enemy_position:
    #             return (y,x)
    #     return None

    # maxs=0
    # for archors in candidates:
    #     arc=get_distance(maps,archors,D)
    #     kills=0
    #     #각 경우의 수 마다 적 위치는 초기화 해야 하므로 
    #     copy_enemy_map=deepcopy(enemy_position)
    #     while enemy_position:
    #         temp=set()
    #         for arc_map in arc:
    #             kill=find_nearest_enemy(arc_map,enemy_position)
    #             if kill is not None:
    #                 temp.add(kill)
    #         kills+=len(temp)

    #         enemy_position-=temp

    #         enemy_position=go_forward(enemy_position,N)
        
    #     enemy_position=copy_enemy_map
    #     if maxs < kills:
    #         maxs=kills
    # print(maxs)

#백준 문제 <단지 번호 붙이기> -> 다 왔는데 카운트 하는걸 모르겠다
    # from collections import deque
    # N= int(input())
    # answer_list=[]*626
    # graph=[]
    # for i in range(N):
    #     k=list(str(input()))
    #     for j in range(N):
    #         k[j]=int(k[j])
    #     graph.append(k)
    # visited=[[0]*N for _ in range(N)]

    # dx=[-1,1,0,0]
    # dy=[0,0,1,-1]
    # queue=deque()
    # cnt=1
    # def BFS(x,y):
    #     global cnt, graph, visited
    #     if(graph[x][y]==1 and visited[x][y]==0):
    #         graph[x][y]=2
    #         visited[x][y]=cnt
        
    #     queue.append((x,y))
    #     while queue:
    #         x,y=queue.popleft()
    #         for i in range(4):
    #             nx=x+dx[i]
    #             ny=y+dy[i]
    #             if 0<=nx<N and 0<=ny<N and graph[nx][ny]==1 and visited[nx][ny]==0:
    #                 graph[nx][ny]=2
    #                 visited[nx][ny]=cnt
    #                 queue.append((nx,ny))
    #             else: 
    #                 continue
    #     cnt+=1
    #     return

    # for i in range(N):
    #     for j in range(N):
    #         if visited[i][j]==0:
    #             BFS(i,j)

    # print(visited)

#백준 문제 <단지 번호 붙이기> 풀이 
    # from collections import deque

    # dx=[0,0,-1,1]
    # dy=[-1,1,0,0]
    # def bfs(graph,a,b):
    #     n=len(graph)
    #     queue=deque()
    #     queue.append((a,b))
    #     graph[a][b]=0
    #     count=1

    #     while queue:
    #         x,y=queue.popleft()
    #         for i in range(4):
    #             nx=x+dx[i]
    #             ny=y+dy[i]
    #             if nx<0 or nx>=n or ny<0 or ny>=n:
    #                 continue
    #             if graph[nx][ny]==1:
    #                 graph[nx][ny]=0
    #                 queue.append((nx,ny))
    #                 count+=1
    #     return count
    # n=int(input())
    # graph=[]
    # for i in range(n):
    #     graph.append(list(map(int,input())))

    # cnt=[]
    # for i in range(n):
    #     for j in range(n):
    #         if graph[i][j]==1:
    #             cnt.append(bfs(graph,i,j))
    # cnt.sort()
    # print(len(cnt))
    # for i in range(len(cnt)):
    #     print(cnt[i])

#백준 문제 <안전영역>
import copy
from collections import deque
N=int(input())
graph=[]
max=0
for i in range(N):
    k=list(map(int,input().split()))
    graph.append(k)
    for j in range(N):
        if max<k[j]:
            max=k[j]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
def make_graph(i):
    list_graph=copy.deepcopy(graph)
    for x in range(N):
        for y in range(N):
            if(list_graph[x][y]<=i):
                list_graph[x][y]=0
            else: 
                list_graph[x][y]=1
    return list_graph

def BFS(graph,x,y):
    n=len(graph)
    queue=deque()
    queue.append((x,y))
    count=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
                count+=1
    return count

cnt=[]
max_answer=0
for k in range(1,max):
    tmp_graph=make_graph(k)
    cnt=[]
    for i in range(N):
        for j in range(N):
            if tmp_graph[i][j]==1:
                cnt.append(BFS(tmp_graph,i,j))
    if max_answer<len(cnt):
        max_answer=len(cnt)

print(max_answer)

