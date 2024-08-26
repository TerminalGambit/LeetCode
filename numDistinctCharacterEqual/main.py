# from typing import List

"""
You are given two 0-indexed strings word1 and word2.

A move consists of choosing two indices i and j such that 0 <= i < word1.length and 0 <= j < word2.length and swapping word1[i] with word2[j].

Return true if it is possible to get the number of distinct characters in word1 and word2 to be equal with exactly one move. Return false otherwise.

Example 1:

Input: word1 = "ac", word2 = "b"
Output: false
Explanation: Any pair of swaps would yield two distinct characters in the first string, and one in the second string.
Example 2:

Input: word1 = "abcc", word2 = "aab"
Output: true
Explanation: We swap index 2 of the first string with index 0 of the second string. The resulting strings are word1 = "abac" and word2 = "cab", which both have 3 distinct characters.
Example 3:

Input: word1 = "abcde", word2 = "fghij"
Output: true
Explanation: Both resulting strings will have 5 distinct characters, regardless of which indices we swap.
"""

class Solution:

    def canSwap(self, word1: str, word2: str) -> bool:
        # Create a dictionary to store the count of each character in word1
        char_count = {}
        for char in word1:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Iterate through word2 and check if we can swap a character to make the number of distinct characters in both strings equal
        for char in word2:
            if char in char_count:
                if char_count[char] == 1:
                    del char_count[char]
                else:
                    char_count[char] -= 1
                return True
        return False

    def isItPossible(self, word1: str, word2: str) -> bool:
        # Count the number of distinct characters in each string
        distinct_chars1 = len(set(word1))
        distinct_chars2 = len(set(word2))

        # If the number of distinct characters in both strings is the same, return True
        if distinct_chars1 == distinct_chars2:
            return True

        # If the number of distinct characters in both strings differs by more than 1, return False
        if abs(distinct_chars1 - distinct_chars2) > 1:
            return False

        # If the number of distinct characters in both strings differs by exactly 1, check if we can swap a character to make them equal
        if distinct_chars1 > distinct_chars2:
            return self.canSwap(word1, word2)
        else:
            return self.canSwap(word2, word1)


if __name__ == '__main__':
    solution = Solution()
    assert solution.isItPossible("ac", "b") is False
    assert solution.isItPossible("abcc", "aab") is True
    assert solution.isItPossible("abcde", "fghij") is True


