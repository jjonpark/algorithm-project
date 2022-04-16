# <백준 알고리즘> 라면사기 -> 시간 초과........
    # import sys
    # import reuddline
    # x=int(sys.stdin.readline())
    # y=list(map(int,sys.stdin.readline().split()))
    # result=0
    # while y:
    #     if(y[0]==0):
    #         y.pop(0)
    #         continue
    #     if(len(y)>=3):
    #         if(y[0]>=1 and y[1]>=1 and y[2]>=1):
    #             result+=7
    #             y[0]-=1
    #             y[1]-=1
    #             y[2]-=1
    #             continue
    #         elif(y[0]>=1 and y[1]>=1):
    #             result+=5
    #             y[0]-=1
    #             y[1]-=1
    #             continue
    #         else:
    #             result+=3
    #             y[0]-=1
    #             continue
    #     elif(len(y)>=2):
    #         if(y[0]>=1 and y[1]>=1):
    #             result+=5
    #             y[0]-=1
    #             y[1]-=1
    #             continue
    #         else:
    #             result+=3
    #             y[0]-=1
    #             continue
    #     else:
    #         result+=3
    #         y[0]-=1
    #         continue
    # print(result)

#백준 알고리즘 < 라면사기 >
    # import sys
    # input = sys.stdin.readline

    # def buy_triple(idx):
    #     global cost
    #     k = min(arr[idx: idx + 3])
    #     arr[idx] -= k
    #     arr[idx + 1] -= k
    #     arr[idx + 2] -= k
    #     cost += 7 * k
    # def buy_double(idx):
    #     global cost
    #     k = min(arr[idx: idx + 2])
    #     arr[idx] -= k
    #     arr[idx + 1] -= k
    #     cost += 5 * k
    # def buy_each(idx):
    #     global cost
    #     cost += 3 * arr[idx]
    # N = int(input())
    # arr = list(map(int, input().split())) + [0, 0]
    # cost = 0
    # for i in range(N):
    #     if arr[i + 1] > arr[i + 2]:
    #         k = min(arr[i], arr[i + 1] - arr[i + 2])
    #         arr[i] -= k
    #         arr[i + 1] -= k
    #         cost += 5 * k
    #         buy_triple(i)
    #     else:
    #         buy_triple(i)
    #         buy_double(i)
    #     buy_each(i)
    # print(cost)
 
#DFS, BFS 이건 필수로 알아야 하니 나동빈 한번더 들어보자 
#queue 자료구조 사용
    # from collections import deque
    # queue = deque()
    # queue.append(5)
    # queue.append(2)
    # queue.append(3)
    # queue.append(7)
    # queue.popleft()
    # queue.append(1)
    # queue.append(4)
    # queue.popleft()
    # print(queue)
    # queue.reverse()
    # print(queue)

#DFS 깊이 우선 탐색
    # graph=[[], [2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]
    # visited=[False]*9
    # def DFS(graph, v, visited):
    #     visited[v]=True
    #     print(v, end=" ")
    #     for i in graph[v]:
    #         if not visited[i]:
    #             DFS(graph, i, visited)
    # DFS(graph, 1, visited)

#BFS 너비 우선 탐색
    # from collections import deque
    # graph=[[], [2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]
    # visited=[False]*9
    # def BFS(graph, start, visited):
    #     queue=deque([start])
    #     visited[start]=True
    #     while queue:
    #         v=queue.popleft()
    #         print(v, end=" ")
    #         for i in graph[v]:
    #             if not visited[i]:
    #                 queue.append(i)
    #                 visited[i]=True
    # BFS(graph, 1, visited)

#나동빈 코딩테스트 <음료수 얼려먹기>
    # N,M=map(int,input().split())
    # graph=[]
    # visited=[]
    # for i in range(N):
    #     graph.append(list(map(int,input())))
    #     visited.append([0]*M)
    # def DFS(x,y):
    #     if x<=-1 or x>=N or y<=-1 or y>=M:
    #         return False
    #     if graph[x][y]==0:
    #         graph[x][y]=1
    #         DFS(x-1,y)
    #         DFS(x,y-1)
    #         DFS(x+1,y)
    #         DFS(x,y+1)
    #         return True
    #     return False
    # result=0
    # for i in range(N):
    #     for j in range(M):
    #         if DFS(i,j)==True:
    #             result+=1
    # print(result)

#<나동빈 알고리즘> 미로 탈출 문제 
    # from collections import deque
    # N,M=map(int,input().split())
    # graph=[]
    # for i in range(N):
    #     graph.append(list(map(int,input())))

    # def BFS(graph,x,y):
    #     queue=deque()
    #     queue.append([x,y])
    #     while queue:
    #         tmp1,tmp2=queue.popleft()
    #         if tmp1<=-1 or tmp1>=N or tmp2<=-1 or tmp2>=M:
    #             queue.popleft()
    #         elif graph[tmp1][tmp2]==0:
    #             queue.popleft()
    #         else:
    #             queue.append([tmp1+1,tmp2])
    #             queue.append([tmp1,tmp2+1])
    #             queue.append([tmp1-1,tmp2])
    #             queue.append([tmp1,tmp2-1])

    # queue=deque()
    # queue.append([2,3])
    # print(queue)
    # tmp1,tmp2=queue.popleft()
    # print(f"{tmp1} {tmp2}")

#나동빈 알고리즘 미로 찾기 
    # from collections import deque
    # n,m=map(int,input().split())
    # graph=[]
    # for i in range(n):
    #     graph.append(list(map(int,input())))
    # dx=[-1,1,0,0]
    # dy=[0,0,-1,1]

    # def BFS(x,y):
    #     queue=deque()
    #     queue.append(x,y)
    #     while queue:
    #         x,y=queue.popleft()
    #         for i in range(4):
    #             nx=x+dx[i]
    #             ny=y+dy[i]
    #             if nx<0 or nx>=n or ny<0 or ny>=m:
    #                 continue
    #             if graph[nx][ny]==0:
    #                 continue
    #             if graph[nx][ny]==1:
    #                 graph[nx][ny]==graph[x][y]+1
    #                 queue.append((nx,ny))
    #     return graph[n-1][m-1]
    # print(BFS(0,0))

# 나동빈 알고리즘 특정 거리의 도시 찾기 문제 -> 도전 하였으나 실패..
# from collections import deque
# n,m,k,x=map(int,input().split())
# graph=[]
# distance=[]*(n+1)
# for i in range(m):
#     graph.append(list(map(int,input().split())))

# def BFS(x):
#     queue=deque()
#     queue.append(x)
#     while queue:
#         for i in range(m):
#             if(graph[i][0]==x):
#                 queue.append(graph[i][1])
#             elif(graph[i][1]==)

#나동빈 알고리즘 특정거리 도시 찾기 문제 풀이 
    # from collections import deque
    # n,m,k,x=map(int,input().split())
    # graph=[[]for _ in range(n+1)]
    # for _ in range(m):
    #     a,b=map(int,input().split())
    #     graph[a].append(b)
    # distance = [-1]*(n+1) #모든 도시에 대한 최단 거리 초기화 
    # distance[x]=0
    # q=deque([x])
    # while q:
    #     now=q.popleft() #현재 도시에서 이동할수 있는 모든 도시 확인
    #     for next_node in graph[now]:
    #         if distance[next_node]==-1:
    #             distance[next_node]=distance[now]+1
    #             q.append(next_node)
    # check = False
    # for i in range(1,n+1):
    #     if distance[i]==k:
    #         print(i)
    #         check=True
    # if check==False:
    #     print(-1)

#나동빈 알고리즘 -바이러스 증식 문제- 이거 진짜 어려운디?
    # from collections import deque
    # n,k=map(int,input().split())
    # graph=[]
    # data=[] #바이러스에 대한 정보를 담는 리스트
    # for i in range(n):
    #     graph.append(list(map(int,input().split())))
    #     for j in range(n):
    #         if graph[i][j]!=0:
    #             data.append((graph[i][j],0,i,j)) #(바이러스 종류, 시간, 위치 x, 위치 y) 삽입
    # data.sort()
    # q= deque(data)
    # target_s,target_x,target_y=map(int,input().split())
    # dx=[-1,0,1,0]
    # dy=[0,1,0,-1]
    # while q:
    #     virus, s, x, y= q.popleft()
    #     if s == target_s: #정확히 s초가 지나거나, 큐가 빌때까지 반복
    #         break
    #     for i in range(4):
    #         nx=x+dx[i]
    #         ny=y+dy[i]
    #         if 0<= nx and nx<n and 0 <=ny and ny<n:
    #             if graph[nx][ny]==0:
    #                 graph[nx][ny]=virus
    #                 q.append((virus, s + 1, nx, ny))

    # print(graph[target_x-1][target_y-1])

#백준 알고리즘 <연구소> -> 잠깐 보류 
    # import collections
    # import sys
    # ClEAN=0
    # WALL=1
    # VIRUS=2
    # lab=[[0] for _ in range(8) for _ in range(8)]
    # mirror = [[0 for _ in range(8)] for _ in range(8)]
    # q_virus_original = collections.deque()

    # def solve():
    #     pass

    # N,M= map(int,sys.stdin.readline().split())
    # for r in range(N):
    #     l = list(map(int,sys.stdin.readline()))
    #     for c in range(M):
    #         lab[r][c]= l[c]
    #         if lab[r][c] is VIRUS:
    #             q_virus_original.append((r,c))
    # solve()

#백준 알고리즘 <백설공주와 일곱 난쟁이> 아직 입력안함
    # import sys
    # y=[]
    # no=[]
    # sum=0
    # for _ in range(9):
    #     k=int(sys.stdin.readline())
    #     sum+=k
    #     y.append(k)

    # for i in range(9):
    #     for j in range(i+1,9):
    #         result=(y[i]+y[j])
    #         if(result==(sum-100)):
    #             no.append(y[i])
    #             no.append(y[j])
    #             break
    # y.remove(no[0])
    # y.remove(no[1])
    # for i in y:
    #     print(i)

#백준 알고리즘 <모든 순열> -> 기존 제공 함수 활용
    # from itertools import permutations #순열 함수 
    # import sys
    # N=int(sys.stdin.readline())
    # N_list=[i for i in range(1,N+1)]
    # for numbers in list(permutations(N_list)):
    #     for num in numbers:
    #         print(num, end=' ')
    #     print()

#백준 알고리즘 <모든 순열> <DFS 활용> 
    # n=int(input())
    # ch=[0]*n
    # ans=[0]*n
    # def DFS(L):
    #     if L==n:
    #         print(' '.join(map(str,ans)))
    #     for i in range(n):
    #         if ch[i]==0:
    #             ch[i]=1
    #             ans[L]=i+1
    #             DFS(L+1)
    #             ch[i]=0
    # DFS(0)

#백준 알고리즘 <모든 순열> for 문 함수 활용
    # visited = [0]*4
    # for i in range(1,4):
    #     visited[i]=1
    #     for j in range(1,4):
    #         if visited[j]:
    #             continue
    #         visited[j]=1
    #         for k in range(1,4):
    #             if visited[k]:
    #                 continue
    #             visited[k]=1
    #             print(i,j,k)
    #             visited[k]=0
    #         visited[j]=0
    #     visited[i]=0

#백준 알고리즘 <모든 순열> 재귀 함수 활용
    # import sys
    # x=int(sys.stdin.readline())
    # array=[]
    # for i in range(1,x+1):
    #     array.append(i)
    # visited=[0]*x
    # answer=[0]*x

    # def permutaion(level):
    #     if level==x:
    #         for _ in answer:
    #             print(_,end=" ")
    #         print()
    #         return
    #     for i in range(x):
    #         if visited[i]:
    #             continue
    #         visited[i]=1
    #         answer[level]=array[i]
    #         permutaion(level+1)
    #         visited[i]=0

    # permutaion(0)

#나동빈 알고리즘 미로 찾기 
    # from collections import deque
    # n,m=map(int,input().split())
    # graph=[]
    # for i in range(n):
    #     graph.append(list(map(int,input())))
    # dx=[-1,1,0,0]
    # dy=[0,0,-1,1]

    # def BFS(x,y):
    #     queue=deque()
    #     queue.append(x,y)
    #     while queue:
    #         x,y=queue.popleft()
    #         for i in range(4):
    #             nx=x+dx[i]
    #             ny=y+dy[i]
    #             if nx<0 or nx>=n or ny<0 or ny>=m:
    #                 continue
    #             if graph[nx][ny]==0:
    #                 continue
    #             if graph[nx][ny]==1:
    #                 graph[nx][ny]==graph[x][y]+1
    #                 queue.append((nx,ny))
    #     return graph[n-1][m-1]
    # print(BFS(0,0))

#백준 알고리즘 <미로탐색>
    # import sys
    # from collections import deque
    # N,M=map(int,sys.stdin.readline().split())
    # graph=[]
    # for i in range(N):
    #     graph.append(list(map(int,sys.stdin.readline().strip())))
    # dx=[-1,1,0,0]
    # dy=[0,0,-1,1]
    # array=[[] for _ in range(N)]

    # def BFS(x,y):
    #     queue=deque()
    #     queue.append((x,y))
    #     while queue:
    #         x,y=queue.popleft()
    #         for i in range(4):
    #             nx=x+dx[i]
    #             ny=y+dy[i]
    #             if nx<0 or nx>(N-1) or ny<0 or ny>(M-1):
    #                 continue
    #             if graph[nx][ny]==0:
    #                 continue
    #             if graph[nx][ny]==1:
    #                 graph[nx][ny]=graph[x][y]+1
    #                 queue.append((nx,ny))
    #     return graph[N-1][M-1]

    # print(BFS(0,0))
#백준 알고리즘 <촌수 계산>
    # import sys
    # from collections import deque
    # x=int(sys.stdin.readline())
    # start,end=map(int,sys.stdin.readline().split())
    # num=int(sys.stdin.readline())
    # distance=[-1]*(x+1)
    # graph=[[]for _ in range(x+1)]
    # for i in range(num):
    #     a,b=map(int,sys.stdin.readline().split())
    #     graph[a].append(b)
    #     graph[b].append(a)
    # distance[start]=0

    # def DFS(graph,start,end):
    #     queue=deque([start])
    #     while queue:
    #         now=queue.popleft()
    #         for next_node in graph[now]:
    #             if distance[next_node]==-1:
    #                 distance[next_node]=distance[now]+1
    #                 queue.append(next_node)
    #     result=distance[end]
    #     return result
    # print(DFS(graph,start,end))

#백준 알고리즘 <바이러스>
    # import sys
    # from collections import deque
    # num=int(sys.stdin.readline())
    # line=int(sys.stdin.readline())
    # graph=[[]for _ in range(num+1)]
    # for i in range(line):
    #     a,b=map(int,sys.stdin.readline().strip().split())
    #     graph[a].append(b)
    #     graph[b].append(a)
    # visited=[0]*(num+1)

    # def BFS(start):
    #     queue=deque([start])
    #     visited[start]=1
    #     while queue:
    #         now=queue.popleft()
    #         for next_node in graph[now]:
    #             if(visited[next_node]==1):
    #                 continue
    #             else:
    #                 queue.append(next_node)
    #                 visited[next_node]=1
    #     return
    # BFS(1)
    # count=0
    # for _ in visited:
    #     if(_==1):
    #         count+=1
    # print(count-1)

#백준 알고리즘 <삼성 A형 기출> <괄호 추가하기>
    # import sys
    # input=sys.stdin.readline
    # x=int(input())

    # def cal(n1,n2,op):
    #     if op == '+':
    #         return n1 + n2
    #     elif op == '-':
    #         return n1 - n2
    #     elif op == '+':
    #         return n1 * n2
    # max_sum = float('-inf')

    # def dfs(idx, ans):
    #     global max_sum
    #     if idx >= len(opr):
    #         max_sum = max(max_sum, ans)
    #         return 
    #     dfs(idx+1,cal(ans,num[idx+1],opr[idx]))

    #     if idx+1 < len(opr):
    #         dfs(idx+2,cal(ans, cal(num[idx+1],num[idx+2],opr[idx+1]), opr[idx]))
    # num,opr=[], []
    # def sol(m):
    #     for i in m[:-1]:
    #         if i.isdigit():
    #             num.append(int(i))
    #         else:
    #             opr.append(i)
    #     dfs(0,num[0])
    # sol(m)
    # print(max_sum)

#백준 알고리즘 < 평범한 배낭 > -> 이게 DP 문제라고라!?
    # import sys
    # N,K=map(int,sys.stdin.readline().split())
    # list=[]
    # for i in range(N):
    #     k_1,k_2=map(int,sys.stdin.readline().split())
    #     k_3=(k_2/k_1)
    #     list.append([k_1,k_2,k_3])
    # list=sorted(list, key=lambda x:x[2], reverse=True)
    # weight=0
    # value=0
    # for i in range(N):
    #     weight+=list[i][0]
    #     if(weight>K):
    #         weight-=list[i][0]
    #     else:
    #         value+=list[i][1]
    # print(value)

# 백준 알고리즘 <평범한 배낭> 풀이 
    # N,K = map(int,input().split())
    # weight=[0]
    # value=[0]
    # dp=[[0] *(K+1) for _ in range(N+1)]
    # for i in range(N):
    #     W,V=map(int,input().split())
    #     weight.append(W)
    #     value.append(V)
    # for i in range(1,N+1):
    #     for j in range(1,K+1):
    #         if weight[i]<=j:
    #             dp[i][j]= max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
    #         else:
    #             dp[i][j]=dp[i-1][j]
                
# 백준 알고리즘 <평범한 배낭> 강의 풀이
    # def solve():
    #     n,k=[int(x) for x in input().split()]
    #     table = [0]*(k+1)
    #     for _ in range(n):
    #         w,v=[int(x) for x in input().split()]
    #         if w>k:
    #             continue
    #         for j in range(k,0,-1):
    #             if j + w <=k and table[j]!=0:
    #                 table[j+w]= max(table[j+w], table[j]+v)
    #         table[w] = max(table[w], v)
    #     print(max(table))
    # solve()

#나동빈 코딩테스트 <음료수 얼려먹기>
    # N,M=map(int,input().split())
    # graph=[]
    # visited=[]
    # for i in range(N):
    #     graph.append(list(map(int,input())))
    #     visited.append([0]*M)
    # def DFS(x,y):
    #     if x<=-1 or x>=N or y<=-1 or y>=M:
    #         return False
    #     if graph[x][y]==0:
    #         graph[x][y]=1
    #         DFS(x-1,y)
    #         DFS(x,y-1)
    #         DFS(x+1,y)
    #         DFS(x,y+1)
    #         return True
    #     return False
    # result=0
    # for i in range(N):
    #     for j in range(M):
    #         if DFS(i,j)==True:
    #             result+=1
    # print(result)

#백준 알고리즘 <배추밭 문제>
    # import sys
    # T= int(sys.stdin.readline())
    # def DFS(x,y):
    #     if x<0 or x>N-1 or y<0 or y>M-1:
    #         return False
    #     if graph[x][y]==1:
    #         graph[x][y]=0
    #         DFS(x-1,y)
    #         DFS(x+1,y)
    #         DFS(x,y-1)
    #         DFS(x,y+1)
    #         return True
    #     return False

    # for test_case in range(1,T+1):
    #     M,N,K=map(int,sys.stdin.readline().split())
    #     graph=[[0]*M for _ in range(N)]
    #     for i in range(K):
    #         tmp1,tmp2=map(int,sys.stdin.readline().split())
    #         graph[tmp2][tmp1]=1
    #     result=0
    #     for i in range(N):
    #         for j in range(M):
    #             if DFS(i,j)==True:
    #                 result+=1
    #     print(result)

#백준 알고리즘 <배추밭 문제> DFS 풀이 -->중요
    # t = int(input())
    # dx = [1, -1, 0, 0]
    # dy = [0, 0, -1, 1]
    # def dfs(x, y):
    #     queue = [[x, y]]
    #     while queue:
    #         a, b = queue[0][0], queue[0][1]
    #         del queue[0]
    #         for i in range(4):
    #             q = a + dx[i]
    #             w = b + dy[i]
    #             if 0 <= q < n and 0 <= w < m and s[q][w] == 1:
    #                 s[q][w] = 0
    #                 queue.append([q, w])
    # for i in range(t):
    #     m, n, k = map(int, input().split())
    #     s = [[0] * m for i in range(n)]
    #     cnt = 0
    #     for j in range(k):
    #         a, b = map(int, input().split())
    #         s[b][a] = 1
    #     for q in range(n):
    #         for w in range(m):
    #             if s[q][w] == 1:
    #                 dfs(q, w)
    #                 s[q][w] = 0
    #                 cnt += 1
    #     print(cnt)

    # #위의 풀이 내껄로 만들기 
    # dx=[-1,1,0,0]
    # dy=[0,0,1,-1]
    # def DFS(x,y):
    #     queue=[[x,y]]
    #     while queue:
    #         a,b=queue[0][0],queue[0][1]
    #         del queue[0]
    #         for i in range(4):
    #             q=a+ dx[i]
    #             w=b+ dy[i]
    #             if 0<q<n and 0<w<m and s[q][w]==1:
    #                 s[q][w]=0
    #                 queue.append([q,w])

#백준 알고리즘 <달팽이는 올라가고 싶다>
    # import sys
    # A,B,V=map(int,sys.stdin.readline().split())
    # result=0
    # if A>=V:
    #     result=1
    # tmp1=V-A
    # tmp2=A-B
    # if tmp1%tmp2==0:
    #     result=(tmp1//tmp2)+1
    # else:
    #     result=(tmp1//tmp2)+2
    # print(result)

#프로그래머스 <오픈 채팅방>
    # def solution(record):
    #     answer = []
    #     trace = []
    #     map={} #사전 자료형 
    #     for i in range(len(record)):
    #         tmp=record[i].split(' ')

    #         if tmp[0]=="Enter":
    #             map[tmp[1]]=tmp[2]
    #             trace.append([tmp[0],tmp[1]])
    #         elif tmp[0]=="Leave":
    #             trace.append([tmp[0],tmp[1]])
    #         else:
    #             map[tmp[1]]=tmp[2]

    #     for j in range(len(trace)):
    #         if trace[j][0]=="Enter":
    #             result=map[trace[j][1]] + "님이 들어왔습니다."
    #             answer.append(result)
    #         elif trace[j][0]=="Leave":
    #             result=map[trace[j][1]] + "님이 나갔습니다."
    #             answer.append(result)

    #     return answer

#백준 알고리즘 <치킨 배달> ->내가 전개한 대로 풀면 안댐
    # import sys
    # N,M = map(int,sys.stdin.readline().split())
    # graph=[[]*N for _ in range(N)]
    # for i in range(N):
    #     graph[i]=list(map(int,sys.stdin.readline().strip().split()))

    # def distance(x,y):
    #     result=0
    #     for i in range(N):
    #         for j in range(N):
    #             if(graph[i][j]==1):
    #                 result+=(abs(i-x)+abs(j-y))
    #     return result

    # visited=[[0]*N for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         if graph[i][j]==2:
    #             visited[i][j]=distance(i,j)
    # print(visited)

#백준 알고리즘 <치킨 배달> 콤비네이션을 활용한 풀이 (완전 탐색)
    # n,m = map(int, input().split())
    # City=[list(map(int,input().split())) for _ in range(n)]
    # answer = 987654321
    # house = []
    # for i in range(n):
    #     for j in range(n):
    #         if(City[i][j] == 1):
    #             house.append((i,j))
    # def Min_distance(chicken, house):
    #     sum_Distance=[]
    #     for i in house:
    #         min_D = 987654321
    #         for j in chicken:
    #             Distance= abs(i[0]-j[0]) + abs(i[1]-j[1])
    #             min_D=min(min_D,Distance)
    #         sum_Distance.append(min_D)
    #     return sum_Distance
    # def Brute_Force(idx, x, y):
    #     global answer
    #     if(idx == m):
    #         choice_chicken=[]
    #         for i in range(n):
    #             for j in range(n):
    #                 if(City[i][j]==3):
    #                     choice_chicken.append((i,j))
    #         res=Min_distance(choice_chicken,house)
    #         if(answer>sum(res)):
    #             answer=sum(res)
    #         return
    #     else:
    #         for i in range(x,n):
    #             if(i==x):
    #                 k=y
    #             else:
    #                 k=0
    #             for j in range(k,n):
    #                 if(City[i][j]==2):
    #                     City[i][j]=3
    #                     Brute_Force(idx+1,i,j+1)
    #                     City[i][j]=2
    # Brute_Force(0,0,0)
    # print(answer)

