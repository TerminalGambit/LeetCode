from typing import List

class Solution:
    """
    You are given an m x n binary matrix matrix.
    You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).
    Return the maximum number of rows that have all values equal after some number of flips.
    """
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hashdict = {}

        for row in matrix:
            if row[0] == 0:
                row = [1 - x for x in row]
            hashdict[tuple(row)] = hashdict.get(tuple(row), 0) + 1

        return max(hashdict.values())


    def assertions(self):
        assert (self.maxEqualRowsAfterFlips(solution, matrix=[[0, 1], [1, 1]]) == 1)
        assert (self.maxEqualRowsAfterFlips(solution, matrix=[[0, 1], [1, 0]]) == 2)
        assert (self.maxEqualRowsAfterFlips(solution, matrix=[[0, 0, 0], [0, 0, 1], [1, 1, 0]]) == 2)


if __name__ == "__main__":
    solution = Solution
    solution.assertions(solution)
