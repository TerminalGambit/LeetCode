class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def is_feasible_distance(distance):
            """Return True if distance is a feasible distance."""
            count, prev = 0, -inf # where previous ball is put
            for x in position:
                if x - prev >= distance: 
                    count += 1
                    if count == m: return True
                    prev = x
            return False 
        
		# "last True" binary search (in contrast to "first True" binary search)
        lo, hi = 1, position[-1] - position[0]
        while lo < hi: 
            mid = lo + hi + 1 >> 1
            if is_feasible_distance(mid): lo = mid
            else: hi = mid - 1
        return lo