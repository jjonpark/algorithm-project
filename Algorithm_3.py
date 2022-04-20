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

#백준 문제풀이 <소트>
import sys
x=int(sys.stdin.readline())
y=list(map(int,sys.stdin.readline().strip().split()))
cnt=int(sys.stdin.readline())
if x==1:
    print(y[0])
else:
    while cnt>0:
        for i in range(1,x):
            if(y[i-1]<y[i]):
                y[i],y[i-1]=y[i-1],y[i]
                cnt-=1
                break
        for j in range(1,x):
            if(y[j-1]<y[j]):
                break
            else:
                if(j==x-1):
                    cnt=0
                
    for i in range(x):
        print(y[i],end=" ")
