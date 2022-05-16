# 들어가기 전 백준 문제 리마인드
# S=list(input())
# for i in range(len(S)):
#     S[i]=int(S[i])
# case_1=[]
# case_2=[]
# tmp_0=[]
# tmp_1=[]
# for i in range(len(S)):
#     if S[i]==0:
#         tmp_0.append(S[i])
#     elif S[i]==1:
#         tmp_1.append(S[i])
#     if i>0:
#         if S[i]!=S[i-1]:
#             if S[i]==1:
#                 case_1.append(tmp_0)
#                 tmp_0=[]
#             else:
#                 case_2.append(tmp_1)
#                 tmp_1=[]
# if len(tmp_0)!=0:
#     case_1.append(tmp_0)
# if len(tmp_1)!=0:
#     case_2.append(tmp_1)
# ans=min(len(case_1),len(case_2))

# print(ans)

# leetcode 문제 <Two sum>
# class Solution:
#     nums=list(map(int,input().split()))
#     target=int(input())
#     def twoSum(self, nums, target: int):
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if(nums[i]+nums[j]==target):
#                     return [i,j]
#     print(twoSum(self,nums,target))

# 파이썬에서 구조체 선언
# from dataclasses import dataclass

# @dataclass
# class product:
#     weight: int = None
#     price: float = None

# apple = product()
# apple.price = 10
# print(apple.price)

# leedcode <Valid palindrome>
# s = input()

# def solve(s):
#     s = list(s)
#     ans = []
#     for i in range(len(s)):
#         if 48 <= ord(s[i]) <= 57 or 65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122:
#             ans.append(s[i])
#     tmp = []
#     for j in range(len(ans)):
#         if 65 <= ord(ans[j]) <= 90:
#             ans[j] = chr(ord(ans[j])+32)
#         tmp.append(ans[j])
#     ans.reverse()
#     if tmp == ans:
#         return True
#     else:
#         return False

# print(solve(s))

# leetCode <344 Reverse String>
# s = list(input())
# print(s[::-1])

# leetCode <937. Reorder Data in Log Files>
    # logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
    #         "let2 own kit dig", "let3 art zero"]


    # def solve(logs):
    #     digits, letters = [], []
    #     for s in logs:
    #         if s.split()[1].isdigit():
    #             digits.append(s)
    #         else:
    #             letters.append(s)

    #     letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    #     return letters + digits

#leetCode <819. Most Common Word>
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def mostCommonWord(paragraph,banned):
    new=paragraph.split()
    print(new)

mostCommonWord(paragraph,banned)