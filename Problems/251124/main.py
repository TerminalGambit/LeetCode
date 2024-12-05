from collections import deque
from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [3, 1, 5],
            5: [4, 2]
        }

        start = tuple(board[0] + board[1])
        target = (1, 2, 3, 4, 5, 0)
        queue = deque([(start, 0)])
        visited = set()
        visited.add(start)

        while queue:
            current, steps = queue.popleft()

            if current == target:
                return steps

            iz = current.index(0)

            for move in moves[iz]:
                ns = current
                ns = list(ns)
                print(ns)
                ns[iz], ns[move] = ns[move], ns[iz]
                print(ns)
                nt = tuple(ns)

                if nt not in visited:
                    visited.add(nt)
                    queue.append((nt, steps + 1))

        return -1


if __name__ == "__main__":
    solution = Solution()
    solution.slidingPuzzle([[1, 2, 3], [4, 0, 5]])
