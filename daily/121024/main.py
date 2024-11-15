import heapq
from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap = []

        for interval in intervals:
            start, end = interval
            if heap and heap[0] < start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)
