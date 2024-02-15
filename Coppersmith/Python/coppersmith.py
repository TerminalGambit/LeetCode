"""
Given two matrix, implement the Coppersmith algorithm to multiply the two matrix.
"""

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # if A is empty, return empty matrix
        if len(A) == 0:
            return []
        
        # if B is empty, return empty matrix
        if len(B) == 0:
            return []
        
        # if A is not empty and B is not empty, return the product of A and B
        # use three pointers to indicate the row, column and the length of the matrix
        # use a new matrix to store the product of A and B
        # return the product of A and B
        row = len(A)
        column = len(B[0])
        length = len(A[0])
        new_matrix = [[0 for i in range(column)] for j in range(row)]
        for i in range(row):
            for j in range(column):
                for k in range(length):
                    new_matrix[i][j] += A[i][k] * B[k][j]
        return new_matrix