from typing import List

class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned_set = set(bannedWords)
        banned_count = 0

        for word in message:
            if word in banned_set:
                banned_count += 1
            if banned_count >= 2:
                return True

        return False


# Test cases
solution = Solution()

# Example 1
message1 = ["hello", "world", "leetcode"]
bannedWords1 = ["world", "hello"]
assert solution.reportSpam(message1, bannedWords1) is True, "Test case 1 failed."

# Example 2
message2 = ["hello", "programming", "fun"]
bannedWords2 = ["world", "programming", "leetcode"]
assert solution.reportSpam(message2, bannedWords2) is False, "Test case 2 failed."

print("All test cases passed.")
