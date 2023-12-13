"""
Given an integer x, return true if x is a 
palindrome, and false otherwise.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Convert to string
        x = str(x)
        # Check if the string is equal to the reverse
        if x == x[::-1]:
            return True
        else:
            return False