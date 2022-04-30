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
def lower_bound(s,e,d,l):
    while (e-s>0):
        m=(s+e)//2
        if(l[m]<d):
            s=m+1
        else:
            e=m
    return e
up=[]
down=[]
result=[0]*500001
n,h=map(int,input().split())
for i in range(n):
    obstacle=int(input())
    if i%2==1:
        up.append(obstacle)
    else:
        down.append(obstacle)

up.sort()
down.sort()
answer=0
mx=2147483647
for i in range(1,h+1):
    idxd=lower_bound(0,len(down),i,down)
    idxu=lower_bound(0,len(up),h-i+1,up)
    result[i]=n//2-idxd+n//2-idxu
    mx=min(mx,result[i])
for i in range(1,h+1):
    if result[i]==mx:
        answer+=1
print(mx,answer)
