from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # if the length of the list is 0, return 0
        if len(nums) == 0:
            return 0
        
        # if the length of the list is 1, return 1
        if len(nums) == 1:
            return 1
        
        # if the length of the list is greater than 1, return the length of the longest increasing subsequence
        # use a new list to store the length of the longest increasing subsequence
        # use a for loop to iterate through the list
        # use a nested for loop to iterate through the list
        # if the current element is greater than the previous element, increment the length of the longest increasing subsequence
        # return the length of the longest increasing subsequence
        length = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    length[i] = max(length[i], length[j] + 1)
        return max(length)