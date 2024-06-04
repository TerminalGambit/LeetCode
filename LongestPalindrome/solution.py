class Solution:
    def longestPalindrome(self, s: str) -> int:
        # if the length of the string is 0, return 0
        if len(s) == 0:
            return 0
        
        # if the length of the string is 1, return 1
        if len(s) == 1:
            return 1
        
        # if the length of the string is greater than 1, return the length of the longest palindrome
        # use a new dictionary to store the frequency of the characters in the string
        # use a variable to store the length of the longest palindrome
        # use a for loop to iterate through the string
        # if the character is already in the dictionary, increment the frequency
        # if the character is not in the dictionary, add the character to the dictionary
        # use a variable to store the flag for the middle character
        # use a for loop to iterate through the dictionary
        # if the frequency is even, increment the length of the longest palindrome
        # if the frequency is odd, set the flag to 1
        # if the flag is 1, increment the length of the longest palindrome
        # return the length of the longest palindrome
        freq = {}
        length = 0
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        flag = 0
        for key in freq:
            if freq[key] % 2 == 0:
                length += freq[key]
            else:
                flag = 1
                length += freq[key] - 1
        if flag == 1:
            length += 1
        return length