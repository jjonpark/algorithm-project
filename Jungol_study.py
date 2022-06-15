# JUNGOL <구구단>
# while True:
#     s,e= map(int,input().split())
#     if 2<=s<=9 and 2<=e<=9:
#         break
#     else:
#         print("INPUT ERROR!")

# for i in range(1,10):
#     tmp=s
#     if s>e:
#         while tmp>=e:
#             ans=tmp*i
#             print(f"{tmp} * {i} =""{:>3}".format(ans), end= "   ")
#             tmp-=1
#     else:
#         while tmp<=e:
#             ans=tmp*i
#             print(f"{tmp} * {i} =""{:>3}".format(ans), end= "   ")
#             tmp+=1
#     print()

# JUNGOL <구구단2>
# s, e = map(int, input().split())

# tmp = s
# if s > e:
#     while tmp >= e:
#         for i in range(1, 9, 3):
#             ans = tmp*i
#             print(f"{tmp} * {i} =""{:>3}".format(ans), end="   ")
#             ans = tmp*(i+1)
#             print(f"{tmp} * {i+1} =""{:>3}".format(ans), end="   ")
#             ans = tmp*(i+2)
#             print(f"{tmp} * {i+2} =""{:>3}".format(ans), end="   ")
#             print()
#         tmp -= 1
#         print()
# else:
#     while tmp <= e:
#         for i in range(1, 9, 3):
#             ans = tmp*i
#             print(f"{tmp} * {i} =""{:>3}".format(ans), end="   ")
#             ans = tmp*(i+1)
#             print(f"{tmp} * {i+1} =""{:>3}".format(ans), end="   ")
#             ans = tmp*(i+2)
#             print(f"{tmp} * {i+2} =""{:>3}".format(ans), end="   ")
#             print()
#         tmp += 1
#         print()


# JUNGOL <숫자 사각형1>

# N, M = map(int, input().split())
# for i in range(1, N+1):
#     for j in range(M*(i-1)+1, M*i+1):
#         print(j, end=" ")
#     print()

# JUNGOL < 숫자 사각형2 >
# N,M = map(int,input().split())
# for i in range(1, N+1):
#     if i%2==1:
#         for j in range(M*(i-1)+1,M*i+1):
#             print(j, end=" ")
#     else:
#         for k in range(M*i,M*(i-1),-1):
#             print(k, end=" ")
#     print()

# JUNGOL < 숫자 사각형3 >
# N = int(input())
# for i in range(1, N+1):
#     cnt = 0
#     while cnt < N:
#         print(i+N*cnt, end=" ")
#         cnt += 1
#     print()

# JUNGOL < 문자 사각형 1 >
# print(ord("A"))
# print(ord("P"))
# print(chr(89))
# N=int(input())
# tmp=65+(N**2)-1
# if tmp>90:
#     Start_str=((tmp-91)%26)+65
# else:
#     Start_str=tmp
# for i in range(Start_str,Start_str-N,-1):
#     cnt = 0
#     while cnt < N:
#         k=i-(N*cnt)
#         while k < 65:
#             k+=26
#         print(chr(k), end=" ")
#         cnt+=1
#     print()

# JUNGOL <문자 사각형 2>
# N = int(input())
# arr = [[0]*N for i in range(N)]
# cnt = 65
# for j in range(N):
#     if j % 2 == 0:
#         for i in range(N):
#             if cnt > 90:
#                 cnt = ((cnt-91) % 26 + 65)
#             arr[i][j] = chr(cnt)
#             cnt += 1
#     else:
#         for i in range(N-1, -1, -1):
#             if cnt > 90:
#                 cnt = ((cnt-91) % 26 + 65)
#             arr[i][j] = chr(cnt)
#             cnt += 1

# for i in range(N):
#     for j in range(N):
#         print(arr[i][j], end=" ")
#     print()

# JUNGOL <문자 삼각형1> -> 문제를 꼼꼼하게 읽자!
# N = int(input())
# arr = [[0]*N for i in range(N)]
# cnt = 65
# for i in range(N):
#     for j in range(N-i-1, N):
#         if cnt > 90:
#             cnt = (cnt-91) % 26+65
#         arr[i][j] = chr(cnt)
#         cnt += 1
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 0:
#             print(" ", end=" ")
#         else:
#             print(arr[i][j], end=" ")
#     print()

# JUNGOL < 문자 삼각형 1 >

# N=int(input())
# for i in range(N):
#     v=i
#     w=N
#     for j in range(N):
#         if i+j+1>=N:
#             print(chr(v%26+25), end = ' ')
#             w-=1
#             v+=w
#         else:
#             print(' ', end=' ')
#     print()
# n=int(input())
# for i in range(n):
#     v=i
#     w=n
#     for j in range(n):
#         if i+j+1>=n:
#             print(chr(v%26+65), end=' ')
#             w-=1; v+=w
#         else:
#             print(' ', end=' ')
#     print()

# while True:
#     N = int(input())
#     if 1 <= N <= 100 and N%2!=0:
#         break
#     else:
#         print("INPUT ERROR")
#         continue
# arr = [[0]*N for i in range(N)]
# tmp= (N-1)//2
# cnt=65
# for j in range(tmp,-1,-1):
#     for i in range(j,N-j):
#         if cnt>90:
#             cnt = (cnt-91)%26 +65
#         arr[i][j]=chr(cnt)
#         cnt+=1
# for i in range(N):
#     for j in range(N):
#         if arr[i][j]==0:
#             print(" ", end=" ")
#         else:
#             print(arr[i][j], end=" ")
#     print()

# < 별 삼각형 1 >
# def tri_1(N):
#     for i in range(1,N+1):
#         for j in range(i):
#             print("*", end ="")
#         print()

# def tri_2(N):
#     for i in range(N,0,-1):
#         for j in range(i):
#             print("*", end ="")
#         print()

# def tri_3(N):
#     for i in range(1,N+1):
#         for j in range(N-i):
#             print(" ", end = "")
#         for k in range(1,2*i):
#             print("*", end ="")
#         print()


# N,M=map(int,input().split())
# arr=[1,2,3]
# if 1<=N<=100 and (M in arr):
#     if M==1:
#         tri_1(N)
#     elif M==2:
#         tri_2(N)
#     else:
#         tri_3(N)
# else:
#     print("INPUT ERROR!")

# < 별 삼각형 2>
#    def tri_1(N):
#         tmp = (N+1)//2
#         for i in range(1, tmp):
#             for j in range(i):
#                 print("*", end="")
#             print()
#         for i in range(tmp):
#             print("*", end="")
#         print()
#         for i in range(tmp-1, 0, -1):
#             for j in range(i):
#                 print("*", end="")
#             print()

#     def tri_2(N):
#         tmp = (N+1)//2
#         arr = [[0]*tmp for i in range(N)]
#         for i in range(tmp):
#             for j in range(tmp-i-1, tmp+i):
#                 arr[j][i] = "*"
#         for i in range(N):
#             for j in range(tmp):
#                 if (arr[i][j] ==0):
#                     print(" ", end="")
#                 else:
#                     print(arr[i][j], end="")
#             print()

#     def tri_3(N):
#         arr = [[0]*N for i in range(N)]
#         tmp = (N-1)//2
#         for i in range(tmp+1):
#             for j in range(i, N-i):
#                 arr[i][j] = "*"
#         for i in range(tmp+1, N):
#             for j in range((N-i)-1, i+1):
#                 arr[i][j] = "*"
#         for i in range(N):
#             for j in range(N):
#                 if (arr[i][j] ==0):
#                     print(" ", end="")
#                 else:
#                     print(arr[i][j], end="")
#             print()

#     def tri_4(N):
#         arr = [[0]*N for i in range(N)]
#         tmp = (N+1)//2
#         for i in range(tmp):
#             for j in range(i, tmp):
#                 arr[i][j] = "*"
#         for i in range(tmp, N):
#             for j in range(tmp-1, i+1):
#                 arr[i][j] = "*"
#         for i in range(N):
#             for j in range(N):
#                 if (arr[i][j] ==0):
#                     print(" ", end="")
#                 else:
#                     print(arr[i][j], end="")
#             print()
#     N,M = map(int, input().split())
#     if (N%2) == 0 or N >100 or M<1 or M>4:
#         print("INPUT ERROR!")
#     else:
#         if M ==1:
#             tri_1(N)
#         elif M ==2:
#             tri_2(N)
#         elif M ==3:
#             tri_3(N)
#         else:
#             tri_4(N)

# <별 삼각형 3>
# N = int(input())
# if (N % 2) == 0 or N > 100:
#     print("INPUT ERROR!")
# else:
#     tmp = (N-1)//2
#     arr = [[0]*(tmp+N) for i in range(N)]
#     for i in range(tmp+1):
#         for j in range(i, (i)*2+i+1):
#             arr[i][j] = "*"
#     for i in range(tmp+1, N):
#         for j in range(N-i-1, (N-i-1)*2+(N-i-1)+1):
#             arr[i][j] = "*"
#     for i in range(N):
#         for j in range(tmp+N):
#             if (arr[i][j] == 0):
#                 print(" ", end="")
#             else:
#                 print(arr[i][j], end="")
#         print()

# < 달팽이 삼각형 >
# from collections import deque
# dx = [1, 0, -1]
# dy = [1, -1, 0]
# N = int(input())
# arr = [[-1]*N for i in range(N)]
# queue = deque()
# queue.append((0, 0))
# tmp = 0
# cnt = 0
# while queue:
#     x, y = queue.pop()
#     arr[x][y] = cnt
#     nx = x+dx[tmp]
#     ny = y+dy[tmp]
#     if 0 <= nx < N and 0 <= ny <= N and arr[nx][ny] == -1:
#         queue.append((nx, ny))
#         cnt += 1
#         if(cnt > 9):
#             cnt -= 10
#     else:
#         tmp += 1
#         if tmp > 2:
#             tmp -= 3
#         nx = x+dx[tmp]
#         ny = y+dy[tmp]
#         if 0 <= nx < N and 0 <= ny <= N and arr[nx][ny] == -1:
#             queue.append((nx, ny))
#             cnt += 1
#             if(cnt > 9):
#                 cnt -= 10
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == -1:
#             print("", end=" ")
#         else:
#             print(arr[i][j], end=" ")
#     print()

# < 약수 >
# import math
# N = int(input())
# N_sqr = math.sqrt(N)
# N_sqr = int(N_sqr)
# arr = []
# for i in range(1, N_sqr+1):
#     if N % i == 0:
#         if i not in arr:
#             arr.append(i)
#         k = N//i
#         if k not in arr:
#             arr.append(k)
# arr.sort()
# for i in range(len(arr)):
#     print(arr[i], end=" ")

# < 약수와 배수 >
# import math
# n = int(input())
# arr = list(map(int, input().split()))
# m = int(input())
# arr.sort()
# k = arr[-1]
# tmp2 = k//m
# m_sqr = math.sqrt(m)
# m_sqr = int(m_sqr)
# arr_1 = []
# for i in range(1, m_sqr+1):
#     if m % i == 0:
#         if i not in arr_1:
#             arr_1.append(i)
#         q = m//i
#         if q not in arr_1:
#             arr_1.append(q)
# ans_1 = 0
# ans_2 = 0
# for i in arr:
#     if i in arr_1:
#         ans_1 += i
# for i in range(n):
#     if (arr[i] % m) == 0 and (arr[i]//m) >= 1:
#         ans_2 += arr[i]
# print(ans_1)
# print(ans_2)


# < 약수 구하기 >
# import math
# N, K = map(int, input().split())
# N_sqr = int(math.sqrt(N))
# arr = []
# for i in range(1, N_sqr+1):
#     if N % i == 0:
#         if i not in arr:
#             arr.append(i)
#         if (N//i) not in arr:
#             arr.append(N//i)
# arr.sort()
# if len(arr) < K:
#     print(0)
# else:
#     print(arr[K-1])

# < 최대공약수 와 최소공배수 >
# import math
# N, M = map(int, input().split())
# N_sqr = int(math.sqrt(N))
# arr_1 = []
# for i in range(1, N_sqr+1):
#     if N % i == 0:
#         if i not in arr_1:
#             arr_1.append(i)
#         if (N//i) not in arr_1:
#             arr_1.append(N//i)
# arr_1.sort()

# M_sqr = int(math.sqrt(M))
# arr_2 = []
# for i in range(1, M_sqr+1):
#     if M % i == 0:
#         if i not in arr_2:
#             arr_2.append(i)
#         if (M//i) not in arr_2:
#             arr_2.append(M//i)
# arr_2.sort()
# ans_1 = 0
# for i in range(len(arr_1)-1, -1, -1):
#     if arr_1[i] in arr_2:
#         ans_1 = arr_1[i]
#         break
# ans_2 = (N*M)//ans_1
# print(ans_1)
# print(ans_2)

# < 최대공약수, 최소 공배수 >
# import copy
# N = int(input())
# arr = list(map(int, input().split()))
# arr_2 = copy.deepcopy(arr)


# def GCD(a, b):
#     while b != 0:
#         r = a % b
#         a = b
#         b = r
#     return a


# tmp = arr.pop()
# while arr:
#     a_1 = arr.pop()
#     tmp = GCD(tmp, a_1)
# ans_2 = 1
# while len(arr_2) != 1:
#     b_1 = arr_2.pop()
#     b_2 = arr_2.pop()
#     ans_2 = (b_1*b_2)//(GCD(b_1, b_2))
#     arr_2.append(ans_2)
# print(f"{tmp} {ans_2}")

# < 23. 각 자리수의 역과 합 >

# while True:
#     N = list(input())
#     ans = 0
#     for i in range(len(N)):
#         N[i] = int(N[i])
#         ans += N[i]
#     if len(N) == 1 and N[0] == 0:
#         break
#     N.reverse()
#     for i in range(len(N)):
#         print(N[i], end="")
#     print(f" {ans}")

# < 24. 소수와 합성수 >
# import math
# arr = list(map(int, input().split()))


# def return_ans(A):
#     A_sqr = int(math.sqrt(A))
#     arr_1 = []
#     for i in range(1, A_sqr+1):
#         if A % i == 0:
#             if i not in arr_1:
#                 arr_1.append(i)
#             if A//i not in arr_1:
#                 arr_1.append(A//i)
#     if len(arr_1) == 2:
#         return 1
#     else:
#         return 0


# for i in arr:
#     if i == 1:
#         print("number one")
#     elif return_ans(i):
#         print("prime number")
#     else:
#         print("composite number")

# <25. 소수 >
# import math
# M = int(input())
# N = int(input())


# def return_ans(A):
#     A_sqr = int(math.sqrt(A))
#     arr_1 = []
#     for i in range(1, A_sqr+1):
#         if A % i == 0:
#             if i not in arr_1:
#                 arr_1.append(i)
#             if A//i not in arr_1:
#                 arr_1.append(A//i)
#     if len(arr_1) == 2:
#         return 1
#     else:
#         return 0


# tmp = N
# if M == 1:
#     M += 1
# ans = 0
# for i in range(M, N+1):
#     if return_ans(i):
#         if tmp >= i:
#             tmp = i
#         ans += i
# if ans == 0:
#     print("-1")
# else:
#     print(ans)
#     print(tmp)

# <26. 소수 구하기>
# import math


# def return_ans(A):
#     A_sqr = int(math.sqrt(A))
#     arr_1 = []
#     for i in range(1, A_sqr+1):
#         if A % i == 0:
#             if i not in arr_1:
#                 arr_1.append(i)
#             if A//i not in arr_1:
#                 arr_1.append(A//i)
#     if len(arr_1) == 2:
#         return 1
#     else:
#         return 0


# N = int(input())
# for i in range(1, N+1):
#     M = int(input())
#     ans_1 = M
#     ans_2 = M
#     while ans_1 < 1000000:
#         if return_ans(ans_1):
#             break
#         ans_1 += 1
#     while ans_2 > 0:
#         if return_ans(ans_2):
#             break
#         ans_2 -= 1
#     if ans_1 == 1000000:
#         plus_cnt = 1000000
#     else:
#         plus_cnt = ans_1-M
#     if ans_2 == 0:
#         minus_cnt = 1000000
#     else:
#         minus_cnt = M-ans_2

#     if plus_cnt == minus_cnt and plus_cnt!=0:
#         print(f"{ans_2} {ans_1}")
#     elif plus_cnt == minus_cnt:
#         print(ans_1)
#     elif plus_cnt < minus_cnt:
#         print(ans_1)
#     else:
#         print(ans_2)

# <27. 소수의 개수>
# import math


# def return_ans(A):
#     if A == 1:
#         return 0
#     A_sqr = int(math.sqrt(A))
#     arr_1 = []
#     for i in range(2, A_sqr+1):
#         if A % i == 0:
#             return 0
#     return 1


# M, N = map(int,input().split())
# ans = 0
# for i in range(M, N+1):
#     if return_ans(i):
#         ans += 1
# print(ans)

# <28. 이진수>
number_list = list(input())
for i in range(len(number_list)):
    number_list[i] = int(number_list[i])
cnt = len(number_list)
ans = 0
for i in range(len(number_list)):
    ans += (number_list[i]*2**(cnt-i-1))
print(ans)
