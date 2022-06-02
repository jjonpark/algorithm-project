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
N=int(input())
tmp=65+(N**2)-1
if tmp>90:
    Start_str=((tmp-91)%26)+65
else:
    Start_str=tmp
for i in range(Start_str,Start_str-N,-1):
    cnt = 0
    while cnt < N:
        k=i-(N*cnt)
        while k < 65:
            k+=26
        print(chr(k), end=" ")
        cnt+=1
    print()