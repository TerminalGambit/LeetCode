from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # XOR all numbers to get xor of the two unique numbers
        xor = 0
        for num in nums:
            xor ^= num
        
        # Find a bit that is set (1) in xor (i.e., a bit that is different in the two unique numbers)
        # This bit can be used to differentiate between the two unique numbers
        diff_bit = xor & -xor
        
        # Initialize the two unique numbers
        num1 = 0
        num2 = 0
        
        # Separate the numbers into two groups based on the diff_bit and XOR within each group
        for num in nums:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]

# Example usage:
solution = Solution()
print(solution.singleNumber([1, 2, 1, 3, 2, 5]))  # Output: [3, 5]
