from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)

        def create_solutions(length):
            result = []
            current = [1] * length
            result.append(current)

            for i in range(length):
                for j in range(2, 7):
                    current[i] = j
                    result.append(current)

            return result

        solutions = create_solutions(n)

        for solution in solutions:
            tested_value = solution + rolls
            if sum(tested_value) % (n + m) == 0:
                total_mean = sum(tested_value) / (n + m)
                if total_mean == mean:
                    return tested_value[:n]

        return []
