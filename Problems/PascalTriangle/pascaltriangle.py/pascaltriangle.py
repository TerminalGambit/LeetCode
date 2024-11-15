# Given an integer numRows, return the first numRows of Pascal's triangle.
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result

        first_row = [1]
        result.append(first_row)

        for i in range(1, numRows):
            prev_row = result[i - 1]
            current_row = [1]

            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])

            current_row.append(1)
            result.append(current_row)

        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.generate(5))
    print(solution.generate(1))
    print(solution.generate(2))
    print(solution.generate(3))
    print(solution.generate(4))