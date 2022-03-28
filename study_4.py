#백준 알고리즘 5-1번
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=list(sys.stdin.readline().split())
    # for i in range(x):
    #     y[i]=int(y[i])
    # y.sort()
    # print(f"{y[0]} {y[x-1]}")
#백준 알고리즘 5-2번
    # import sys
    # import readline

    # x=[None]*9
    # for i in range(9):
    #     x[i]=int(sys.stdin.readline())
    # print(max(x))
    # print((x.index(max(x)))+1)
    
#백준 알고리즘 5-3번
    # import sys
    # import readline
    # a=int(sys.stdin.readline())
    # b=int(sys.stdin.readline())
    # c=int(sys.stdin.readline())
    # result=a*b*c
    # y=list(map(int,str(result)))
    # for i in range(10):
    #     print(y.count(i))
#백준 알고리즘 5-4번
    # import sys
    # import readline
    # y=[None]*10
    # for i in range(10):
    #     x=int(sys.stdin.readline())
    #     y[i]=x%42
    # new_y=set(y)
    # print(len(new_y))
#백준 알고리즘 5-5번
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=list(sys.stdin.readline().split())
    # for i in range(x):
    #     y[i]=int(y[i])
    # y_max=max(y)
    # result=0
    # for i in range(x):
    #     result+=((y[i]/y_max)*100)
    # print(result/x)
#백준 알고리즘 5-6번
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # for test_case in range(1,x+1):
    #     y=list(sys.stdin.readline())
    #     cnt=1
    #     result=0
    #     for i in range(len(y)-1):
    #         if(y[i]=="X"):
    #             cnt=1
    #             continue
    #         else:
    #             result+=cnt
    #             cnt+=1
    #     print(result)

#백준 알고리즘 5-7번
    # import sys
    # import readline
    # T=int(sys.stdin.readline())
    # for test_case in range(1,T+1):
    #     x_num=list(sys.stdin.readline().split())
    #     x=int(x_num[0])
    #     y=[None]*x
    #     result=0
    #     for i in range(x):
    #         y[i]=int(x_num[i+1])
    #         result+=y[i]
    #     mid=result/x
    #     cnt=0
    #     for j in range(len(y)):
    #         if(y[j]>mid):
    #             cnt+=1
    #     print(f"{(cnt/x*100):.3f}%")
#백준 알고리즘 6-1번
    # def solve(a:list)->int:
    #     result=0
    #     for i in range(len(a)):
    #         result+=a[i]
    #     return result
#백준 알고리즘 6-2번
    # def solve(a:int):
    #     result=0
    #     for j in str(a):
    #         result+=int(j)
    #     result+=a
    #     return result

    # a_list=set()
    # b_list=set()
    # for i in range(1,10001):
    #     a_list.add(solve(i))
    #     b_list.add(i)
    # result_list=set()
    # result_list=sorted(b_list-a_list)

    # for k in result_list:
    #     print(k)
#백준 알고리즘 6-3번
    # def hansu(x:int)->int:
    #     if(len(str(x))==3):
    #         a=x//100
    #         b=(x%100)//10
    #         c=(x%100)%10
    #         if((b-a)==(c-b)):
    #             return 1
    #     if(x<100):
    #         return 1
    #     else :
    #         return 0
    # import sys
    # import readline
    # num=int(sys.stdin.readline())
    # result=0
    # for i in range(1,num+1):
    #     result+=hansu(i)
    # print(result)
#백준 알고리즘 7-1번
    # import sys 
    # import readline
    # x=input()
    # print(ord(x))

#백준 알고리즘 7-2번
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # y=list(sys.stdin.readline())

    # result=0
    # for i in range(x):
    #     result+=int(y[i])
    # print(result)

#백준 알고리즘 7-3번
    # x=list(input())
    # y=[None]*len(x)
    # for i in range(len(x)):
    #     y[i]=ord(x[i])
    # for j in range(97,123):
    #     if j not in y:
    #         print("-1",end=' ')
    #     else:
    #         print(y.index(j),end=' ')
#백준 알고리즘 7-4번
    # import sys
    # import readline
    # x=int(sys.stdin.readline())
    # for i in range(1,x+1):
    #     y=list(sys.stdin.readline())
    #     k=int(y[0])
    #     for i in range(2,len(y)-1):
    #         print(y[i]*k,end='')
    #     print("")
#백준 알고리즘 7-5번
    # import sys
    # import readline

    # x=input()
    # x_2=x.upper()
    # x_3=set(x_2)
    # x_5=list(x_3)
    # x_4=[None]*len(x_5)
    # for i in range(len(x_5)):
    #     a=x_5[i]
    #     x_4[i]=x_2.count(a)
    # cnt=0
    # for j in range(len(x_4)):
    #     if(x_4[j]==max(x_4)):
    #         cnt+=1
    #         result=x_5[j]
    #     if(cnt>=2):
    #         result="?"
    #         break
    # print(result)
#백준 알고리즘 7-6번
    # x=list(input())
    # cnt=1
    # for i in range(1,len(x)-1):
    #     if(x[i]==' '):
    #         cnt+=1
    # if(x[0]==' 'and len(x)==1):
    #     cnt=0
    # print(cnt)
#백준 알고리즘 7-7번
    # import sys
    # import readline
    # def solve(x:int) ->int:
    #     a=[None]*3
    #     a[2]=x//100
    #     a[1]=((x%100)//10)
    #     a[0]=x%10
    #     return ((a[0]*100) +(a[1]*10) + (a[2]))
    # x,y=map(int,sys.stdin.readline().split())
    # x_1=solve(x)
    # y_1=solve(y)
    # print(max(x_1,y_1))

#백준 알고리즘 7-8번
    # def number(x:str)->int:
    #     k=(ord(x)-ord("A"))
    #     result=0
    #     if(k<=2) :
    #         result=3
    #     elif(2<k<=5):
    #         result=4
    #     elif(5<k<=8):
    #         result=5
    #     elif(8<k<=11):
    #         result=6
    #     elif(11<k<=14):
    #         result=7
    #     elif(14<k<=18):
    #         result=8
    #     elif(18<k<=21):
    #         result=9
    #     elif(21<k<=25):
    #         result=10
    #     return result
    # x=list(input())
    # result=0
    # for i in range(len(x)):
    #     k=str(x[i])
    #     result+=number(k)
    # print(result)
#백준 알고리즘 7-9번 -> 실패 재도전
    # x=list(input())
    # result=0
    # for i in range(len(x)):
    #     if(x[i]==('=' or '-')):
    #         continue
    #     if(x[i]=='d'and i+2<len(x) and x[i+1]=='z' and x[i+2]=='='):
    #         continue
    #     if(x[i]=='n' and i+1<len(x) and x[i+1]=='j'):
    #         continue
    #     if(x[i]=='l' and i+1<len(x) and x[i+1]=='j'):
    #         continue
    #     else:
    #         result+=1
    # print(result)
#백준 알고리즘 7-9번 풀이
    # croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    # word=input()
    # for i in croatia:
    #     word= word.replace(i,'*')
    # print(len(word))

#백준 알고리즘 7-10번 -> 실패
    # x=int(input())
    # result=0
    # for test_case in range(1,x+1):
    #     text=list(input())
    #     if(len(text)<=2):
    #         result+=1
    #         continue
    #     y=list(set(text))
    #     result_list=[None]*len(y)
    #     for i in range(len(y)):
    #         result_list[i]=list(filter(lambda x:text[x]==y[i],range(len(text))))
    #     for i in range(len(result_list)):
    #         if(len(result_list[i])==1):
    #             continue
    #         for j in range(len(result_list[i])-1):
    #             if(int(result_list[i][j+1])-int(result_list[i][j])!=1):
    #                 break
    #     result+=1
    # print(result)  
#백준 알고리즘 7-10번 풀이
    # n=int(input())
    # group_word=0
    # for _ in range(n):
    #     word = input()
    #     error=0
    #     for index in range(len(word)-1):
    #         if word[index] != word[index+1]:
    #             new_word = word[index+1:]
    #             if new_word.count(word[index]) >0:
    #                 error+=1
    #     if error==0:
    #         group_word+=1
    # print(group_word)
#백준 알고리즘 8-1번
    # import sys
    # import readline
    # a,b,c=map(int,sys.stdin.readline().split())
    # Bep=0
    # if((c-b)<=0):
    #     Bep=-1
    # else:
    #     Bep=(a//(c-b))+1
    # print(Bep)
#백준 알고리즘 8-2번
    # x=int(input())
    # y=[1]
    # k=0
    # i=1
    # while i<1000000000:
    #     k+=1
    #     i+=(k*6)
    #     y.append(i)
    # # for i in range(10):
    # #     print(y[i])
    # for j in range(len(y)-1):
    #     if(x==1):
    #         print(1)
    #         break
    #     if(int(y[j])<x and (x<=int(y[j+1]))):
    #         print(y.index(y[j])+2)
    #         break
#백준 알고리즘 8-3번
    # x=int(input())
    # y=[1,2]
    # k=1
    # i=1
    # while i <10000000:
    #     i+=(5+4*(k-1))
    #     y.append(i)
    #     y.append(i+1)
    #     k+=1
    # # for i in range(10):
    # #     print(y[i])
    # for j in range(len(y)-1):
    #     if(x==1):
    #         result_x=1
    #         result_y=1
    #     if(int(y[j])<x and x<int(y[j+1])):
    #         result_x=1 +(x-int(y[j]))
    #         result_y=j+1 -(x-int(y[j]))
    #         if(result_y<=0):
    #             result_x=1+(int(y[j+1])-x)
    #             result_y=j+2-(int(y[j+1])-x)
    #     if(int(y[j])==x):
    #         result_x=1
    #         result_y=j+1
    # print(f"{result_x}/{result_y}")
#백준 알고리즘 8-4번
    # import sys
    # import readline
    # a,b,c=map(int,sys.stdin.readline().split())
    # k=(a-b)
    # if((c//k)-1+a>=c):
    #     result=c//k-1
    # else:
    #     result=(c//k)+1
    # print(result)
#백준 알고리즘 8-4번 풀이
    # import sys
    # import math
    # a,b,v=map(int,sys.stdin.readline().split())
    # day=(v-b)/(a-b)
    # print(math.ceil(day))
#백준 알고리즘 8-5번 
    # T=int(input())
    # for test_case in range(1,T+1):
    #     h,w,n=map(int,input().split())
    #     y=[None]*2
    #     y[0]=n%h
    #     y[1]=(n//h)+1
    #     if(y[0]==0):
    #         y[0]=h
    #         y[1]=(n//h)
    #     print(y[0]*100+y[1])
#백준 알고리즘 8-6번
    # import sys
    # import readline
    # T=int(sys.stdin.readline())
    # for i in range(1,T+1):
    #     k=int(sys.stdin.readline())
    #     n=int(sys.stdin.readline())
    #     y=[]
    #     for x in range(1,n+2):
    #         y.append(int(x))
    #     for j in range(1,k+1):
    #         for l in range(1,n+2):
    #             if(l==1):
    #                 y.append(1)
    #             else:
    #                 if(j==1):
    #                     y.append(y[n+l-1]+y[l-1])
    #                 else:
    #                     sum=int(((n+1)*j)+l-2)
    #                     y.append(y[sum]+y[sum-n])
    #     result=(n+1)*(k+1)-2
    #     print(y[result])
#백준 알고리즘 8-7번
    # x=int(input())
    # result=0
    # y=[]
    # for a in range(2000):
    #     for b in range(1001):
    #         if((3*a)+(5*b)==x):
    #             y.append(int(a+b))
    #             break
    #         elif((3*a)+(5*b)>=x):
    #             break
    # y.sort()
    # if(y==[]):
    #     print(-1)
    # else:
    #     print(y[0])
#백준 알고리즘 8-8 번 -> 갓 파이썬
    # a,b=map(int,input().split())
    # print(a+b)
#백준 알고리즘 9-1번

    # def only_num(x:int):
    #     result=True
    #     if(x==1):
    #         result= False
    #     else:
    #         for i in range(2,x):
    #             if(x%i==0):
    #                 result= False
    #                 break 
    #             else:
    #                 result=True
    #     return result

    # x=int(input())
    # y=list(input().split())
    # result_2=0
    # for i in range(x):
    #     k=int(y[i])
    #     if(only_num(k)==True):
    #         result_2+=1
    #     else :
    #         continue
    # print(result_2)
#백준 알고리즘 9-2번
    # def only_num(x:int):
    #         result=True
    #         if(x==1):
    #             result= False
    #         else:
    #             for i in range(2,x):
    #                 if(x%i==0):
    #                     result= False
    #                     break 
    #                 else:
    #                     result=True
    #         return result
    # x=int(input())
    # y=int(input())
    # result_list=[]
    # sum=0
    # for i in range(x,y+1):
    #     if(only_num(i)==True):
    #         result_list.append(i)
    #         sum+=i
    #     else:
    #         continue
    # if(result_list==[]):
    #     print(-1)
    # else:
    #     print(sum)
    #     print(min(result_list))
#백준 알고리즘 9-3번
    # def div_2(x:int):
    #     if(x==1):
    #         return 
    #     for i in range(2,x+1):
    #         if(x%i==0):
    #             print(i)
                
    #             div_2(int(x//i))
    #             break
    #         elif(i==x):
    #             print(i)
                
    # x=int(input())
    # y=div_2(x)
#백준 알고리즘 9-4번->시간 초과가 뜨네?
    # import sys
    # import readline
    # def only_num(x:int,y:int):
    #     if(y==2):
    #         print(y)
    #     for i in range(x,y+1):
    #         for j in range(2,i):
    #             if(i%j==0):
    #                 result=False
    #                 break
    #             else:
    #                 result=True
    #                 if(j==(i-1)and result==True):
    #                     print(i)
    # x,y=map(int,sys.stdin.readline().split())
    # only_num(x, y)
#백준 알고리즘 9-4번 이중 포문 말고 그냥 포문을 써서 지우자
    # def only_num(x:int):
    #     result=True
    #     for i in range(2,int(x**0.5)+1):
    #         if(x%i==0):
    #             result=False
    #             break
    #         else:
    #             result=True
            
    #     return result

    # import sys
    # import readline
    # x,y=map(int,sys.stdin.readline().split())
    # result=[]
    # for i in range(x,y+1):
    #     if(i==1):
    #         continue
    #     if(only_num(int(i))==True):
    #         result.append(i)
    #     else:
    #         continue
    # for k in range(len(result)):
    #     print(result[k])
#백준 알고리즘 9-5번 -> 시간 초과가 뜸,.
    # def only_num(x:int):
    #     result=True
    #     for i in range(2,int(x**0.5)+1):
    #         if(x%i==0 and i<x):
    #             result=False
    #             break
    #         else:
    #             result=True
    #     if(x==1):
    #         result=False
            
    #     return result

    # import sys
    # import readline
    # while True :
    #     x=int(sys.stdin.readline())
    #     if(x==0):
    #         break
    #     double_x=2*x
    #     cnt=0
    #     for i in range(x+1,double_x+1):
    #         if((only_num(i))==True):
    #             cnt+=1
    #         else:
    #             continue
    #     print(cnt)

# 백준 알고리즘 9-5번 새로운 풀이 
    # def only_num(x:int):
    #     result=True
    #     for i in range(2,int(x**0.5)+1):
    #         if(x%i==0 and i<x):
    #             result=False
    #             break
    #         else:
    #             result=True
    #     if(x==1):
    #         result=False
            
    #     return result
    # import sys
    # import readline
    # all_list=list(range(2,246912))
    # memo_list=[]
    # for i in range(len(all_list)):
    #     if(only_num(all_list[i])==True):
    #         memo_list.append(all_list[i])
    # while True:
    #     cnt=0
    #     x=int(sys.stdin.readline())
    #     if(x==0):
    #         break
    #     for k in range(len(memo_list)):
    #         if(x<memo_list[k] and memo_list[k]<=(2*x)):
    #             cnt+=1
    #     print(cnt)
#백준 알고리즘 9-6번 
    # def only_num(x:int):
    #     result=True
    #     for i in range(2,int(x**0.5)+1):
    #         if(x%i==0 and i<x):
    #             result=False
    #             break
    #         else:
    #             result=True
    #     if(x==1):
    #         result=False   
    #     return result
    # import sys
    # import readline
    # all_list=list(range(2,10000))
    # memo_list=[]
    # for i in range(len(all_list)):
    #     if(only_num(all_list[i])==True):
    #         memo_list.append(all_list[i])
    # T=int(sys.stdin.readline())
    # for test_case in range(1,T+1):
    #     x=int(sys.stdin.readline())
    #     x_2=int(x/2)
    #     result=[]    
    #     for i in range(x_2,0,-1):
    #         if(i in memo_list and (x-i) in memo_list):
    #             result.append(int (i))
    #             break
    #         else: 
    #             continue
    #     result_2=int(x-(int(result[0])))
    #     print(f"{result[0]} {result_2}")
#백준 알고리즘 9-7번
    # import sys
    # import readline
    # x,y,w,h=map(int,sys.stdin.readline().split())
    # x_1=x
    # y_1=y
    # w_1=w-x
    # h_1=h-y
    # result=min(x_1,y_1,w_1,h_1)
    # print(result)
#백준 알고리즘 9-8번
    # import sys
    # import readline
    # x_1,y_1=map(int,sys.stdin.readline().split())
    # x_2,y_2=map(int,sys.stdin.readline().split())
    # x_3,y_3=map(int,sys.stdin.readline().split())
    # x_list=[x_1,x_2,x_3]
    # y_list=[y_1,y_2,y_3]
    # for i in range(3):
    #     if(x_list.count(x_list[i])==1):
    #         result_x=x_list[i]
    #     if(y_list.count(y_list[i])==1):
    #         result_y=y_list[i]
    # print(f"{result_x} {result_y}")
#백준 알고리즘 9-9번
    # import sys
    # import readline
    # while True:
    #     x,y,z=map(int,sys.stdin.readline().split())
    #     if(x==0 and y==0 and z==0):
    #         break
    #     tri_list=[x,y,z]
    #     max_tri=max(x,y,z)
    #     tri_list.remove(max_tri)
    #     sum=0
    #     for i in range(2):
    #         sum+=(tri_list[i]**2)
    #     if(sum==(max_tri**2)):
    #         print("right")
    #     else:
    #         print("wrong")
#백준 알고리즘 9-10번
    # import math
    # pi=math.pi
    # x=int(input())
    # result_1=(x**2)*pi
    # result_2=((2*x)**2)/2
    # print(f"{result_1:.6f}")
    # print(f"{result_2:.6f}")
#백준 알고리즘 9-11번
    # import math

    # n = int(input())

    # for _ in range(n):
    #     x1, y1, r1, x2, y2, r2 = map(int, input().split())
    #     distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 거리 (원의방정식활용)
    #     if distance == 0 and r1 == r2 :  # 두 원이 동심원이고 반지름이 같을 때
    #         print(-1)
    #     elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때
    #         print(1)
    #     elif abs(r1-r2) < distance < (r1+r2) :  # 두 원이 서로다른 두 점에서 만날 때
    #         print(2)
    #     else:
    #         print(0)