#백준 알고리즘 기초 1- 스택
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=[]
    # for i in range(x):
    #     command=list(sys.stdin.readline().split())
    #     if(command[0]=='push'):
    #         y.append(command[1])
    #     if(command[0]=='top'):
    #         if(len(y)!=0):
    #             print(y[len(y)-1])
    #         else:
    #             print(-1)
    #     if(command[0]=='pop'):
    #         if(len(y)!=0):
    #             print(y.pop())
    #         else:
    #             print(-1)
    #     if(command[0]=='size'):
    #         print(len(y))
    #     if(command[0]=='empty'):
    #         if(len(y)!=0):
    #             print(0)
    #         else:
    #             print(1)

#백준 알고리즘 기초1 - 단어 뒤집기
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # for i in range(x):
    #     y=[]
    #     y=list(sys.stdin.readline().strip().split())
    #     y_reverse=y.copy()
    #     y_list=[]
    #     for i in range(len(y)):
    #         y_reverse[i]=list((y[i]))
    #         y_reverse[i].reverse()
    #         y_list.append((y_reverse[i]))
    #     for k in range(len(y_list)):
    #         for j in range(len(y_list[k])):
    #             print(y_list[k][j], end="")
    #         print(" ",end="")

#백준 알고리즘 기초1 -괄호
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # for i in range(x):
    #     y=list(sys.stdin.readline().strip())
    #     result="YES"
    #     right_count=y.count('(')
    #     left_count=y.count(')')
    #     if(right_count!=left_count):
    #         result="NO"
    #     else:
    #         cnt=0
    #         for i in range(len(y)):
    #             if(y[i]=="("):
    #                 cnt+=1
    #             else:
    #                 cnt-=1
    #                 if(cnt<0):
    #                     result="NO"
    #                     break
    #     print(result)

#백준 알고리즘 기초1 - 스택 수열 -> 어렵다. 풀이 참고후 작성
    # import sys
    # import readline

    # x= int(sys.stdin.readline())
    # stack=[]
    # answer=[]
    # flag=0
    # cur=1
    # for i in range(x):
    #     num=int(sys.stdin.readline())
    #     while cur<=num:
    #         stack.append(cur)
    #         answer.append("+")
    #         cur +=1
    #     if stack[-1]==num:
    #         stack.pop()
    #         answer.append("-")
    #     else:
    #         print("NO")
    #         flag=1
    #         break
    # if flag==0:
    #     for i in answer:
    #         print(i)

#백준 알고리즘 기초1 - 에디터 -> 시간 초과?
    # import sys
    # import readline
    # y=list(sys.stdin.readline().strip())
    # x=int(sys.stdin.readline())
    # cursor=len(y)
    # for i in range(x):
    #     command=list(sys.stdin.readline().strip().split())
    #     if(command[0]=="P"):
    #         y.insert(cursor,command[1])
    #         cursor+=1
    #     if(command[0]=="L"):
    #         if(cursor!=0):
    #             cursor-=1
    #     if(command[0]=="D"):
    #         if(cursor!=len(y)):
    #             cursor+=1
    #     if(command[0]=="B"):
    #         if(cursor!=0):
    #             del y[cursor-1]
    #             cursor-=1
    # for j in range(len(y)):
    #     print(y[j],end="")

#백준 알고리즘 기초1 - 에디터 풀이
    # import sys
    # import readline
    # s1=list(sys.stdin.readline().strip())
    # s2=[]
    # m=int(sys.stdin.readline())
    # n=len(s1)
    # for i in range(m):
    #     com=sys.stdin.readline().strip()
    #     if com[0]=="P":
    #         s1.append(com[2])
    #     elif com[0]=="L" and s1 != []:
    #         s2.append(s1.pop())
    #     elif com[0]=="D" and s2 !=[]:
    #         s1.append(s2.pop())
    #     elif com[0]=="B" and s1 !=[]:
    #         s1.pop()
    # print("".join(s1+list(reversed(s2))))

#백준 알고리즘 기초1- 큐
    # import sys
    # import readline
    # x= int(sys.stdin.readline())
    # y=[]
    # for i in range(x):
    #     k=list(sys.stdin.readline().strip().split())
    #     if(k[0]=="push"):
    #         y.append(k[1])
    #     if(k[0]=="front" and len(y)==0 ):
    #         print(-1)
    #     if(k[0]=="front" and len(y)!=0):
    #         print(y[0])
    #     if(k[0]=="pop" and len(y)==0):
    #         print(-1)
    #     if(k[0]=="pop" and len(y)!=0):
    #         print(y[0])
    #         del y[0]
    #     if(k[0]=="size"):
    #         print(len(y))
    #     if(k[0]=="empty" and len(y)!=0):
    #         print(0)
    #     if(k[0]=="empty" and len(y)==0):
    #         print(1)
    #     if(k[0]=="back" and len(y)!=0):
    #         print(y[len(y)-1])
    #     if(k[0]=="back" and len(y)==0):
    #         print(-1)

#백준 알고리즘 기초1 - 요세푸스 문제 
    # import sys
    # import readline
    # N,K=map(int,sys.stdin.readline().split())
    # y=[None]*N
    # for i in range(N): 
    #     y[i]=i+1
    # answer=[]
    # k=K-1
    # while True:
    #     answer.append(y[k])
    #     del y[k]
    #     k+=K-1
    #     if(len(y)==0):
    #         break
    #     if(k>=len(y)):
    #         k= k%len(y)
        
    # print("<",end="")
    # for i in range(len(answer)):
    #     if(i==len(answer)-1):
    #         print(f"{answer[i]}>")
    #     else:
    #         print(f"{answer[i]},",end=" ")

#백준 알고리즘 기초1- 덱
    # from collections import deque
    # import sys
    # import readline
    # N=int(sys.stdin.readline())
    # dq=deque()
    # for i in range(N):
    #     command=list(sys.stdin.readline().strip().split())
    #     if(command[0]=="push_back"):
    #         dq.append(command[1])
    #     if(command[0]=="push_front"):
    #         dq.appendleft(command[1])
    #     if(command[0]=="pop_front" and len(dq)==0):
    #         print(-1)        
    #     if(command[0]=="pop_front" and len(dq)!=0):
    #         print(dq.popleft())
    #     if(command[0]=="pop_back" and len(dq)==0):
    #         print(-1)
    #     if(command[0]=="pop_back" and len(dq)!=0):
    #         print(dq.pop())
    #     if(command[0]=="front" and len(dq)!=0):
    #         print(dq[0])
    #     if(command[0]=="front" and len(dq)==0):
    #         print(-1)
    #     if(command[0]=="back" and len(dq)!=0):
    #         print(dq[len(dq)-1])
    #     if(command[0]=="back" and len(dq)==0):
    #         print(-1)
    #     if(command[0]=="size"):
    #         print(len(dq))
    #     if(command[0]=="empty" and len(dq)!=0):
    #         print(0)
    #     if(command[0]=="empty" and len(dq)==0):
    #         print(1)

#백준 알고리즘 자료구조1 (연습) 단어 뒤집기2 -> 내일 다시 풀어보자
    # import sys

    # s = list(map(str, sys.stdin.readline().strip()))

    # res = ""
    # word = ""
    # reverse = True

    # for c in s:

    #     if c == '<':
    #         reverse = False
    #         res += word
    #         word = c

    #     elif c == '>':
    #         reverse = True
    #         res += (word + '>')
    #         word = ""

    #     elif c == ' ':
    #         res += word + c
    #         word = ""

    #     elif reverse:
    #         word = c + word

    #     else:
    #         word += c

    # res += word
    # print(res)

#백준 알고리즘 자료구조1 (연습) - 쇠막대기
    # import sys
    # import readline
    # x=list(sys.stdin.readline().strip())
    # cnt=1
    # if(x[1]==")"):
    #         cnt-=1
    # result=0
    # for i in range(1,len(x)-1):
    #     if(x[i]=="(" and x[i+1]!=")"):
    #         cnt+=1
    #     if(x[i]=="(" and x[i+1]==")"):
    #         result+=cnt
    #     if(x[i-1]!="(" and x[i]==")"):
    #         result+=1
    #         cnt-=1
    # print(result+1)

#백준 알고리즘 자료구조1 (연습) - 오큰수 -> 시간초과?
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=list(map(int,sys.stdin.readline().strip().split()))
    # Nge=[None]*len(y)
    # for i in range(x):
    #     if(i==(x-1)):
    #         Nge[i]=-1
    #         break
    #     for j in range(i+1,x):
    #         if(y[i]<y[j]):
    #             Nge[i]=y[j]
    #             break
    #         else: 
    #             Nge[i]=-1
    # for _ in Nge:
    #     print(_ , end=" ")

#떡 가져가는 문제(이코테 강의)
    # import sys
    # import readline
    # n,m=map(int,sys.stdin.readline().split())
    # y=list(map(int,sys.stdin.readline().strip().split()))
    # start=0
    # end=max(y)
    # result=0
    # while (start<=end):
    #     total =0
    #     mid = (start+end)//2
    #     for x in y:
    #         if x> mid:
    #             total+=x-mid
    #     if total <m:
    #         end=mid-1
    #     else:
    #         result=mid
    #         start=mid+1
    # print(result)

# 정렬된 배열의 특정 수의 개수 구하기 : 이코테 강의 
    # import sys
    # import readline
    # from bisect import bisect_right,bisect_left
    # n,m=map(int,sys.stdin.readline().split())
    # y=list(map(int, sys.stdin.readline().strip().split()))

    # def count_by_range(array, left_value, right_value):
    #     right_index = bisect_right(array, right_value)
    #     left_index = bisect_left(array, left_value)
    #     return right_index-left_index

    # count=count_by_range(y,m,m)
    # if count==0:
    #     print(-1)
    # else:
    #     print(count)

#백준 알고리즘 자료구조1 (연습) - 오큰수 시간초과가 떠있어서 재풀이..
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=list(map(int,sys.stdin.readline().strip().split()))
    # answer=[-1]*x
    # stack=[0]
    # for i in range(1,x):
    #     while stack and y[stack[-1]]<y[i]:
    #         answer[stack.pop()]=y[i]
    #     stack.append(i)
    # print(*answer)

#백준 알고리즘 자료구조1 (연습) - 오등큰수
#-> 그리디 알고리즘 공부로 넘어가자!