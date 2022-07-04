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
# number_list = list(input())
# for i in range(len(number_list)):
#     number_list[i] = int(number_list[i])
# cnt = len(number_list)
# ans = 0
# for i in range(len(number_list)):
#     ans += (number_list[i]*2**(cnt-i-1))
# print(ans)

# <29. 10진수를 2,8,16 진수로>

# def return_arr(N, B):
#     tmp = N
#     arr = []
#     while tmp != 0:
#         k = tmp % B
#         if k == 10:
#             k = "A"
#         elif k == 11:
#             k = "B"
#         elif k == 12:
#             k = "C"
#         elif k == 13:
#             k = "D"
#         elif k == 14:
#             k = "E"
#         elif k == 15:
#             k = "F"
#         arr.append(k)
#         tmp = tmp//B
#     arr.reverse()
#     return arr


# N, B = map(int, input().split())
# ans = return_arr(N, B)
# for i in range(len(ans)):
#     print(ans[i], end="")

# <31. 문자열 찾기>

# arr = list(input())

# ans_1 = 0
# ans_2 = 0
# for i in range(0, len(arr)-1):
#     if arr[i] == "K" and arr[i+1] == "O" and arr[i+2] == "I":
#         ans_1 += 1
#     if arr[i] == "I" and arr[i+1] == "O" and arr[i+2] == "I":
#         ans_2 += 1
# print(ans_1)
# print(ans_2)

# <32. 암호풀기 >

# print(ord("a"))
# print(ord("z"))
# print(ord("A"))
# print(ord("Z"))
# print(ord(" "))
# arr_list = list(input())
# arr_2_list = []
# for i in range(len(arr_list)):
#     k = chr(ord(arr_list[i])-32)
#     arr_2_list.append(k)
# ans_list = list(input())
# rans_list = []
# for i in range(len(ans_list)):
#     tmp1 = ord(ans_list[i])
#     if 97 <= tmp1 <= 122:
#         rans_list.append(arr_list[tmp1-97])
#     elif tmp1 == 32:
#         rans_list.append(" ")
#     elif 65 <= tmp1 <= 90:
#         rans_list.append(arr_2_list[tmp1-65])
# for i in range(len(rans_list)):
#     print(rans_list[i], end="")

# <33. 단어집합2>
# ans_arr = []
# while True:
#     arr = list(input().split())
#     if arr[0] == "END":
#         break
#     for i in arr:
#         if i not in ans_arr:
#             ans_arr.append(i)
#     for j in ans_arr:
#         print(j, end=" ")
#     print()

# <34. 단어 세기>
# while True:
#     arr = list(input().split())
#     ans = []
#     if arr[0] == "END":
#         break
#     for i in arr:
#         if i not in ans:
#             ans.append(i)
#     ans.sort()
#     for i in range(len(ans)):
#         tmp = 0
#         for j in range(len(arr)):
#             if ans[i] == arr[j]:
#                 tmp += 1
#         print(f"{ans[i]} : {tmp}")


# < 35. 변장 >
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     arr = {}
#     list_a = []
#     for i in range(N):
#         wear = list(input().split())
#         if wear[1] in arr:
#             arr[wear[1]] += 1
#         else:
#             arr[wear[1]] = 1
#         if wear[1] not in list_a:
#             list_a.append(wear[1])
#     ans = 1
#     for i in list_a:
#         ans *= ((arr[i])+1)
#     print(ans-1)

# < 36. 색종이 > -> 겹치는거 생각해서 풀면 답이 없다
# N = int(input())
# arr = []
# for i in range(N):
#     k_1, k_2 = map(int, input().split())
#     arr.append([k_1, k_2])

# minus_ans = 0
# for i in range(len(arr)-1):
#     for j in range(i+1, len(arr)):
#         tmp_x = 0
#         tmp_y = 0
#         tmp_1 = abs(arr[i][0]-arr[j][0])
#         tmp_2 = abs(arr[i][1]-arr[j][1])
#         if tmp_1 < 10 and tmp_2 < 10:
#             tmp_x = (min(arr[i][0], arr[j][0])+10)-(max(arr[i][0], arr[j][0]))
#             tmp_y = (min(arr[i][1], arr[j][1])+10)-(max(arr[i][1], arr[j][1]))
#             minus_ans += (tmp_x*tmp_y)

# ans = (100*N)-(minus_ans)
# print(ans)


# < 36. 색종이 > 풀이 참고
# arr = [[0]*100 for i in range(100)]
# N = int(input())
# for i in range(N):
#     x, y = map(int, input().split())
#     for k in range(y, y+10):
#         for j in range(x, x+10):
#             arr[k][j] = 1
# ans = 0
# for i in range(100):
#     for j in range(100):
#         if arr[i][j] == 1:
#             ans += 1
# print(ans)

# < 37. 색종이(중) >

# arr = [[0]*100 for i in range(100)]
# N = int(input())
# for i in range(N):
#     x, y = map(int, input().split())
#     for k in range(y, y+10):
#         for j in range(x, x+10):
#             arr[k][j] = 1

# for i in range(100):
#     for j in range(100):
#         print(arr[i][j],end="")
#     print()
# ans = 0
# for i in range(1, 99):
#     for j in range(1, 99):
#         if arr[i][j] == 1 :
#             if arr[i][j+1]==0 or arr[i][j-1]==0 or arr[i+1][j]==0 or arr[i-1][j]==0:
#                 ans += 1
# for i in range(100):
#     if arr[i][0] == 1:
#         ans += 1
#     if arr[i][99] == 1:
#         ans += 1
# for j in range(100):
#     if arr[0][j] == 1:
#         ans += 1
#     if arr[99][j] == 1:
#         ans += 1

# print(ans)


# <37. 색종이 중>

# n = int(input())

# MAP = [[False for _ in range(101)] for _ in range(101)]

# for _ in range(n):
#     st_j, st_i = map(int, input().split())

#     for i in range(st_i, st_i + 10):
#         for j in range(st_j, st_j + 10):
#             MAP[i][j] = True

# total = 0
# for j in range(1, 101):
#     for i in range(1, 101):
#         if MAP[i][j] != MAP[i - 1][j]:
#             total += 1

# for i in range(1, 101):
#     for j in range(1, 101):
#         if MAP[i][j] != MAP[i][j - 1]:
#             total += 1

# print(total)

# <38. 떡 먹는 호랑이 >
# arr = [1, 1]
# for i in range(2, 31):
#     arr.append(arr[i-1]+arr[i-2])

# D, K = map(int, input().split())
# b = D-2
# a = D-3
# x = 1
# tmp = K
# a = arr[a]
# b = arr[b]
# while tmp != 0:
#     x += 1
#     tmp = K-(x*a)
#     tmp = (tmp % b)
# print(x)
# print((K-x*a)//b)

# <41. 오목 >
# arr = []
# arr.append([0]*20)
# for i in range(19):
#     k = [0]
#     tmp=list(map(int, input().split()))
#     tmp.append(0)
#     k.append(tmp)
#     arr.append(k)
# arr.append([0]*20)


# def omok(r, c):
#     cnt = 0
#     for i in range(c, 20):
#         if arr[r][i] != arr[r][c]:
#             break
#         cnt += 1
#     if cnt == 5 and (arr[r][c-1] != arr[r][c]):
#         return 1
#     cnt = 0
#     for i in range(r, 20):
#         if arr[i][c] != arr[r][c]:
#             break
#         cnt += 1
#     if cnt == 5 and (arr[r-1][c] != arr[r][c]):
#         return 1
#     cnt = 0
#     for i in range(r, 20):
#         for j in range(c, 20):
#             if arr[i][j] != arr[r][c]:
#                 break
#             cnt += 1
#     if cnt == 5 and (arr[r-1][c-1] != arr[r][c]):
#         return 1
#     cnt = 0
#     for i in range(r, -1, -1):
#         for j in range(c, 20):
#             if arr[i][j] != arr[r][c]:
#                 break
#             cnt == 1
#     if cnt == 5 and arr[r+1][c-1] != arr[r][c]:
#         return 1
#     return 0


# tmp = 0
# for i in range(1,20):
#     for j in range(1,20):
#         if arr[i][j] != 0:
#             if (omok(i, j)):
#                 print(arr[i][j])
#                 print(f"{i} {j}")
#                 tmp = 1
# if tmp == 0:
#     print("0")

# <40. 오목 >
# import sys
# input = sys.stdin.readline

# board = []
# for i in range(19):
#     board.append(list(map(int, input().split())))

# # → ↓ ↘ ↗
# dx = [0, 1, 1, -1]
# dy = [1, 0, 1, 1]

# for x in range(19):
#     for y in range(19):
#         if board[x][y] != 0:
#             focus = board[x][y]

#             for i in range(4):
#                 cnt = 1
#                 nx = x + dx[i]
#                 ny = y + dy[i]

#                 while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == focus:
#                     cnt += 1

#                     if cnt == 5:
#                         # 육목 체크
#                         if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == focus:
#                             break
#                         if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == focus:
#                             break
#                         # 육목이 아니면 성공한거니까 종료
#                         print(focus)
#                         print(x + 1, y + 1)
#                         sys.exit(0)

#                     nx += dx[i]
#                     ny += dy[i]

# print(0)

# < 41. 빙고 >
# arr = []
# for i in range(5):
#     k = list(map(int, input().split()))
#     arr.append(k)


# def check_list(a):
#     cnt = 0
#     for i in range(5):
#         if a[i][0] == 1 and a[i][1] == 1 and a[i][2] == 1 and a[i][3] == 1 and a[i][4] == 1:
#             cnt += 1
#     for j in range(5):
#         if a[0][j] == 1 and a[1][j] == 1 and a[2][j] == 1 and a[3][j] == 1 and a[4][j] == 1:
#             cnt += 1
#     if a[0][0] == 1 and a[1][1] == 1 and a[2][2] == 1 and a[3][3] == 1 and a[4][4] == 1:
#         cnt += 1
#     if a[0][4] == 1 and a[1][3] == 1 and a[2][2] == 1 and a[3][1] == 1 and a[4][0] == 1:
#         cnt += 1
#     if cnt >= 3:
#         return 1
#     return 0


# ans_list = [[0]*5 for i in range(5)]
# arr_list = []
# for i in range(5):
#     k = list(map(int, input().split()))
#     arr_list.append(k)
# tmp = 0
# c = 0
# b = 0
# d = 0
# for i in range(5):
#     for j in range(5):
#         for x in range(5):
#             for y in range(5):
#                 if arr[x][y] == arr_list[i][j]:
#                     ans_list[x][y] = 1
#                     tmp += 1
#                     if check_list(ans_list) == 1:
#                         c = 1
#                         break
#             if c == 1:
#                 b = 1
#                 break
#         if b == 1:
#             d = 1
#             break
#     if d == 1:
#         break

# print(tmp)

# <42. 숫자 야구 >
# from collections import deque

# arr = []
# for i in range(1, 10):
#     for j in range(1, 10):
#         for k in range(1, 10):
#             if i != j and j != k and i != k:
#                 arr.append([i, j, k])


# def check_1(N, S, B):
#     global arr
#     N_list = list(str(N))
#     for i in range(3):
#         N_list[i] = int(N_list[i])
#     for i in range(len(arr)):
#         in_S = 0
#         in_B = 0
#         if arr[i] != 0:
#             for k in range(3):
#                 if N_list[k] == arr[i][k]:
#                     in_S += 1
#                 for j in range(3):
#                     if k != j:
#                         if N_list[k] == arr[i][j]:
#                             in_B += 1
#         if in_B == B and in_S == S:
#             continue
#         else:
#             arr[i] = 0


# M = int(input())

# for i in range(M):
#     N, S, B = map(int, input().split())
#     check_1(N, S, B)
# ans = 0
# for i in range(len(arr)):
#     if arr[i] != 0:
#         ans += 1
# print(ans)

# <43. 연속 부분 합 찾기 >
# N = int(input())
# arr = list(map(int, input().split()))

# ans_arr = []
# for i in range(N):
#     if i == 0:
#         ans_arr.append(arr[0])
#     else:
#         tmp = ans_arr[i-1]+arr[i]
#         if tmp <= arr[i]:
#             ans_arr.append(arr[i])
#         else:
#             ans_arr.append(tmp)
# ans = -100000000
# for i in range(len(ans_arr)):
#     if ans <= ans_arr[i]:
#         ans = ans_arr[i]

# print(ans)

# <44. stack >

# N = int(input())
# arr = []
# for i in range(N):
#     k = list(input().split())
#     if k[0] == "i":
#         arr.append(int(k[1]))
#     elif k[0] == "c":
#         print(len(arr))
#     elif k[0] == "o":
#         if len(arr) == 0:
#             print("empty")
#         else:
#             print(arr.pop())

# <45. queue>
# from collections import deque

# N = int(input())
# arr = deque()

# for i in range(N):
#     k = list(input().split())
#     if k[0] == "i":
#         arr.append(int(k[1]))
#     if k[0] == "c":
#         print(len(arr))
#     if k[0] == "o":
#         if (len(arr) == 0):
#             print("empty")
#         else:
#             print(arr.popleft())

# < 46. Bad hair day> --> 시간 초과

# N = int(input())
# arr = []
# for i in range(N):
#     k = int(input())
#     arr.append(k)
# ans = 0
# for i in range(N-1):
#     for j in range(i+1, N):
#         if arr[i] <= arr[j]:
#             break
#         else:
#             ans += 1
# print(ans)

# <46. bad hair day> //강의 참고
# N = int(input())
# arr = []
# ans = 0
# for i in range(N):
#     k = int(input())
#     while True:
#         if len(arr) != 0 and arr[-1] <= k:
#             arr.pop()
#         else:
#             arr.append(k)
#             ans += (len(arr)-1)
#             break
# print(ans)

# <47. 쇠 막대기 > #풀었던건데 기억이 안남
# arr = list(input())
# tmp = 0
# ans = 0
# for i in range(len(arr)-1):
#     if arr[i] == "(" and arr[i+1] == ")":
#         ans += tmp
#     elif arr[i] == ")" and arr[i-1] != "(":
#         ans += 1
#     if arr[i] == "(":
#         tmp += 1
#     elif arr[i] == ")":
#         tmp -= 1
# print(ans+1)

# <48. 팩토리얼 >

# N = int(input())


# def factorial(N):
#     tmp = N
#     ans = 1
#     while tmp >= 1:
#         if tmp == 1:
#             print("1! = 1")
#             tmp -= 1
#         else:
#             print(f"{tmp}! = {tmp} * {tmp-1}!")
#             ans *= tmp
#             tmp -= 1
#     print(ans)


# factorial(N)

# <49. 하노이탑>

# def move_disk(N, start_peg, end_peg):
#     print(f"{N} : {start_peg} -> {end_peg}")


# def hanoi(N, start_peg, end_peg, other_peg):
#     if N == 1:
#         move_disk(1, start_peg, end_peg)
#     else:
#         hanoi(N-1, start_peg, other_peg, end_peg)
#         move_disk(N, start_peg, end_peg)
#         hanoi(N-1, other_peg, end_peg, start_peg)


# N = int(input())
# hanoi(N, 1, 3, 2)

# <50. 주사위 던지기1 >
# N, M = map(int, input().split())
# arr = [0]*(N)


# def case_1(num):
#     if (num >= N):
#         print(f"{arr[0]} {arr[1]} {arr[2]}")
#         return
#     else:
#         for i in range(1, 7):
#             arr[num] = i
#             case_1(num+1)


# arr = [0]*(N)


# def case_2(num):
#     if (num >= N):
#         print(f"{arr[0]} {arr[1]} {arr[2]}")
#         return
#     else:
#         for i in range(1, 7):
#             if num >= 1:
#                 if arr[num-1] <= i:
#                     arr[num] = i
#                     case_2(num+1)
#             else:
#                 arr[num] = i
#                 case_2(num+1)


# arr = [0]*(N)


# def case_3(num):
#     if (num >= N):
#         print(f"{arr[0]} {arr[1]} {arr[2]}")
#         return
#     else:
#         for i in range(1, 7):
#             if num >= 1:
#                 if i not in arr:
#                     arr[num] = i
#                     case_3(num+1)
#             else:
#                 arr[num] = i
#                 case_3(num+1)


# if M == 1:
#     case_1(0)
# elif M == 2:
#     case_2(0)
# elif M == 3:
#     case_3(0)

# <51. 주사위 던지기2 >
# N, M = map(int, input().split())
# arr = [0]*N


# def answer(A):
#     if A >= N:
#         ans = 0
#         for i in range(N):
#             ans += arr[i]
#         if ans == M:
#             for i in range(N):
#                 print(f"{arr[i]}", end=" ")
#             print()
#         return
#     else:
#         for j in range(1, 7):
#             arr[A] = j
#             answer(A+1)


# answer(0)

# <52. 숫자 고르기 >
# N = int(input())
# arr = []
# for i in range(N):
#     k = int(input())
#     arr.append(k)
# visit = []
# ans_list = []


# def find_answer(A, B):
#     global visit
#     global ans_list
#     if (A == B):
#         visit = []
#         ans_list.append(A)
#         return 1
#     elif B in visit:
#         visit = []
#         return 0
#     else:
#         visit.append(B)
#         return find_answer(A, arr[B-1])


# ans = 0
# for i in range(N):
#     if find_answer(i+1, arr[i]):
#         ans += 1
#         continue
# print()
# print(ans)
# for i in range(len(ans_list)):
#     print(ans_list[i])

# <53. 숫자 고르기>
# N = int(input())
# M = int(input())
# visit = [0]*(N+1)
# arr = [[0]*(N+1) for i in range(N+1)]
# for i in range(M):
#     a_1, a_2, a_3 = map(int, input().split())
#     visit[a_1] = 1
#     arr[a_1][a_2] = a_3
# basic_list=[]
# for i in range(N+1):
#     if visit[i]==0:
#         basic_list.append(i)


# def find_answer(A, B):
#     global visit
#     if A in basic_list:
#         visit[A] += B
#         return
#     else:
#         for i in range(N+1):
#             if arr[A][i] != 0:
#                 find_answer(i, arr[A][i]*B)

# find_answer(N,1)
# for i in range(1,N+1):
#     if i in basic_list:
#         print(f"{i} {visit[i]}")

# <54.로또 번호>
# from itertools import combinations

# arr = list(input().split())
# N = int(arr[0])
# arr_list = arr[1:]
# for i in range(N):
#     arr_list[i] = int(arr_list[i])

# ans = list(combinations(arr_list, 6))
# for i in range(len(ans)):
#     for j in range(6):
#         print(f"{ans[i][j]}", end=" ")
#     print()

# <56. 회의실 배정>
# N = int(input())
# arr = [[] for i in range(N)]
# for i in range(N):
#     a_1, a_2, a_3 = map(int, input().split())
#     arr[i] = [a_1, a_2, a_3]

# arr.sort(key=lambda x: x[2])
# ans = [arr[0][0]]
# tmp = arr[0][2]
# for i in range(1, N):
#     if tmp <= arr[i][1]:
#         tmp = arr[i][2]
#         ans.append(arr[i][0])
# print(len(ans))
# for i in range(len(ans)):
#     print(ans[i], end=" ")

# <57. 동전 자판기>
# #include<cstdio>
# #include<algorithm>
# using namespace std;
# int arr[10],n,l[10],cost[10]={0,500,100,50,10,5,1};
# int main()
# {
#     int i,cnt=0,sum=0;
#     scanf("%d",&n);
#     for(i=1;i<=6;i++){
#         scanf("%d",&arr[i]);
#         sum+=arr[i]*cost[i];
#     }
#     n=sum-n;
#     for(i=1;i<=6;i++){
#         int temp=min(arr[i],n/cost[i]);
#         n-=cost[i]*temp;
#         l[i]+=temp;
#     }
#     for(i=1;i<=6;i++) cnt+=arr[i]-l[i];
#     printf("%d\n",cnt);
#     for(i=1;i<=6;i++){
#         printf("%d ",arr[i]-l[i]);
#     }
#     return 0;
# }

# <58. 색종이 만들기 >
# N = int(input())
# graph = []
# for i in range(N):
#     k = list(input().split())
#     for j in range(N):
#         k[j] = int(k[j])
#     graph.append(k)
# ans_1 = 0
# ans_0 = 0


# def check(N, a, b):
#     global ans_1
#     global ans_0
#     if N == 1:
#         if graph[a][b] == 1:
#             ans_1 += 1
#             return
#         else:
#             ans_0 += 1
#             return
#     else:
#         tmp = graph[a][b]
#         for i in range(a,a+N):
#             for j in range(b,b+N):
#                 if tmp != graph[i][j]:
#                     check(N//2, a, b)
#                     check(N//2, a+N//2, b)
#                     check(N//2, a, b+N//2)
#                     check(N//2, a+N//2, b+N//2)
#                     return
#         if tmp == 1:
#             ans_1 += 1
#             return
#         else:
#             ans_0 += 1
#             return
# check(N,0,0)
# print(ans_0)
# print(ans_1)

# <59. 이진탐색>
# def binarySearch(A, low, high, target):
#     while low <= high:
#         mid = (low+high)//2
#         if A[mid] == target:
#             return mid
#         elif A[mid] > target:
#             high = mid-1
#         else:
#             low = mid+1
#     return -1


# N = int(input())
# arr = list(input().split())
# for i in range(N):
#     arr[i] = int(arr[i])

# M = int(input())
# find_list = list(input().split())
# for i in range(M):
#     find_list[i] = int(find_list[i])

# for i in range(M):
#     print(binarySearch(arr, 0, N, find_list[i]),end=" ")

# <60.제곱수 출력>
# import math
# N, M = map(int, input().split())


# def answer(N, M):
#     if M == 1:
#         return N
#     elif M == 0:
#         return 1
#     return N*answer(N, M-1)


# answer = int(math.pow(N, M))
# print(int(answer % 20091024))

# <61 N queens >
N = int(input())
graph = [[0]*N for i in range(N)]
col = [0]*(N+1)
left = [0]*(2*N)
right = [0]*(2*N)

ans = 0


def DFS(R):
    global ans, col, left, right
    if R >= N:
        ans += 1
        return
    for c in range(N):
        if col[c] == 0 and left[R+c] == 0 and right[R-c+N] == 0:
            col[c] = 1
            left[R+c] = 1
            right[R-c+N] = 1
            DFS(R+1)
            col[c] = 0
            left[R+c] = 0
            right[R-c+N] = 0


DFS(0)

print(ans)