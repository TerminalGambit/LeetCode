from typing import List

"""
You are given an array of positive integers nums.

You have to check if it is possible to select two or more elements in the array such that the bitwise OR of the selected elements has at least one trailing zero in its binary representation.

For example, the binary representation of 5, which is "101", does not have any trailing zeros, whereas the binary representation of 4, which is "100", has two trailing zeros.

Return true if it is possible to select two or more elements whose bitwise OR has trailing zeros, return false otherwise.

"""

class Solution:
    def trailingZeroes(self, nums: List[int]) -> bool:
        # Initialize a variable to store the bitwise OR of all elements in the array
        bitwise_or = 0

        # Iterate through the elements in the array
        for num in nums:
            # Update the bitwise OR with the OR of the current element
            bitwise_or |= num

        # Check if the bitwise OR has trailing zeroes
        return bitwise_or & -bitwise_or != bitwise_or