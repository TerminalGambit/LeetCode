from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        bits_associated = {}

        for num in nums:
            bit_count = bin(num).count('1')
            if bit_count not in bits_associated:
                bits_associated[bit_count] = []
            bits_associated[bit_count].append(num)

        sorted_nums = []
        for key in sorted(bits_associated.keys()):
            bits_associated[key].sort()
            sorted_nums.extend(bits_associated[key])

        return sorted_nums == sorted(nums)


if __name__ == "__main__":
    sol = Solution()
    print(sol.canSortArray([1,2,3,4,5]))
