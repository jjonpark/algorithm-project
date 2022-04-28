#백준 문제 풀이 로마 숫자 
    # x_1=list(str(input()))
    # x_2=list(str(input()))

    # def roma_to_num(x:list) ->int:
    #     result=0
    #     list={"I":1,"V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    #     result+=list[x[0]]
    #     for i in range(1,len(x)):
    #         if x[i] in list.keys():
    #             result+=list[x[i]]
    #         if list[x[i-1]] < list[x[i]]:
    #             result -=(list[x[i-1]]*2)
    #     result=int(result)
    #     return result

    # def num_to_roma(n:int)->str:
    #     s=""
    #     while n>0:
    #         if n>=1000:
    #             s+="M"
    #             n-=1000
    #         elif n>=900:
    #             s+="CM"
    #             n-=900
    #         elif n>=500:
    #             s+="D"
    #             n-=500
    #         elif n>=400:
    #             s+="CD"
    #             n-=400
    #         elif n>=100:
    #             s+="C"
    #             n-=100
    #         elif n>=90:
    #             s+="XC"
    #             n-=90
    #         elif n>=50:
    #             s+="L"
    #             n-=50
    #         elif n>=40:
    #             s+="XL"
    #             n-=40
    #         elif n>=10:
    #             s+="X"
    #             n-=10
    #         elif n>=9:
    #             s+="IX"
    #             n-=9
    #         elif n>=5:
    #             s+="V"
    #             n-=5
    #         elif n>=4:
    #             s+="IV"
    #             n-=4
    #         elif n>=1:
    #             s+="I"
    #             n-=1
    #     return s

    # answer_num= (roma_to_num(x_1) + roma_to_num(x_2))
    # print(answer_num)
    # print(num_to_roma(answer_num))

    # #백준 알고리즘 <패션왕 신해빈>
    # T=int(input())
    # for test_case in range(1,T+1):
    #     x=int(input())
    #     kinds_list={}
    #     num_list=[]
    #     for i in range(x):
    #         K_1,K_2=map(str,input().split())
    #         if K_2 in kinds_list.keys():
    #             for i in range(len(num_list)):
    #                 if(K_2==num_list[i][0]):
    #                     num_list[i][1]+=1
    #         else:
    #             kinds_list[K_2]=K_1
    #             num_list.append([K_2,1])
    #     result=1
    #     for i in range(len(num_list)):
    #         result*=(num_list[i][1]+1)
    #     print(result-1)

    # #백준 알고리즘 <패션왕 신해빈> 풀이
    # testcase = int(input())

    # for i in range(testcase):
    #     map = {}
    #     answer = 1
    #     n= int(input())
    #     for j in range(n):
    #         a,b = input().split()
    #         if not b in map:
    #             map[b] = 1
    #         else:
    #             map[b] +=1
    #     for k in map.keys():
    #         answer = answer * (map[k]+1)
    #     print(answer-1)

#코드 포스 Non-zero segments
    # n=int(input())
    # a=list(map(int,input().split()))
    # prefix_sum=[0]*200001
    # map={}
    # answer=0

    # map[0]=1
    # for i in range(n):
    #     prefix_sum[i]=a[i]
    #     if i !=0:
    #         prefix_sum[i]+=prefix_sum[i-1]
    #     if prefix_sum[i] in map :
    #         answer+=1
    #         map.clear()
    #         map[prefix_sum[i-1]]=1
    #     map[prefix_sum[i]]=1
    # print(answer)

#코드 포스 MEX maximizing
    # import sys

    # q,x=map(int, sys.stdin.readline().split())
    # map={}
    # mex=0
    # for _ in range(q):
    #     y= int(sys.stdin.readline())
    #     if y%x in map:
    #         if y%x + x*map[y%x] in map:
    #             map[y%x+x*map[y%x]]+=1
    #         else:
    #             map[y%x+x*map[y%x]]=1
    #         map[y%x]+=1
    #     else: 
    #         map[y%x]=1
    #     while mex in map:
    #         mex+=1
    #     print(mex)

#백준 알고리즘 <최대 힙>
    # import sys
    # import heapq
    # x=int(sys.stdin.readline())
    # heap=[]
    # for i in range(x):
    #     num=int(sys.stdin.readline())
    #     if len(heap)!=0 and num ==0:
    #         print(-(heapq.heappop(heap)))
    #     elif len(heap)==0 and num ==0:
    #         print(0)
    #     else:
    #         heapq.heappush(heap,-num)

#백준 알고리즘 <카드 정렬하기>
    # import sys
    # import heapq
    # heap=[]
    # x=int(sys.stdin.readline())
    # for i in range(x):
    #     num=int(sys.stdin.readline())
    #     heapq.heappush(heap,num)
    # answer=0
    # if len(heap)==1:
    #     answer=0
    # else:
    #     while True:
    #         if(len(heap)==2):
    #             x_1=heapq.heappop(heap)
    #             x_2=heapq.heappop(heap)
    #             answer+=(x_1+x_2)
    #             break
    #         x_1=heapq.heappop(heap)
    #         x_2=heapq.heappop(heap)
    #         x_3=x_1+x_2
    #         answer+=x_3
    #         heapq.heappush(heap,x_3)
    # print(answer)

#백준 문제 풀이 <잃어 버린 괄호> -> 하놔 이거 쉬운건데..
    # y=list(input())
    # num_list=[]
    # cal_list=[]
    # while y:
    #     for i in range(len(y)):
    #         if y[i] == '-' or '+' :
    #             tmp=y[:i-1]
    #             tmp.reverse()
    #             tmp_num=0
    #             for j in range(len(tmp)):
    #                 y.remove(tmp[j])
    #                 tmp_num+=(int(tmp[j])*(10**j))
    #             num_list.append(tmp_num)
    #             cal_list.append(y[i])
    #             y.pop()
    # print(num_list)

#백준 문제풀이 <잃어버린 괄호>
    # equtation=input().split('-')
    # answer=0

    # for i in equtation[0].split('+'):
    #     answer+=int(i)
    # for i in equtation[1:]:
    #     for j in i.split('+'):
    #         answer-=int(j)
    # print(answer)

#백준 문제풀이 <소트> ->이게 왜 실패인지 아직도 모르겠어 
    # import sys
    # x=int(sys.stdin.readline())
    # y=list(map(int,sys.stdin.readline().strip().split()))
    # cnt=int(sys.stdin.readline())
    # if x==1:
    #     print(y[0])
    # else:
    #     while cnt>0:
    #         for i in range(1,x):
    #             if(y[i-1]<y[i]):
    #                 y[i],y[i-1]=y[i-1],y[i]
    #                 cnt-=1
    #                 break
    #         for j in range(1,x):
    #             if(y[j-1]<y[j]):
    #                 break
    #             else:
    #                 if(j==x-1):
    #                     cnt=0
                    
    #     for i in range(x):
    #         print(y[i],end=" ")

#백준 문제 <소트>
    # import sys
    # N=int(sys.stdin.readline())
    # arr=list(map(int,sys.stdin.readline().strip().split()))
    # cnt=int(sys.stdin.readline())

    # while True:
    #     tof =False
    #     for i in range(N):
    #         idx=i
    #         cmp=0
    #         for j in range(N-1,i,-1):
    #             if arr[idx]<arr[j] and j-i<=cnt:
    #                 idx=j
    #                 tof=True
    #                 cmp=j-i
    #         if idx!=i:
    #             tmp=arr[idx]
    #             del arr[idx]
    #             arr.insert(i,tmp)
    #             cnt-=cmp
    #             break
    #     if tof==False:
    #         break
    # print(*arr)

#백준 문제 <회의실 배정>
    # import sys
    # num=int(sys.stdin.readline())
    # time_list=[]
    # for i in range(num):
    #     tmp1,tmp2=map(int,sys.stdin.readline().split())
    #     time_list.append([tmp1,tmp2])
    # sort_time=sorted(time_list,key=lambda x:(x[1],x[0]))
    # cnt=0
    # tmp3=0
    # for i in range(num):
    #     if(tmp3<=sort_time[i][0]):
    #         tmp3=sort_time[i][1]
    #         cnt+=1
    # print(cnt)

#백준 문제 <소트>
    # import sys
    # x= int(sys.stdin.readline())
    # y= list(map(int,sys.stdin.readline().split()))
    # csort=[0 for _ in range(10002)]
    # for i in range(x):
    #     csort[y[i]]+=1

    # answer=''
    # while True:
    #     tof=False
    #     for i in range(1001):
    #         if csort[i]:
    #             tof=True
    #             if csort[i+1]:
    #                 k-=1
    #                 for j in range(i+2,1001):
    #                     if(csort[j]):
    #                         k=j
    #                         break
    #                 if  k!=-1:
    #                     while csort[i]:
    #                         answer+=str(i)+" "
    #                         csort[i]-=1
    #                     answer+=str(i+1)+' '
    #                     csort[k]-=1
    #                     break
    #                 else:
    #                     answer+=str(i+1)+' '
    #                     csort[i+1]-=1
    #                     break
    #             else:
    #                 while(csort[i]):
    #                     answer+=str(i)+' '
    #                     csort[i]-=1
    #                 break
    #     if(tof==False):
    #         break
    # print(answer)

#백준 문제 <팩토리얼>

    # def facto(N):
    #     if(N==1):
    #         return 1
    #     else:
    #         result = N*facto(N-1)
    #         return result
    # N=int(input())

    # if(N==0):
    #     print(1)
    # else:
    #     print(facto(N))

#백준 문제 <하노이 탑>
    # N=int(input())

    # def hanoi(num,start,to,end):
    #     if num ==1:
    #         print(start, end)
    #     else:
    #         hanoi(num-1,start,end,to)
    #         print(start, end)
    #         hanoi(num-1,to,start,end)
    # print(2**N-1)
    # hanoi(N,1,2,3)

#백준 문제 <파이프 옮기기>
    # N=int(input())
    # arr=[]
    # for i in range(N):
    #     k=list(map(int,input().split()))
    #     k.append(0)
    #     arr.append(k)
    # tmp=[0]*(N+1)
    # arr.append(tmp)
    # cnt=0

    # def situation(x_1,x_2,x_3,x_4):
    #     if(x_3>=N or x_4>=N):
    #         return
    #     elif(x_3==N-1 and x_4==N-1):
    #         global cnt
    #         cnt+=1
    #         return
    #     else:
    #         if(x_3-x_1==0 and x_4-x_2==1):
    #             x_1,x_2=x_3,x_4
    #             if(arr[x_3][x_4+1]==1):
    #                 return
    #             else:
    #                 situation(x_1,x_2,x_3,x_4+1)
    #             if(arr[x_3+1][x_4+1]==1 or arr[x_3][x_4+1]==1 or arr[x_3+1][x_4]==1):
    #                 return
    #             else:
    #                 situation(x_1,x_2,x_3+1,x_4+1)
    #         elif(x_3-x_1==1 and x_4-x_2==0):
    #             x_1,x_2=x_3,x_4
    #             if(arr[x_3+1][x_4]==1):
    #                 return
    #             else:
    #                 situation(x_1,x_2,x_3+1,x_4)
    #             if(arr[x_3+1][x_4+1]==1 or arr[x_3][x_4+1]==1 or arr[x_3+1][x_4]==1):
    #                 return
    #             else:
    #                 situation(x_1,x_2,x_3+1,x_4+1)
    #         elif(x_3-x_1==1 and x_4-x_2==1):
    #             x_1,x_2=x_3,x_4
    #             if(arr[x_3+1][x_4]==1):
    #                 return
    #             else:
    #                 situation(x_1,x_2,x_3+1,x_4)
    #             if(arr[x_3][x_4+1]==1):
    #                 return
    #             else:
    #                 situation(x_1,x_2,x_3,x_4+1)
    #             if(arr[x_3+1][x_4+1]==1 or arr[x_3][x_4+1]==1 or arr[x_3+1][x_4]==1):
    #                 return
    #             else:
    #                 situation(x_1,x_2,x_3+1,x_4+1)
    # situation(0,0,0,1)
    # print(cnt)

#백준 문제풀이 <깔끔> -> 시간 초과가 나는구만?ㅋㅋ
    # def recursive(y,x,shape):
    #     global ans
    #     if y>n or x>n:
    #         return 
    #     if y==n and x==n:
    #         ans+=1
    #     if home[y][x+1]==0 and (shape==0 or shape==2):
    #         recursive(y,x+1,0)
    #     if home[y+1][x]==0 and (shape==1 or shape==2):
    #         recursive(y+1,x,1)
    #     if home[y+1][x]==0 and home[y][x+1]==0 and home[y+1][x+1]==0:
    #         recursive(y+1,x+1,2)

    # n=int(input())
    # home =[[0 for col in range(18)] for row in range(18)]
    # for i in range(1,n+1):
    #     row= list(map(int,input().split()))
    #     for j in range(1,n+1):
    #         home[i][j]=row[j-1]

    # ans=0
    # recursive(1,2,0)
    # print(ans)

#백준 문제 시간 초과 안나는 파이프 옮기기 
    # from collections import deque
    # import sys
    # input = sys.stdin.readline
    # def dfs(x, y, direction):
    #     global count
    #     if x == n - 1 and y == n - 1: count += 1
    #     if direction == 0:
    #         if y + 1 < n and s[x][y + 1] == 0: dfs(x, y + 1, 0)
    #         if x + 1 < n and y + 1 < n:
    #             if s[x][y + 1] == 0 and s[x + 1][y + 1] == 0 and s[x + 1][y] == 0:
    #                 dfs(x + 1, y + 1, 2)
    #     elif direction == 1:
    #         if x + 1 < n and s[x + 1][y] == 0: dfs(x + 1, y, 1)
    #         if x + 1 < n and y + 1 < n:
    #             if s[x][y + 1] == 0 and s[x + 1][y + 1] == 0 and s[x + 1][y] == 0:
    #                 dfs(x + 1, y + 1, 2)
    #     elif direction == 2:
    #         if y + 1 < n and s[x][y + 1] == 0: dfs(x, y + 1, 0)
    #         if x + 1 < n and s[x + 1][y] == 0: dfs(x + 1, y, 1)
    #         if x + 1 < n and y + 1 < n:
    #             if s[x][y + 1] == 0 and s[x + 1][y + 1] == 0 and s[x + 1][y] == 0:
    #                 dfs(x + 1, y + 1, 2)
    # n = int(input())
    # s = [list(map(int, input().split())) for i in range(n)]
    # count = 0
    # dfs(0, 1, 0)
    # print(count)

#백준 문제 <색종이 자르기>
    # import sys
    # N= int(sys.stdin.readline())
    # K=1
    # tmp=2
    # while tmp<N:
    #     tmp*=2
    #     K+=1
    # graph=[]
    # for i in range(N):
    #     k=list(map(int,input().split()))
    #     graph.append(k)
    # a_cnt=0 #0일때 숫자 카운트
    # b_cnt=0 #1일때 숫자 카운트
    # def check(K,y,x):
    #     tmp1=graph[y][x]
    #     for i in range(y,2**K):
    #         for j in range(x,2**K):
                
#백준 문제 <색종이 자르기>
    # import sys
    # n=int(sys.stdin.readline())

    # colortpaper=[]
    # for i in range(n):
    #     k=list(map(int,sys.stdin.readline().split()))
    #     colortpaper.append(k)
    # white=0
    # blue=0

    # def divide(x,y,n):
    #     global blue, white
    #     samecolor=colortpaper[x][y]
    #     for i in range(x, x+n):
    #         for j in range(y, y+n):
    #             if colortpaper[i][j]!=samecolor:
    #                 divide(x,y,n//2)
    #                 divide(x+n//2,y,n//2)
    #                 divide(x,y+n//2,n//2)
    #                 divide(x+n//2,y+n//2,n//2)
    #                 return
    #     if samecolor==1:
    #         blue+=1
    #         return
    #     else:
    #         white+=1
    #         return
    # divide(0,0,n)
    # print(white)
    # print(blue)

#백준 문제 <영화 감독 숌>
    # import sys
    # x=int(sys.stdin.readline())
    # arr=[]
    # for i in range(6669999):
    #     arr.append(i)
    # answer=[]
    # for i in range(len(arr)):
    #     tmp=list(str(arr[i]))
    #     for j in range(1,len(tmp)):
    #         if tmp[j]==tmp[j-1]=='6':
    #             answer.append(arr[i])
    # print(answer[x+1])

#백준 문제 <영화 감독 숌> 풀이 
    # n= int(input())
    # title=666
    # find_cnt=0
    # while(True):
    #     if "666" in str(title):
    #         find_cnt+=1
    #     if find_cnt == n:
    #             print(title)
    #             break
    #     title+=1

#백준 문제 <체스판 다시 칠하기> -> 맞았음 좀더 깔끔한 풀이?
    # import sys
    # N,M=map(int,sys.stdin.readline().split())
    # graph=[]
    # for _ in range(N):
    #     k=list(str(sys.stdin.readline().strip()))
    #     graph.append(k)
    # tmp1=N-8
    # tmp2=M-8

    # def count(x,y):
    #     sample_1=[['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]
    #     sample_2=[['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]
    #     cnt_1=0
    #     cnt_2=0
    #     for i in range(x,x+8):
    #         for j in range(y,y+8):
    #             if(graph[i][j]!=sample_1[i-x][j-y]):
    #                 cnt_1+=1
    #     for i in range(x,x+8):
    #         for j in range(y,y+8):
    #             if(graph[i][j]!=sample_2[i-x][j-y]):
    #                 cnt_2+=1
    #     cnt_3=min(cnt_1,cnt_2)
    #     return cnt_3 
    # answer=1e9    
    # for i in range(tmp1+1):
    #     for j in range(tmp2+1):
    #         answer=min(answer,count(i,j))
    # print(answer)

#백준 문제 <체스판 다시 칠하기>
    # n,m=map(int,input().split())
    # board=[]
    # answer=[]

    # for _ in range(n):
    #     board.append(input())

    # for col in range(n - 7):
    #     for row in range(m -7):
    #         countW=0
    #         countB=0
    #         for i in range(col, col+8):
    #             for j in range(row, row+8):
    #                 if (i+j)%2 ==0 :
    #                     if board[i][j]!='W':
    #                         countW +=1
    #                     if board[i][j]!='B':
    #                         countB+=1
    #                 else:
    #                     if board[i][j]!='B':
    #                         countW+=1
    #                     if board[i][j]!='W':
    #                         countB+=1
    #         answer.append(countW)
    #         answer.append(countB)
    # print(min(answer))

#백준 문제 풀이 <테트로미노>
    # n, m = map(int, input().split())
    # board = [list(map(int, input().split())) for _ in range(n)]
    # tetromino = [
    #     [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    #     [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    #     [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    #     [(0,0), (0,1), (0,2), (1,0)], 
    #     [(1,0), (1,1), (1,2), (0,2)],
    #     [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    #     [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    #     [(0,0), (1,0), (2,0), (2,1)],
    #     [(2,0), (2,1), (1,1), (0,1)],
    #     [(0,0), (0,1), (1,0), (2,0)], 
    #     [(0,0), (0,1), (1,1), (2,1)],
    #     [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    #     [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    #     [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    #     [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    #     [(1,0), (2,0), (0,1), (1,1)],
    #     [(0,0), (1,0), (1,1), (2,1)],
    #     [(1,0), (0,1), (1,1), (0,2)],
    #     [(0,0), (0,1), (1,1), (1,2)]
    # ]

    # def find(x,y):
    #     global answer
    #     for i in range(19):
    #         result=0
    #         for j in range(4):
    #             try:
    #                 next_x=x+tetromino[i][j][0]
    #                 next_y=y+tetromino[i][j][1]
    #                 result+=board[next_x][next_y]
    #             except IndexError:
    #                 continue
    #         answer = max(answer,result)
    # def solve():
    #     for i in range(n):
    #         for j in range(m):
    #             find(i,j)
    # answer=0
    # solve()
    # print(answer)

#백준 문제 < N과 M 3> 어렵네. 일단 얼른 정리하고 영화 고고 하자 
    # n,m=map(int,input().split())
    # answer=[]

    # def backTracking(depth):
    #     if depth==m:
    #         print(' '.join(map(str,answer)))
    #         return
    #     for i in range(1, n+1):
    #         answer.append(i)
    #         backTracking(depth+1)
    #         answer.pop()
    # backTracking(0)

#백준 문제 <N과 M 3> 정답 복기
    # import sys
    # n,m=map(int,sys.stdin.readline().split())
    # answer=[]
    # def solve(depth):
    #     if depth==m :
    #         print(' '.join(map(str,answer)))
    #         return
    #     for i in range(1,n+1):
    #         answer.append(i)
    #         solve(depth+1)
    #         answer.pop()
    # solve(0)

#백준 문제 < N과 M 1>
    # import sys
    # n,m=map(int,sys.stdin.readline().split())
    # answer=[]
    # def backtraking(depth):

    #     if depth == m :
    #         print(' '.join(map(str,answer)))
    #         return
    #     for i in range(1,n+1):
    #         if i not in answer:
    #             answer.append(i)
    #             backtraking(depth+1)
    #             answer.pop()
    # backtraking(0)

#백준 문제 <연산자 끼워넣기> -> 이런 형태의 문제는 한번 보고 다시 도전하자 
    # import sys
    # N=int(sys.stdin.readline())
    # num_list=list(map(int,sys.stdin.readline()))
    # cal_list=list(map(int,sys.stdin.readline()))
    # for i in range(4):
    #     if i==0:
    #         for _ in range()

#백준 문제 <연산자 끼워넣기>
    # N=int(input())
    # numArr=list(map(int,input().split()))
    # operator=list(map(int,input().split()))
    # minAns = float('Inf')
    # maxAns = float('-Inf')

    # def back_tracking(index, sum):
    #     global minAns
    #     global maxAns

    #     if index == N-1:
    #         if minAns > sum :
    #             minAns=sum
    #         if maxAns < sum :
    #             maxAns=sum
    #         return
        
    #     for i in range(4):
    #         temp=sum
    #         if operator[i]==0 :
    #             continue
    #         if i==0:
    #             sum+=numArr[index+1]
    #         elif i==1:
    #             sum-=numArr[index+1]
    #         elif i==2:
    #             sum*=numArr[index+1]
    #         else:
    #             if sum<0 :
    #                 sum= abs(sum)//numArr[index+1]*-1
    #             else:
    #                 sum=sum//numArr[index+1]
    #         operator[i] -=1
    #         back_tracking(index+1,sum)
    #         operator[i]+=1
    #         sum=temp
    # back_tracking(0,numArr[0])
    # print(maxAns)
    # print(minAns)

#백준 문제 <미로 탐색>
    # from collections import deque
    # N,M=map(int,input().split())

    # dx=[0,0,1,-1]
    # dy=[-1,1,0,0]
    # graph=[]
    # for i in range(N):
    #     k=list(str(input()))
    #     graph.append(k)
    # for i in range(N):
    #     for j in range(M):
    #         if graph[i][j]=='1':
    #             graph[i][j]=1
    #         else:
    #             graph[i][j]=0
    # queue=deque()
    # queue.append((0,0))
    # def DFS():
        
    #     while queue:
    #         x,y=queue.popleft()
    #         for i in range(4):
    #             nx=x+dx[i]
    #             ny=y+dy[i]
    #             if(nx<0 or ny<0 or nx>=N or ny>=M):
    #                 continue
    #             else:
    #                 if graph[nx][ny]==1:
    #                     graph[nx][ny]=graph[x][y]+1
    #                     queue.append((nx,ny))

    # DFS()
    # print(graph[N-1][M-1])

#백준 문제 <벽 뿌수고 탈출하기>

    # from collections import deque
    # import queue
    # N,M=map(int,input().split())
    # dx=[0,0,1,-1]
    # dy=[-1,1,0,0]
    # graph=[]
    # for i in range(N):
    #     k=list(str(input()))
    #     graph.append(k)
    # for i in range(N):
    #     for j in range(M):
    #         if graph[i][j]=='1':
    #             graph[i][j]=1
    #         else:
    #             graph[i][j]=0
    # queue=deque()
    # queue.append([0,0,0])
    # def BFS():
    #     visit =[[[0]*2 for _ in range(M)] for _ in range(N)]
    #     visit[0][0][0]=1
    #     while queue:
    #         x,y,wall=queue.popleft()
    #         if x==(N-1) and y==(M-1):
    #             return visit[x][y][wall]
    #         for i in range(4):
    #             if 0<=x+dx[i]<N and 0<=y+dy[i]<M and visit[x+dx[i]][y+dy[i]][wall]==0:
    #                 if graph[x+dx[i]][y+dy[i]]==0:
    #                     visit[x+dx[i]][y+dy[i]][wall]=visit[x][y][wall]+1
    #                     queue.append([x+dx[i],y+dy[i],wall])
    #                 if wall==0 and graph[x+dx[i]][y+dy[i]]==1:
    #                     visit[x+dx[i]][y+dy[i]][1]=visit[x][y][0]+1
    #                     queue.append([x+dx[i],y+dy[i],1])
    #     return -1
    # print(BFS())

#백준 문제 <연구소>
    # from collections import deque
    # import copy

    # def BFS():
    #     global answer
    #     queue=deque()
    #     tmp_graph=copy.deepcopy(graph)
    #     for i in range(N):
    #         for j in range(M):
    #             if(tmp_graph[i][j]==2):
    #                 queue.append((i,j))
        
    #     while queue:
    #         x,y=queue.popleft()
    #         for i in range(4):
    #             nx=x+dx[i]
    #             ny=y+dy[i]
    #             if 0<=nx<N and 0<=ny<M:
    #                 if tmp_graph[nx][ny]==0:
    #                     tmp_graph[nx][ny]=2
    #                     queue.append((nx,ny))
    #     count=0
    #     for i in range(N):
    #         for j in range(M):
    #             if(tmp_graph[i][j]==0):
    #                 count+=1

    #     answer=max(answer,count)

    # def make_wall(depth):
    #     if(depth==3):
    #         BFS()
    #         return
    #     else:
    #         for i in range(N):
    #             for j in range(M):
    #                 if graph[i][j]==0:
    #                     graph[i][j]=1
    #                     make_wall(depth+1)
    #                     graph[i][j]=0
    # N,M=map(int,input().split())
    # graph=[]
    # for i in range(N):
    #     k=list(map(int,input().split()))
    #     graph.append(k)
    # dx=[-1,1,0,0]
    # dy=[0,0,-1,1]
    # answer=0
    # make_wall(0)
    # print(answer)

#백준 문제 < 부분수열의 합 >
    # N,S=map(int,input().split())
    # array=list(map(int,input().split()))
    # answer=0
    # def dfs(idx, sum):
    #     global answer
    #     if idx>=N:
    #         return
    #     sum +=array[idx]
    #     if S==sum:
    #         answer+=1
    #     dfs(idx+1,sum-array[idx])
    #     dfs(idx+1,sum)
    # dfs(0,0)
    # print(answer)

#백준 문제 <DFS 와 BFS>
    # from collections import deque
    # import sys
    # N,M,V=map(int,sys.stdin.readline().split())
    # graph=[[] for _ in range(N+1)]
    # visit=[0]*(N+1)
    # visit_1=[0]*(N+1)
    # for i in range(M):
    #     k_1,k_2=map(int,sys.stdin.readline().split())
    #     graph[k_1].append(k_2)
    #     graph[k_2].append(k_1)
    # for i in range(N+1):
    #     graph[i].sort()
    # print(V,end=' ')
    # def DFS(V):
    #     if(visit_1[V]==1):
    #         return
    #     else:
    #         visit_1[V]=1
    #         stack=graph[V]
    #         for i in stack:
    #             if(visit_1[i]==0):
    #                 print(i,end=' ')
    #                 DFS(i)

    # queue=deque()
    # visit[V]=1
    # queue.append(graph[V])
    # def BFS():
    #     print(V, end=' ')
    #     while queue:
    #         x=queue.popleft()
    #         for i in x:
    #             if(visit[i]==0):
    #                 visit[i]=1
    #                 print(i,end=' ')
    #                 queue.append(graph[i])
    # DFS(V)
    # print()
    # BFS()

#백준 문제 <이항 계수1>
    # N,K=map(int,input().split())

    # def bino(N,K):
    #     answer=1
    #     for i in range(K):
    #         answer*=(N-i)
    #     for j in range(K):
    #         answer/=(j+1)
        
    #     return answer
    # print(int(bino(N,K)))

#백준 문제 < 이항 계수2> -> 숫자가 너무 커지기 떄문에 모듈러 연산을 사용해야 한다는점만 확인 ㅇㅋ
    # import sys
    # N,K=map(int,sys.stdin.readline().split())

    # def bino(N,K):
    #     answer=1
    #     for i in range(K):
    #         answer*=(N-i)
    #     for j in range(K):
    #         answer/=(j+1)
        
    #     return answer*10007
    # print(int(bino(N,K)))

#백준 문제 <이항 계수 2>
    # n,k=map(int, input().split())
    # dp=[[0]*1001 for _ in range(1001)]

    # for i in range(1,n+1):
    #     for j in range(0,i+1):
    #         if j==0:
    #             dp[i][j]=1
    #         elif j == i :
    #             dp[i][j]=1
    #         else:
    #             dp[i][j]=(dp[i-1][j-1] + dp[i-1][j])%10007

    # print(dp[n][k])

#백준 문제 < 소수 구하기 >
M,N=map(int,input().split())


def solo_check(K):
    if(K==1):
        return 0
    elif(K==2):
        return 1
    else:
        tmp=int(K**(1/2))
        for i in range(2,tmp+1):
            if (K%i)==0:
                return 0
        return 1

for i in range(M,N+1):
    if solo_check(i):
        print(i)
