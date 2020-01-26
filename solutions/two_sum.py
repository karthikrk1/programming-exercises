"""
Problem Description: https://leetcode.com/problems/two-sum/

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import List
import datetime


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        start = datetime.datetime.now()
        d = {}
        for index, value in enumerate(nums):
            if (target-value) in d:
                end = datetime.datetime.now()
                print("two_sum for input: {}, target: {}, took: {}s".format(nums, target, (end-start).total_seconds()))
                return [d[target-value], index]
            d[value] = index


output = Solution.two_sum([2, 7, 11, 15], 9)
print(output)
