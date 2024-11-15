from typing import List

"""
You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.
Return [answer1,answer2].
"""

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a set of the second array
        nums2_set = set(nums2)

        # Calculate the number of indices i such that nums1[i] exists in nums2
        answer1 = sum(1 for num in nums1 if num in nums2_set)

        # Calculate the number of indices i such that nums2[i] exists in nums1
        answer2 = sum(1 for num in nums2 if num in nums1)

        return [answer1, answer2]