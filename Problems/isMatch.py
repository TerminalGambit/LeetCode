def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)

    # dp[i][j] will be True if s[:i] matches p[:j], otherwise False
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base cases
    dp[0][0] = True  # empty string matches empty pattern

    # Only '*' can match with an empty string
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    # Final answer is in dp[m][n]
    return dp[m][n]


# Example test cases
print(isMatch("aa", "a"))  # Output: False
print(isMatch("aa", "*"))  # Output: True
print(isMatch("cb", "?a"))  # Output: False