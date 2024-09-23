from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def is_possible(t):
            total = 0
            for w in workerTimes:
                if w == 0:
                    continue
                s = (2 * t) // w
                left, right = 0, s
                max_x = 0
                while left <= right:
                    mid = (left + right) // 2
                    if mid * (mid + 1) <= s:
                        max_x = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                total += max_x
                if total >= mountainHeight:
                    return True
            return total >= mountainHeight

        low, high = 0, 1 << 60
        while low < high:
            mid = (low + high) // 2
            if is_possible(mid):
                high = mid
            else:
                low = mid + 1
        return low


# Test cases
solution = Solution()

# Example 1
mountainHeight1 = 4
workerTimes1 = [2, 1, 1]
assert solution.minNumberOfSeconds(mountainHeight1, workerTimes1) == 3, "Test case 1 failed."

# Example 2
mountainHeight2 = 10
workerTimes2 = [3, 2, 2, 4]
assert solution.minNumberOfSeconds(mountainHeight2, workerTimes2) == 12, "Test case 2 failed."

# Example 3
mountainHeight3 = 5
workerTimes3 = [1]
assert solution.minNumberOfSeconds(mountainHeight3, workerTimes3) == 15, "Test case 3 failed."

print("All test cases passed.")
