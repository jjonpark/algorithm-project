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
s=str(input())
bomb=str(input())
left=[]
start=0
end=len(s)-1
while start<=end:
    tof=True
    left.append(s[start])
    start+=1
    if(len(left)>=len(bomb)):
        for i in range(len(bomb)):
            if bomb[i]!=left[len(left)-len(bomb)+i]:
                tof=False
                break
        if tof==True:
            for i in range(len(bomb)):
                left.pop()
if len(left)==0:
    print("FRULA")
else:
    for i in range(len(left)):
        print(left[i], end='')