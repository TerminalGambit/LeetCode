class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        freq_s = [0] * 26
        freq_t = [0] * 26

        for char in s:
            freq_s[int(ord(char) - ord('a'))] += 1

        for char in t:
            freq_t[int(ord(char) - ord('a'))] += 1

        for i in range(26):
            if freq_s[i] > freq_t[i]:
                return False

        return True
