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

# def maxProfit(prices):
#     import sys
#     profit = 0
#     min_price = sys.maxsize
#     for price in prices:
#         min_price = min(min_price, price)
#         profit = max(profit, price - min_price)

#     return profit

# leedCode < 234. Palindrome Linked List > -> 연결 리스트를 리스트로 전환해주는 과정이 필요하네?

# head = [1, 2, 2, 1]


# def isPalindrome(head):
#     if head == head[::-1]:
#         return True
#     else:
#         return False


# print(isPalindrome(head))

# leedCode < 234. Palindrome Linked List > 풀이
# def isPalindrome(head):
#     q = []
#     if not head:
#         return True
#     node = head
#     while node:
#         q.append(node.val)
#         node = node.next
#     if q == q[::-1]:
#         return True
#     else:
#         return False

# leedCode < 21 Merge Two sorted lists >


# def mergeTwolists(list1, list2):
#     p = []
#     if not list1:
#         return list2
#     if not list2:
#         return list1
#     node = list1
#     while node:
#         p.append(node.val)
#         node = node.next
#     node_2 = list2
#     while node_2:
#         p.append(node_2.val)
#         node_2 = node_2.next

#     p.sort()
#     return p

# 연결된 리스트는 좀 다른 방식으로 접근해야 하는거 같음

# from typing import Optional


# class Solution:
#      def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not l1 or l2 and l1.val > l2.val:
#             l1,l2 = l2, l1
#         if l1:
#             l1.next = self.mergeTwolist(l1.next,l2)
#         return l1
# list1 = [1,2,4]
# list2 = [1,3,4]
# print(Solution.mergeTwolist(Solution,list1,list2))

# class 공부
# class jss:
#     def __init__(self) -> None: #클래스에서 입력 변수가 없을시 self 을 넣어줘야 한다.
#         print("JSS 선언!")
#         self.name = input("네임:")
#         self.age = input("나이:")
#     def show(self):
#         print(f"나의 이름은{self.name} 이고, 나이는 {self.age} 입니다")
# a=jss() #init 함수는 클래스를 만드는 순간에 실행된다.
# a.show()#init 함수가 아닌 함수는 .함수명을 붙혀줌

# #jss 클래스를 상속 받아보자
# class jss2(jss):
#     def __init__(self) -> None:
#         super().__init__()
#         self.gender = input("성별 :")
#     def show(self):
#         print(f"나의 이름은{self.name} 이고, 나이는 {self.age} 이고, 성별은 {self.gender}입니다.")
# b=jss2()
# b.show()


# 링크드 리스트 클래스 구현
# class ListNode:
#     def __init__(self, val) -> None:
#         self.val = val
#         self.nex = None


# head_node = ListNode(1)
# head_node.next = ListNode(2)
# head_node.next.next = ListNode(3)

# 링크드 리스트 (인프런 강의 )

# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self) -> None:
#         init = Node('init')
#         self.head = init
#         self.tail = init

#         self.현재노드 = None
#         self.데이터수 = 0

#     def __len__(self):
#         return self.데이터수

#     def append(self, data):
#         새로운노드 = Node(data)
#         self.tail.next = 새로운노드
#         self.tail = 새로운노드
#         self.데이터수 += 1


# l = LinkedList()
# l.append(10)
# l.append(20)
# l.append(30)
# l.append(40)
# l.append(15)
# print(l.tail.next)

# class Node:
#     def __init__(self, key=None) -> None:
#         self.key = key
#         self.next = None

#     def __str__(self) -> str:  # print로 호출시 print(v.__str__())으로 동작함
#         return str(self.key)


# # 3--> 9 --> -1 링크 리스트 만들기
# a = Node(3)
# b = Node(9)
# c = Node(-1)
# a.next = b
# b.next = c

# # head node 만 있으면 모든 데이터에 접근 가능하니, head 와 size 로만 구성 된 클래스를 만들자,


# class singlyLinkedList:
#     def __init__(self) -> None:
#         self.head = None  # 빈리스트는 head 가 None 이다
#         self.size = 0

#     def __len__(self):
#         return self.size

#     def pushfront(self, key):
#         new_node = Node(key)
#         new_node.next = self.head
#         self.head = new_node
#         self.size += 1

#     def pushback(self, key):
#         V = Node(key)
#         if len(self) == 0:
#             self.head = V
#         else:
#             tail = self.head
#             while tail.next != None:
#                 tail = tail.next
#             tail.next =V
#         self.size += 1

#     def popfront(self):
#         if len(self)==0:
#             return None
#         else:
#             x=self.head
#             key = x.key
#             self.head = x.next
#             self.size -=1
#             del x
#             return key
#     def popBack(self):
#         if len(self)==0 :
#             return None
#         else:
#             prev, tail = None, self.head
#             while tail.next !=None:
#                 prev = tail
#                 tail = tail.next
#             if len(self)==1:
#                 self.head = None
#             else:
#                 prev.next= None
#             key = tail.key
#             del tail
#             size -=1
#             return key

# leetCode < 21. Merge Two Sorted Lists >
# def mergeTwoLists(self, l1, l2):
#     if not l1 or l2 and l1.val>l2.val :
#         l1, l2 = l2, l1
#     if l1:
#         l1.next = self.mergeTwoLists(l1.next, l2)
#     return l1

# leetCode < 21. Merge Two Sorted Lists >
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def mergeTwoLists(self, list1, list2):
#         dummyNode = ListNode(0)
#         runner = dummyNode
#         while list1 or list2:
#             if list1 is None:
#                 runner.next = list2
#                 list2 = list2.next
#             elif list2 in None:
#                 runner.next = list1
#                 list1 = list1.next
#             else:
#                 if list1.val < list2.val:
#                     runner.next = list1
#                     list1 = list1.next
#                 else:
#                     runner.next = list2
#                     list2 = list2.next
#             runner = runner.next
#         return dummyNode.next

# #재귀 풀이
# class Solution:
#     def mergeTwoLists(self, list1, list2):
#         if list1 is None or list2 is None:
#             return list1 or list2
#         if list1.val < list2.val:
#             list1.next = self.mergeTwoLists(list1.next, list2)
#             return list1
#         else:
#             list2.next = self.mergeTwoLists(list1, list2.next)
#             return list2
# # leedCode < 206. Reverse Linked List >
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def reverseList(self, head):
#         while self.next != None:
#             self.next.val
#             head = self.next


# 삼성 SW 커리큘럼 대로 공부 해서 취득해보자!!

# SW 커리큘럼 < 단순 2진 암호코드 > -> 복습의 개념 으로

# N,M=map(int, input().split())
# graph=[]
# for i in range(N):
#     k=list(map,str(input().split()))
#     print(k)
#     for j in range(M):
#         k[j]=int(k[j])
#     graph.append(k)

# print(graph)

# SW 커리큘럼 < 단순 2진 암호코드 > -> 풀이
# to_num = {
#     '0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
#     '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9',
# }

# for test_case in range(int(input())):
#     answer = 0
#     N, M = map(int, input().split())
#     array = [input() for _ in range(M)]
#     for i in range(N-5):
#         temp_str = ''
#         if answer:
#             break
#         for j in range(M-1, -1, -1):
#             if answer:
#                 break
#             if M-55 < 0:
#                 break
#             if array[i][j] == '0':
#                 continue
#             temp_arrray = array[i][j-55: j+1]
#             for z in range(8):
#                 temp_num = to_num.get(temp_arrray[z*7:(z+1)*7], -1)
#                 if temp_num == -1:
#                     break
#                 else:
#                     temp_str += temp_num
#                     if len(temp_str) == 8:
#                         # 밑에 4개가 자신과 같은지 확인
#                         for k in range(4):
#                             if temp_arrray != array[i+k+1][j-55:j+1]:
#                                 break
#                         else:
#                             # 결과 저장용 임시 변수
#                             check_num = 0
#                             # 홀수자리만 더하기(여기서는 0부터 시작해서 짝수)
#                             for k in range(0, 7, 2):
#                                 check_num += int(temp_str[k])
#                             # 값 3배 해주기
#                             check_num *= 3
#                             # 짝수 자리만 더하기
#                             for k in range(1, 8, 2):
#                                 check_num += int(temp_str[k])
#                             # 10 으로 나눠지는지 확인
#                             if not check_num % 10:
#                                 for k in range(8):
#                                     answer += int(temp_str[k])
#                                 break

#     print('#{} {}'.format(test_case+1, answer))

# leetCode < 21. Merge Two Sorted Lists >
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode):
#         # l1 = [] l2 =[]
#         # l1 = []  l2 = [0]
#         if l1 == None:
#             return l2
#         elif l2 == None:
#             return l1

#         # return 해야 하는 값이 노드 한개 임으로 이를 ans 으로 선언
#         ans = None
#         if l1.var <= l2.var:
#             fromPtr = l1
#             toPtr = l2
#             ans = fromPtr
#         else:
#             fromPtr = l2
#             toPtr = l1
#             ans = fromPtr
#         # fromPtr 이 None 을 가리킬때 까지 반복을 해야 한다.
#         while fromPtr != None:
#             if fromPtr.val <= toPtr.val:
#                 while fromPtr.next != None and fromPtr.next.val <= toPtr.val:
#                     fromPtr = fromPtr.next
#                 temp = fromPtr.next
#                 fromPtr.next = toPtr
#                 fromPtr = temp
#                 pass
#             else:
#                 temp = fromPtr
#                 fromPtr = toPtr
#                 toPtr = temp
#         return ans

# #leetCode < 206 Reverse Linked list >
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# # class Solution:
# #     def reverseList(self, head):
# #         #스택을 생성한후 스택에 값을 넣어주면서 후에 나중에 뒤집어줌
# #         stack = []
# #         node = head
# #         while node != None:
# #             stack.append(node)
# #             node = node.next
# #         #dummy 를 생성하여 dummy -> 5 -> 4- > 3 -> None 형태로 리스트 노드 작성
# #         dummy = ListNode(-1)
# #         node = dummy
# #         while stack:
# #             node.next = stack.pop()
# #             node = node.next
# #         node.next = None
# #         return dummy.next

# # 반복 알고리즘을 이용한 풀이
# class Solution:
#     def reverseList(self, head):
#         prev, curr = None, head
#         while curr:
#             temp_next = curr.next
#             curr.next = prev
#             prev, curr = curr, temp_next
#         return prev

# LeetCode < 2. Add Two Numbers >
# from tkinter.messagebox import NO


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         dummy = ListNode()
#         cur = dummy
#         carry = 0
#         while l1 or l2 or carry:
#             v1 = l1.val if l1 else 0
#             v2 = l2.val if l2 else 0

#             # new digit
#             val = v1 + v2 + carry
#             carry = val // 10
#             val = val % 10
#             cur.next = ListNode(val)

#             # updata ptrs
#             cur = cur.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None

#         return dummy.next

# leetCode < 20. valid Parentheses >
# class Solution:
#     def isValid(self, s):
#         stack = []
#         table = {
#             ')': '(',
#             '}': '{',
#             ']': '[',
#         }
#         for i in s:
#             if i not in table:
#                 stack.append(i)
#             elif not stack or table[i] != stack.pop():
#                 return False
#         return len(stack) == 0

#leetCode < 316 Remove Duplicate Letters >
# s="bcabc"
# stack=[]
# for i in s:
#     stack.append(i)
# ans_list = [0]*26
# for i in range(len(stack)):
#     tmp=ord(stack[i])-97
#     ans_list[tmp]+=1
# ans = []
# for j in range(len(ans_list)):
#     if ans_list[j]!=0:
#         tmp = chr(j+97)
#         ans.append(tmp)
# ans.sort()

# result = ''.join(s for s in ans)
# print(result)

#leetCode < 316. Remove Duplicate letters >
print("hello world")