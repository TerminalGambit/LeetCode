from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == '../':
                depth = max(0, depth - 1)
            elif log != './':
                depth += 1
        return depth


if __name__ == '__main__':
    solution = Solution()
    assert solution.minOperations(["d1/", "d2/", "../", "d21/", "./"]) == 2
    assert solution.minOperations(["d1/", "d2/", "./", "d3/", "../", "d31/"]) == 3
    assert solution.minOperations(["d1/", "../", "../", "../"]) == 0
