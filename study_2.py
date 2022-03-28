#while 문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

# def seq_search(a:Sequence, key : Any) -> int: #Sequence 로 잡아주면서, 튜플, 문자형, 리스트에서 검색이 가능하고, key 또한 실수 문자 모두 가능
#     i=0
#     while True:
#         if i == len(a):
#             return -1
#         if a[i] == key:
#             return i
#         i+=1
# if __name__ == '__main__':
#     num = int(input("원소수를 입력하세요. :"))
#     x=[None]*num

#     for i in range(num):
#         x[i]= int(input(f'x[{i}]: '))
    
#     ky=int(input('검색할 값을 입력하세요 : '))
#     idx=seq_search(x,ky)
#     if idx==-1:
#         print("검색하신 값을 찾지 못했습니다.")
#     else:
#         print(f"검색하신 값은 x[{idx}]에 있습니다.")
    
#첫째줄에 N(1<=N<=100,000과 K(2<=K<=100,000)가 공백을 기준으로 자연수로 주어진다. )

    # x=input().split()

    # N=int(x[0])
    # K=int(x[1])
    # count=0 
    # while True:
    #     if(N%K==0):
    #         N=int((N//K))
    #         count+=1
    #     else :
    #         N-=1
    #         count+=1
    #     if(N==1):
    #         break
    # print(f"{count}")

    # # 위의 답안에 테크닉 추가
    # n,k = map(int, input().split())
    # result = 0
    # while True:
    #     target=(n//k)*k
    #     result+=(n-target)
    #     n= target
    #     if n<k :
    #         break
    #     result +=1
    #     n//=k

#첫째 줄에 여러개의 숫자로 구성된 하나의 문자열 S가 주어진다 

    # S=list(input())
    # print(f"{S}")
    # result=1
    # for i in range(len(S)): 
    #     if(int(S[i])==0):
    #         continue
    #     else :
    #         result*=int(S[i])

    # print(f"{result}") -> 오답 임 1일 경우에 더해야 하는데 곱해버림

    # data= input()
    # result=int(data[0])

    # for i in range(1, len(data)):
    #     num=int(data[i])
    #     if num<=1 or result<=1:
    #         result+= num
    #     else:   
    #         result*=num
    # print(result)

#공포도를 가진 모험가 문제, 
    # x=int(input())
    # y=input().split()

    # y.sort()
    # result =0 
    # count=0
    # for i in range(len(y)):
    #     count +=1
    #     if count >= int(y[i]) :
    #         result +=1
    #         count =0 
    # print(result)
        
#여행가 이동 문제 
    # x=int(input())
    # y=input().split()

    # # for i in range(1,x+1):
    # #     for y in range(1,x+1):
    # #         print(f"({i},{y})" ,end="")
    # #     print()
    # result_x=1
    # result_y=1
    # count=0
    # for i in range(len(y)):
    #     if(y[i]=="R"):
    #         result_y += 1
    #         if(result_y >= x+1):
    #             result_y -=1
    #     elif(y[i]=="L"):
    #         result_y -=1
    #         if(result_y <= 0):
    #             result_y +=1
    #     if(y[i]=="U"):
    #         result_x -= 1
    #         if(result_x <= 0):
    #             result_x +=1
    #     elif(y[i]=="D"):
    #         result_x +=1
    #         if(result_x >= x+1):
    #             result_x -=1
    # print(f"{result_x} {result_y}")
# 시간에 3이 포함되는 문제 
    # x=int(input())
    # count=0
    # for i in range(x+1):
    #     if(i//10==3 or 1%10==3):
    #         count+=3600
    #         continue
    #     for j in range(60):
    #         if(j//10==3 or j%10==3):
    #             count+=60
    #             continue
    #         for k in range(60):
    #             if(k//10==3 or k%10 ==3):
    #                 count+=1
            
    # print(count) -> 왜 틀렸는지 정확히 모르겠지만 값이좀 틀림...ㅠ

# 나동빈 코딩
    # h=int(input())
    # count=0
    # for i in range(h+1):
    #     for j in range(60):
    #         for k in range(60):
    #             if '3' in str(i)+str(j)+ str(k):
    #                 count+=1

    # print(count)

#체스 나이트 이동 문제 
    # input_data=input()
    # row= int(input_data[1])
    # column=int(ord(input_data[0]))-int(ord('a'))+1

    # steps =[(2,1), (1,2), (-2,1), (-1,2), (2,-1), (1,-2), (-2,-1), (-1,-2)]
    # result=0
    # for step in steps:
    #     next_row = row + step[0]
    #     next_column = column +step[1]
    #     if next_row >=1 and next_row <=8 and next_column <=8 and next_column>=1 :
    #         result+=1
    # print(result)
#입력된 값을 알파벳과 정수 따로 구분하여 놀기 
    # data = input()
    # result=[]
    # value=0
    # for x in data: 
    #     if x.isalpha():
    #         result.append(x)
    #     else :
    #         value +=  int(x) 
    # result.sort()

    # if value !=0:
    #     result.append(str(value))
    # print(''.join(result))

#음료수 얼려먹기 
    # n,m=map(int,input().split())

    # graph=[]
    # for i in range(n):
    #     graph.append(list(map(int,input())))

    # def dfs(x,y):
    #     if x<=-1 or x>=n or y<=-1 or y>=m:
    #         return False
    #     if graph[x][y]==0:
    #         graph[x][y]=1
    #         dfs(x-1,y)
    #         dfs(x,y-1)
    #         dfs(x+1,y)
    #         dfs(x,y+1)
    #         return True
    #     return False

    # result =0
    # for i in range(n):
    #     for j in range(m):
    #         if dfs(i,j)==True:
    #             result+=1
        
    # print(result)

#최단경로 찾기 문제 
    # from collections import deque
    # n,m=map(int,input().split())

    # graph=[]
    # for i in range(n):
    #     graph.append(list((map(int,input()))))
    # dx=[0,0,1,-1]
    # dy=[1,-1,0,0]
    # def bfs(x,y):
    #     queue=deque()
    #     queue.append((x,y))
    #     while queue:
    #         x,y=queue.popleft()
    #         for i in range(4):
    #             nx=x+dx[i]
    #             ny=y+dy[i]
    #             if(nx<=-1 or nx>=n or ny<=-1 or ny>=m):
    #                 continue
    #             if(graph[nx][ny]==1):
    #                 graph[nx][ny]=graph[x][y]+1
    #                 queue.append((nx,ny))
    #             if(graph[nx][ny]==0):
    #                 continue
    #     return graph[n-1][m-1]

    # print(bfs(0,0))

#디버깅 연습
    # def std_weight(height, gender):
    #     if gender =="남자":
    #         return height*height*22
    #     else: 
    #         return height*height*21

    # height=175
    # gender = "남성"
    # weight=std_weight(height / 100, gender)
    # weight=round(weight,2)
    # print(f"키 {height}cm {gender}의 표준 체중은 {weight}입니다.")
# 그래프로 DFS BFS 탐색 결과 출력 
from collections import deque

