"""
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
"""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # if matrix is empty, return empty matrix
        if len(matrix) == 0:
            return []
        
        # if matrix is not empty, return the transpose of matrix
        # use two pointers to indicate the row and column of the matrix
        # use a new matrix to store the transpose of matrix
        # return the transpose of matrix
        row = len(matrix)
        column = len(matrix[0])
        new_matrix = [[0 for i in range(row)] for j in range(column)]
        for i in range(row):
            for j in range(column):
                new_matrix[j][i] = matrix[i][j]
        return new_matrix