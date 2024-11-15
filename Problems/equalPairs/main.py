from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = set(grid)
        cols = set(zip(*grid))
        return sum(min(rows.count(row), cols.count(col)) for row in rows for col in cols) // 2