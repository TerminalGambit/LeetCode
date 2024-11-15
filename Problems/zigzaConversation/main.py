def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    # List to hold strings for each row
    rows = ['' for _ in range(numRows)]
    current_row = 0
    going_down = False

    for char in s:
        # Place character in the current row
        rows[current_row] += char

        # Determine if we need to go up or down
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down

        # Update the current row
        if going_down:
            current_row += 1
        else:
            current_row -= 1

    # Join all rows to form the final string
    return ''.join(rows)


# Example usage
s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))  # Output: "PAHNAPLSIIGYIR"

numRows = 4
print(convert(s, numRows))  # Output: "PINALSIGYAHRPI"