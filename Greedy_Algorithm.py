#그리디 알고리즘 공부
#백준 알고리즘 - 동전 
import sys
import readline
n,m=map(int,sys.stdin.readline().split())
y=[]
for i in range(n):
    y.append(int(sys.stdin.readline()))
y.sort(reverse=True)
result=0
for j in range(n):
    if m==0:
        break
    if(m>y[j]):
        result+=(m//y[j])
        m-=((m//y[j])*y[j])
print(result)
