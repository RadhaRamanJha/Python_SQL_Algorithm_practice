# Grind -75 Problems

from typing import List

# 1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search_dict = dict()
        count = -1
        for num in nums:
            find_num = target-num
            count +=1
            if find_num in search_dict:
                return search_dict[find_num], count
            search_dict[num] = nums.index(num)