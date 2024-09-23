from typing import List

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n = len(word1)
        total_substrings = 0
        left = 0

        counts_word2 = [0] * 26
        for c in word2:
            counts_word2[ord(c) - ord('a')] += 1

        counts_window = [0] * 26

        def is_valid(counts_window, counts_word2):
            for i in range(26):
                if counts_word2[i] > counts_window[i]:
                    return False
            return True

        for right in range(n):
            c = word1[right]
            counts_window[ord(c) - ord('a')] += 1
            while is_valid(counts_window, counts_word2):
                total_substrings += n - right
                counts_window[ord(word1[left]) - ord('a')] -= 1
                left += 1

        return total_substrings


# Test cases
solution = Solution()

# Example 1
word1_1 = "bcca"
word2_1 = "abc"
assert solution.validSubstringCount(word1_1, word2_1) == 1, "Test case 1 failed."

# Example 2
word1_2 = "abcabc"
word2_2 = "abc"
assert solution.validSubstringCount(word1_2, word2_2) == 10, "Test case 2 failed."

# Example 3
word1_3 = "abcabc"
word2_3 = "aaabc"
assert solution.validSubstringCount(word1_3, word2_3) == 0, "Test case 3 failed."

print("All test cases passed.")
