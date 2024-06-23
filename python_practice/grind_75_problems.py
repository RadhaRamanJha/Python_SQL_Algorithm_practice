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