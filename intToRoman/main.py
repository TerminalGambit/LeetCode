class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping of integer values to Roman numerals
        value_symbols = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        roman = []  # This will store the result as a list of characters

        # Iterate over each symbol, starting from the largest
        for value, symbol in value_symbols:
            # Append the symbol to the result as many times as num contains value
            while num >= value:
                roman.append(symbol)
                num -= value

        return ''.join(roman)  # Convert the list of characters into a string


# Example Usage
sol = Solution()
print(sol.intToRoman(3))  # Output: "III"
print(sol.intToRoman(4))  # Output: "IV"
print(sol.intToRoman(9))  # Output: "IX"
print(sol.intToRoman(58))  # Output: "LVIII"
print(sol.intToRoman(1994))  # Output: "MCMXCIV"
