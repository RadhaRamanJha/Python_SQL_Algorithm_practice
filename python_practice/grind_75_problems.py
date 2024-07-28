# Grind -75 Problems

from typing import List


class Solution:
    # 1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    # You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search_dict = dict()
        count = -1
        for num in nums:
            find_num = target-num
            count +=1
            if find_num in search_dict:
                return search_dict[find_num], count
            search_dict[num] = nums.index(num)
    
    # 2. Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    # An input string is valid if:
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.
    # Every close bracket has a corresponding open bracket of the same type.

    def isValid(self, s: str) -> bool:
        valid_paras = {')':'(','}':'{',']':'['}
        open_brackets = []
        for bracket in s:
            if bracket not in valid_paras:
                open_brackets.append(bracket)
            elif len(open_brackets) != 0:
                if valid_paras[bracket] == open_brackets[-1]:
                    open_brackets.pop()
                else:
                    return False
            elif valid_paras[bracket] not in set(open_brackets):
                return False
        if len(open_brackets) == 0:
            return True
        else:
            return False
    
    # 3. A phrase is a palindrome if, 
    # after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
    #  it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    # Given a string s, return true if it is a palindrome, or false otherwise.

    def isPalindrome(self, s: str) -> bool:
        chk_str = "".join(chr.lower() for chr in s if chr.isalnum())
        i, j = 0, len(chk_str)-1
        while i < j:
            if chk_str[i] != chk_str[j]:
                return False
            else:
                i+=1
                j-=1
        return True
    
    # 4. You are given an array prices where prices[i] is the price of a given stock on the ith day.
    # You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    # Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)-1
        current_max, max_profit, current_profit = 0, 0, 0
        for i in range(n,-1,-1):
            if prices[i] > current_max:
                current_max = prices[i]
            if prices[i] < current_max:
                current_profit = current_max - prices[i]
            if current_profit > max_profit:
                max_profit = current_profit
        return max_profit
    
#     Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#     An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    

    def isAnagram(self, s: str, t: str) -> bool:
        char_num = dict()
        for chr in s:
            if chr in char_num:
                char_num[chr] += 1
            else:
                char_num[chr] = 1
        for chr in t:
            if (chr in char_num) and (char_num[chr] !=0):
                char_num[chr] -= 1
            else:
                return False
        if sum(char_num.values()) == 0:
            return True
        else:
            return False
# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
# Iteration
    def search(self, nums: List[int], target: int) -> int:
         LL_index = 0
         UL_index = len(nums)-1
         result = -1
         while (LL_index <= UL_index) and (result == -1):
             if nums[LL_index] == target:
                 result = LL_index
             elif nums[UL_index] == target:
                 result = UL_index
             else:
                 mid = (LL_index + UL_index)//2
                 if nums[mid] < target:
                     LL_index = mid + 1
                 elif nums[mid] > target:
                     UL_index = mid - 1
                 else:
                     result = mid
         return result
    
## Recursion 
    def is_mid_target(self, low, high, target, nums):
        if low > high:
            return -1
        else:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.is_mid_target(low, mid-1, target, nums)
            else:
                return self.is_mid_target(mid+1, high, target, nums)

    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        return self.is_mid_target(low, high, target, nums)
    
# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
    
class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        while len(self.pop_stack) != 0:
            pending_item = self.pop_stack.pop()
            self.push_stack.append(pending_item)
        self.push_stack.append(x)

    def pop(self) -> int:
        
        while len(self.push_stack) != 0:
            current_item = self.push_stack.pop()
            self.pop_stack.append(current_item)
        current_poped = self.pop_stack.pop()
        return current_poped

    def peek(self) -> int:
        while len(self.push_stack) != 0:
            current_item = self.push_stack.pop()
            self.pop_stack.append(current_item)
        return self.pop_stack[-1]
        

    def empty(self) -> bool:
        if len(self.push_stack) + len(self.pop_stack) == 0:
            return True
        else:
            return False
        
## Given the root of a binary tree, invert the tree, and return its root.     
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None:
            temp = root.left
            root.left = root.right
            root.right = temp
            Solution.invertTree(self, root.left)
            Solution.invertTree(self, root.right)
        return root
    
## You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        elif list1.val > list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1