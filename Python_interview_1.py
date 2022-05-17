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

# leetCode <819. Most Common Word>
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]

# def mostCommonWord(paragraph,banned):
#     new=paragraph.split()
#     for i in range(len(new)):
#         k=list(i)
#         tmp=[]
#         for j in range(len(k)):
#             if k[j].isalnum():
#                 tmp.append(k[j])
#         new[i]=


# mostCommonWord(paragraph,banned)

# leetCode <819. Most Common Word> ->풀이 -> 머리 아파 포기?
# def mostCommonWord(paragraph,banned):
#     words=[word for word in re.sub(r'[^\W]',' ',paragraph).lower().split() if word not in banned]

# leefCode < 49. Group Anagrams >
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# ans = []
# for i in range(len(strs)):
#     tmp = list(strs[i])
#     tmp.sort()
#     if tmp not in ans:
#         ans.append(tmp)
# real = [[]for _ in range(len(ans))]
# for i in range(len(strs)):
#     tmp = list(strs[i])
#     tmp.sort()
#     for j in range(len(ans)):
#         if tmp == ans[j]:
#             real[j].append(strs[i])
#             break
# print(real)


# leedCode < 5. Longest Palindromic Substring > -> 이론은 맞는데 시간 초과 남
# s = "ac"
# s_list = list(s)

# def check(list):
#     flag = True
#     for i in range(len(list)//2):
#         if list[i] != list[len(list)-i-1]:
#             flag = False
#             return flag
#     return flag

# ans = []
# for i in range(len(s_list)-1):
#     for j in range(i, len(s_list)):
#         if check(s_list[i:j+1]):
#             ans.append(s_list[i:j+1])
# ans_sort = sorted(ans, key=len, reverse=True)
# real = "".join(ans_sort[0])
# print(real)

# leedCode < 5. Longest Palindromic Substring > -> 풀이
# s = "babad"

# print(s[::-1])

# def longestPalindrome(self, s: str) -> str:
#     def expand(left, right) -> str:
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return s[left+1:right]

#     if len(s) < 2 or s == s[::-1]:
#         return s
#     result = ''
#     for i in range(len(s)-1):
#         result = max(result, expand(i, i+1), expand(i, i+2), key=len)
#     return result

# leedCode < 42. Trapping Rain Water >

# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# tmp = height[0]
# tmp_1 = 0
# basket = 0
# max_value = max(height)
# for i in range(1, len(height)):
#     if tmp <= height[i]:
#         tmp = height[i]
#         tmp_1 += basket
#         basket = 0
#     else:
#         basket += (tmp-height[i])
#     if tmp == max_value:
#         break
# tmp = height[0]
# basket = 0
# for j in range(len(height)-1, 0, -1):
#     if tmp <= height[j]:
#         tmp = height[j]
#         tmp_1 += basket
#         basket = 0
#     else:
#         basket += (tmp-height[j])
#     if tmp == max_value:
#         break
# print(tmp_1)

# leedCode < 42. Trapping Rain Water > 풀이
# def solve(height):
#     if not height:
#         return 0
#     volume = 0
#     left, right = 0, len(height)-1
#     left_max, right_max = height[left], height[right]
#     while left < right:
#         left_max, right_max = max(height[left], left_max), max(
#             height[right], right_max)
#         if left_max <= right_max:
#             volume += left_max-height[left]
#             left += 1
#         else:
#             volume += right_max-height[right]
#             right -= 1
#     return volume

# leetCode < 15. 3Sum > -> 완전 탐색으로 하면 시간 초과 및 에러
# nums = [0,0,0,0]


# def threeSum(nums):
#     from itertools import combinations
#     ans = []
#     if len(nums) < 3:
#         return ans
#     elif len(nums) == 3:
#         sum = 0
#         for i in range(3):
#             sum += nums[i]
#         if sum == 0:
#             return nums
#         else:
#             return ans
#     ans_list = list(combinations(nums, 3))
#     for i in range(len(ans_list)):
#         sum = 0
#         for j in range(3):
#             sum += ans_list[i][j]
#         if sum == 0:
#             tmp=sorted(list(ans_list[i]))
#             if tmp not in ans:
#                 ans.append(tmp)
#     if len(ans)==1:
#         return ans[0]
#     else:
#         return ans


# print(threeSum(nums))

# leetCode < 15. 3Sum > ->투포인터를 이용한 풀이!

# def ThreeSum(nums):
#     results = []
#     nums.sort()

#     for i in range(len(nums)-2):
#         if i > 0 and nums[i] == nums[i-1]:
#             continue
#         left, right = i+1, len(nums)-1
#         while left < right:
#             sum = nums[i]+nums[left]+nums[right]
#             if sum < 0:
#                 left += 1
#             elif sum > 0:
#                 right -= 1
#             else:
#                 results.append([nums[i], nums[left], nums[right]])
#                 while left < right and nums[left] == nums[left+1]:
#                     left += 1
#                 while left < right and nums[right] == nums[right-1]:
#                     right -= 1
#                 left += 1
#                 right -= 1
#     return results

# leedCode < 561. Array Partition I >
# nums = [6,2,6,5,1,2]

# def arrayPairSum(nums):
#     nums.sort()
#     sum=0
#     for i in range(0,len(nums),2):
#         sum+=nums[i]
#     return sum

# print(arrayPairSum(nums))

# leetCode < 238. Product of Array Except Self > -> 시간초과..?
# nums = [1, 2, 3, 4]


# def productExceptSelf(nums):
#     ans = []
#     for i in range(len(nums)):
#         sum = 1
#         for j in range(len(nums)):
#             if j != i:
#                 sum *= nums[j]
#         ans.append(sum)
#     return ans


# print(productExceptSelf(nums))

# leetCode < 238. Product of Array Except Self >
# def productExceptSelf(nums):
#     out = []
#     p = 1
#     for i in range(0, len(nums)):
#         out.append(p)
#         p = p*nums[i]
#     p = 1
#     for i in range(len(nums)-1, -1, -1):
#         out[i] = out[i]*p
#         p = p*nums[i]
#     return out

# leedCode < 121. Best Time to Buy and Sell Stock > ->시간초과
# prices = [7, 6, 4, 3, 1]


# def maxProfit(prices):
#     max_ans = 0
#     for i in range(len(prices)-1):
#         for j in range(i, len(prices)):
#             if prices[j] > prices[i]:
#                 tmp = prices[j]-prices[i]
#                 if max_ans < tmp:
#                     max_ans = tmp
#     return max_ans


# print(maxProfit(prices))

# 재풀이
# prices = [7,1,5,3,6,4]


# def maxProfit(prices):
#     max_ans=0
#     from collections import deque
#     queue=deque()
#     queue.append(prices)
#     print(queue.popleft())

# maxProfit(prices)

# leedCode < 121. Best Time to Buy and Sell Stock > ->풀이

def maxProfit(prices):
    import sys
    profit = 0
    min_price = sys.maxsize
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit
