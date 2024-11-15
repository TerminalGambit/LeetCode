"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if s is empty, return 0
        if len(s) == 0:
            return 0
        
        # if s is not empty, return the length of the longest substring
        # use a dictionary to store the index of the character
        # use two pointers to indicate the start and end of the substring
        # if the character is not in the dictionary, add it to the dictionary
        # if the character is in the dictionary, update the start pointer
        # update the length of the longest substring
        # return the length of the longest substring
        dict = {}
        start = 0
        end = 0
        length = 0
        while end < len(s):
            if s[end] in dict:
                start = max(start, dict[s[end]] + 1)
            dict[s[end]] = end
            length = max(length, end - start + 1)
            end += 1
        return length
