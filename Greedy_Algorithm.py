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
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=[]
    # result=0
    # ans=0
    # for i in range(x):
    #     y.append(int(sys.stdin.readline()))
    # y.sort()
    # for i in range(x):
    #     result=y[i]*(x-i)
    #     if(ans<=result):
    #         ans=result
    # print(ans)
    
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

#백준 알고리즘 <신입사원> -> 답은 맞는거 같은데 시간초과... 
    # import sys
    # import readline
    # test_case=int(sys.stdin.readline())
    # for k in range(test_case):
    #     n=int(sys.stdin.readline())
    #     y=[]
    #     for i in range(n):
    #         y_1,y_2=map(int,sys.stdin.readline().split())
    #         y.append([y_1,y_2])
    #         # b=sorted(y,key=lambda x:x[0])
    #         # c=sorted(b,key=lambda x:x[1])
    #         # print(c)
    #     rank=[0]*n
    #     for i in range(n):
    #         for j in range(n):
    #             if(y[i][0]>y[j][0]and y[i][1]>y[j][1]):
    #                 rank[i]+=1
    #     rank_set=list(set(rank))
    #     rank_count=[None]*len(rank_set)
    #     for k in range(len(rank_set)):
    #         rank_count[k]=rank.count(rank_set[k])
    #     print(max(rank_count))
    
#백준 알고리즘 <신입사원> 문제풀이
    # import sys
    # t= int(input())
    # for _ in range(t):
    #     n=int(input())
    #     lst=sorted([list(map(int,sys.stdin.readline().strip().split())) for x in range(n)], key = lambda x:x[0])
    #     cnt=1
    #     min=lst[0][1]

    #     for i in range(1,n):
    #         if lst[i][1]<min:
    #             min=lst[i][1]
    #             cnt+=1
    #     print(cnt)

#백준 알고리즘 < 카드 정렬하기 > -> 출력초과?
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=[]
    # if(x==1):
    #     result=0
    # else:
    #     for i in range(x):
    #         y.append(int(sys.stdin.readline()))
    #     y.sort()
    #     result=0
    #     while len(y)>1:
    #         tmp1=y.pop(0)
    #         tmp2=y.pop(0)
    #         y.insert(0,tmp1+tmp2)
    #         result+=(tmp1 +tmp2)
    # print(result)

#백준 알고리즘 <카드 정렬하기> -> heapq 를 활용해보자 
    # import heapq
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=[]
    # if(x==1):
    #     result=0
    # else:
    #     for i in range(x):
    #         heapq.heappush(y, int(sys.stdin.readline()))
    #     result=0
    #     while len(y)>1:
    #         tmp1=heapq.heappop(y)
    #         tmp2=heapq.heappop(y)
    #         result += tmp1 + tmp2
    #         heapq.heappush(y,tmp1 + tmp2)
    # print(result)

#백준 알고리즘 <단어수학> -> 복잡하여 풀이참조함..
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # num=[9,8,7,6,5,4,3,2,1,0]
    # tmp=[]
    # for i in range(x):
    #     y=list(str(sys.stdin.readline().strip()))
    #     y.reverse()
    #     for j in range(len(y)):
    #         tmp.append([y[j],j])
    # tmp_sort=sorted(tmp,key=lambda x:x[1],reverse=True)
    # print(tmp_sort)
    # tmp2=[]
    # for i in range(len(tmp_sort)):
    #     if(tmp_sort[i][0] in tmp2):
    #         continue
    #     else:
    #         tmp2.append(tmp_sort[i][0])
    #         tmp_sort[i][1]=num.pop(0)
    # print(tmp2)
    # print(tmp_sort)

#백준 알고리즘 <단어수학> - 문제 풀이 
    # n=int(input())
    # alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # frequency=[0]*26
    # for i in range(n):
    #     enter = input()
    #     weight=1
    #     for j in enter[::-1]:
    #         frequency[alphabet.find(j)] +=weight
    #         weight *=10
    # frequency.sort(reverse=True)
    # total=0

    # for i in range(9,0,-1):
    #     total=total+(frequency[9-i]*i)
    # print(total)

#백준 알고리즘 <뒤집기>
    # import sys
    # import readline
    # x=list(str(sys.stdin.readline().strip()))
    # cnt_0=0
    # cnt_1=0
    # if(x[0]=="0"):
    #     cnt_0+=1
    # else:
    #     cnt_1+=1
    # for i in range(1,len(x)):
    #     if(x[i-1]!=x[i]):
    #         if(x[i]=="0"):
    #             cnt_0+=1
    #         else:
    #             cnt_1+=1
    # result=min(cnt_1,cnt_0)
    # print(result)

#백준 알고리즘 <A->B> -> 시간 초과?
    # import sys
    # import readline
    # import math
    # import time
    # start = time.time()
    # x,ans=map(int, sys.stdin.readline().split())
    # tmp1=ans
    # result=0
    # while x<tmp1:
    #     if(tmp1%10==1):
    #         tmp1=tmp1//10
    #         result+=1
    #     else:
    #         if(tmp1%2==0):
    #             tmp1=tmp1//2
    #             result+=1
    # if(x==tmp1):
    #     print(result+1)
    # else:
    #     print(-1)
    # end=time.time()
    # print(f"{end-start :.5f} sec")
#백준 알고리즘 <A->B> 문제풀이
    # import math
    # import time
    # start = time.time() 
    # a,b= map(int, input().split())
    # cnt=1
    # while True:
    #     if b==a:
    #         break
    #     elif(b%2!=0 and b%10 !=1 ) or (b<a):
    #         cnt=-1
    #         break
    #     else:
    #         if b%10 ==1 :
    #             b//=10
    #             cnt+=1
    #         else:
    #             b//=2
    #             cnt+=1
    # print(cnt)
    # end=time.time()
    # print(f"{end-start :.5f} sec")

#백준 알고리즘 <캠핑>
    # import sys
    # import readline
    # test_case=1
    # while True:
    #     L,P,V=map(int,sys.stdin.readline().split())
    #     if(L==0 and P==0 and V==0):
    #         break
    #     result=0
    #     tmp1=(V%P)
    #     result+=((V//P)*L)
    #     if(tmp1>=L):
    #         result+=L
    #     else:
    #         result+=tmp1
    #     print(f"Case {test_case}: {result}")
    #     test_case+=1

#백준 알고리즘 <보석 도둑> -> 시간초과...후...
    # import sys
    # import readline
    # N,K=map(int,sys.stdin.readline().split())
    # M_V=[None]*N
    # C=[None]*K
    # for i in range(N):
    #     m_1,v_1=map(int,sys.stdin.readline().split())
    #     M_V[i]=[m_1,v_1]
    # M_V_sort=sorted(M_V,key= lambda x: x[1], reverse=True)
    # result=0
    # for j in range(K):
    #     C[j]=int(sys.stdin.readline())
    # C.sort()
    # for i in range(K):
    #     for j in range(len(M_V_sort)):
    #         if(C[i]>M_V_sort[j][0]):
    #             result+=M_V_sort[j][1]
    #             M_V_sort.pop(j)
    #             break
    # print(result)

#백준 알고리즘 <보석도둑> 우선순위 큐?
    # import heapq
    # import sys
    # N,K = map(int,sys.stdin.readline().split())
    # jew=[]
    # for _ in range(N):
    #     heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))
    # bags=[]
    # for _ in range(K):
    #     bags.append(int(sys.stdin.readline()))
    # bags.sort()
    # answer=0
    # tmp_jew =[]
    # for bag in bags:
    #     while jew and bag >=jew[0][0]:
    #         heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    #     if tmp_jew:
    #         answer-=heapq.heappop(tmp_jew)
    #     elif not jew:
    #         break 
    # print(answer)

#동적 프로그래밍
#피보나치 수열
    # def fibo(x):
    #     if x==1 or x==2:
    #         return 1 
    #     return fibo(x-1) +fibo(x-2)

    # print(fibo(4))
#메모이제이션을 통한 피보나치 수열
    # d=[0]*100
    # def fibo(x):
    #     if x==1 or x==2:
    #         return 1
    #     if d[x]!=0:
    #         return d[x]
    #     d[x]= fibo(x-1) + fibo(x-2)
    #     return d[x]
    # print(fibo(99))
#바텀업 방싱을 이용한 피보나치 
    # d=[0]*100
    # d[1]=1
    # d[2]=1
    # n=99
    # for i in range(3,n+1):
    #     d[i]=d[i-1]+d[i-2]
    # print(d[n])
#창고 털기 문제 ->다이나믹 프로그래밍?
    # import sys
    # n= int(sys.stdin.readline())
    # array=list(map(int,sys.stdin.readline().strip().split()))

    # d=[0]*100
    # d[0]=array[0]
    # d[1]=max(array[0],array[1])
    # for i in range(2,n):
    #     d[i]=max(d[i-1],d[i-2]+array[i])

    # print(d[n-1])

#<삼성 아카데미> 거듭제곱
    # def jegab(x,y):
    #     if(y==1):
    #         return x
    #     return x*jegab(x,y-1)
    # T=10
    # for test_case in range(1,T+1):
    #     _=input()
    #     x,y=map(int,input().split())
    #     result=jegab(x,y)
    #     print(f"#{test_case} {result}")

#<삼성 아카데미> String
    # T=10
    # for test_case in range(1,T+1):
    #     _=input()
    #     find_st=input()
    #     st=input()
    #     result=st.count(find_st)
    #     print(f"#{test_case} {result}")

#<삼성 아카데미> 단순 2진 암호코드
    # T=int(input())
    # for test_case in range(1,T+1):
    #     N,M=map(int,input().split())
    #     y=[]
    #     y_set=[]
    #     ans_list=[0]
    #     for i in range(N):
    #         y.append(input())
    #         y_set=list((set(y)))
    #     for i in y_set:
    #         if(y.count(i)==7):
    #             ans_list[0]=list((str(i)))
    #     for j in range(M-1,0,-1):
    #         if(ans_list[0][j]=="1"):
    #             ans_list[0]=ans_list[0][j-56:j]
    #             break
    #     tmp1=[]
    #     tmp2=[0]*8
    #     for k in range(0,8):
    #         tmp1.append(ans_list[0][7*k:7*k+7])
    #     for i in range(8):
    #         if(tmp1[i]==['0','0','0','1','1','0','1']):
    #             tmp2[i]=0
    #         elif(tmp1[i]==['0','0','1','1','0','0','1']):
    #             tmp2[i]=1
    #         elif(tmp1[i]==['0','0','1','0','0','1','1']):
    #             tmp2[i]=2
    #         elif(tmp1[i]==['0','1','1','1','1','0','1']):
    #             tmp2[i]=3
    #         elif(tmp1[i]==['0','1','0','0','0','1','1']):
    #             tmp2[i]=4
    #         elif(tmp1[i]==['0','1','1','0','0','0','1']):
    #             tmp2[i]=5
    #         elif(tmp1[i]==['0','1','0','1','1','1','1']):
    #             tmp2[i]=6
    #         elif(tmp1[i]==['0','1','1','1','0','1','1']):
    #             tmp2[i]=7
    #         elif(tmp1[i]==['0','1','1','0','1','1','1']):
    #             tmp2[i]=8
    #         elif(tmp1[i]==['0','0','0','1','0','1','1']):
    #             tmp2[i]=9
    #     if(ans_list[0]==0):
    #         print(0)
    #     else:
    #         print(tmp1)
    #         print(tmp2)

#<삼성 SW expert> 단순 2진 알고리즘
    # T = int(input())

    # for t in range(1, T+1) :
    #     N, M = map(int, input().split())
    #     input_code = []
    #     for _ in range(N) :
    #         input_code.append(list(input()))

    #     num = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

    #     code = ''
    #     for i in range(N) :
    #         if '1' in input_code[i] :
    #             for j in range(M) :
    #                 code += input_code[i][j]
    #             break

    #     rev_code = code[::-1]
    #     for i in range(M) :
    #         if rev_code[i] == '1' :
    #             rev_code = rev_code[i:i+56]
    #             break
    #     code = rev_code[::-1]

    #     code_num = [code[0:7], code[7:14], code[14:21], code[21:28], code[28:35], code[35: 42], code[42:49], code[49:56]]

    #     for i in range(8) :
    #         code_num[i] = num.index(code_num[i])

    #     sum_odd = code_num[0] + code_num[2] + code_num[4] + code_num[6]
    #     sum_even = code_num[1] + code_num[3] + code_num[5]
    #     ver = (sum_odd * 3) + sum_even + code_num[7]

    #     if ver % 10 == 0 :
    #         print("#{} {}".format(t, sum(code_num)))
    #     else :
    #         print("#{} {}".format(t, 0))

#백준 알고리즘 <기타줄>
    # import sys
    # N,M=map(int,sys.stdin.readline().split())
    # line_P=[]
    # line_O=[]
    # for i in range(M):
    #     k_1,k_2=map(int,sys.stdin.readline().split())
    #     line_P.append(k_1)
    #     line_O.append(k_2)
    # answer=0
    # line_O.sort()
    # line_P.sort()
    # if((line_P[0]/6) <= line_O[0]):
    #     answer=min((N//6*line_P[0]) + ((N%6)*line_O[0]),(((N//6)+1)*line_P[0]))
    # else:
    #     answer=N*line_O[0]

    # print(answer)

#나동빈 다이나믹 프로그래밍 -> 아이디어는 맞았다! 강의에서는 어떻게 코딩했나?
    # import sys
    # x=int(sys.stdin.readline())
    # d=[0]*30
    # for i in range(x+1):
    #     if(i==0 or i==1):
    #         d[i]=0
    #         continue
    #     elif(i==2 or i==3 or i==5):
    #         d[i]=1
    #         continue
    #     else:
    #         if(i%2==0 and i%3==0 and i%5==0):
    #             d[i]=min(d[i//2],d[i//3],d[i//5],d[i-1])+1
    #             continue
    #         elif(i%2==0 and i%3==0):
    #             d[i]=min(d[i//2],d[i//3],d[i-1])+1
    #             continue
    #         elif(i%2==0 and i%5==0):
    #             d[i]=min(d[i//2],d[i//5],d[i-1])+1
    #             continue
    #         elif(i%3==0 and i%5==0):
    #             d[i]=min(d[i//3],d[i//5],d[i-1])+1
    #             continue
    #         elif(i%2==0):
    #             d[i]=min(d[i//2],d[i-1])+1
    #             continue
    #         elif(i%3==0):
    #             d[i]=min(d[i//3],d[i-1])+1
    #             continue
    #         elif(i%5==0):
    #             d[i]=min(d[i//5],d[i-1])+1
    #             continue
    #         else:
    #             d[i]=d[i-1]+1
    # print(d[x])

#나동빈 다이나믹 프로그래밍 1만들기 ->정답 풀이
    # x=int(input())
    # d=[0]*30001
    # for i in range(2,x+1):
    #     d[i]=d[i-1]+1
    #     if i%2==0:
    #         d[i]=min(d[i],d[i//2]+1)
    #     elif i%3==0:
    #         d[i]=min(d[i],d[i//3]+1)
    #     if i%5==0:
    #         d[i]=min(d[i],d[i//5]+1)
    # print(d[x])

#나동빈 다이나믹 프로그래밍 화폐만들기 
    # N,M=map(int,input().split())
    # N_list=[]
    # for i in range(N):
    #     N_list.append(int(input()))
    # d=[0]*(M+1)
    # tmp1=min(N_list)
    # tmp2=10000
    # for i in range(tmp1,M+1):
    #     for j in range(N):
    #         if(i==N_list[j]):
    #             d[i]=1
    #             break
    #         elif(d[i-N_list[j]]!=0):
    #             d[i]=min(tmp2,d[i-N_list[j]]+1)
    #             tmp2=d[i-N_list[j]]+1
    # print(d)        

#나동빈 다이나믹 프로그래밍 금광 문제 
T=int(input())
for test_case in range(1,T+1):
    N,M=map(int,input().split())
    y=list(map(int,input().split()))
    array=[]
    answer_array=[]
    for i in range(M):
        array.append(y[i::M])
        answer_array.append([0]*N)
    answer_array[0]=array[0]
    for i in range(1,M):
        for j in range(N):
            if(j==0):
                answer_array[i][j]=max(answer_array[i-1][j],answer_array[i-1][j+1])+array[i][j]
                continue
            if(j==N-1):
                answer_array[i][j]=max(answer_array[i-1][j-1],answer_array[i-1][j])+array[i][j]
                continue
            else:
                answer_array[i][j]=max(answer_array[i-1][j],answer_array[i-1][j+1],answer_array[i-1][j-1])+array[i][j]
                continue
    k=max(answer_array[M-1])
    print(k)