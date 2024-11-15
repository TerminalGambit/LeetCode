# Dynamic programming problem in leetcode

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""
n = 4

1 1 1 1
1 1 2
1 2 1
2 1 1
2 2
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev1 = 1
        prev2 = 2

        for i in range(3, n+1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr

        return prev2

if __name__ == "__main__":
    solution = Solution()
    for i in range(1, 7):
        print(solution.climbStairs(i))