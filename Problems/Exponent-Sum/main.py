class Solution:
    def __init__(self):
        pass

    @staticmethod
    def numberOfWays(n: int, x: int) -> int:
        # Calculate the maximum base such that base^x <= n
        # We keep generating powers until base^x > n
        max_base = 1
        powers = []
        while max_base ** x <= n:
            powers.append(max_base ** x)
            max_base += 1

        # Prepare dp array where dp[i] is the number of ways to sum up to i
        dp = [0] * (n + 1)
        dp[0] = 1  # There's exactly one way to get 0: use no numbers

        # Fill the dp array using the powers
        MOD = 10 ** 9 + 7
        for power in powers:
            for i in range(n, power - 1, -1):
                dp[i] = (dp[i] + dp[i - power]) % MOD

        # Return the number of ways to form n
        return dp[n]


if __name__ == '__main__':
    print(Solution.numberOfWays(5, 3))
