from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        val_min = float('inf')
        val_mid = float('inf')
        for num in nums:
            if num <= val_min:
                val_min = num
            elif num <= val_mid:
                val_mid = num
            else:
                return True
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.increasingTriplet([1,2,3,4,5]))
    print(sol.increasingTriplet([5,4,3,2,1]))
    print(sol.increasingTriplet([2,1,5,0,4,6]))
    print(sol.increasingTriplet([1,2,1,2,1,2,1,2,1,2]))