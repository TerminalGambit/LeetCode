from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        result = [1] * n + rolls
        total_mean = (sum(result) / (n + m)) if sum(result) % (n + m) == 0 else 7
        i = 0
        floor = 2

        while total_mean != mean:
            if result[i] == 6 and i == n:
                return []

        return result[0:n]
