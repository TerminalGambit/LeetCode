class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area with the current left and right pointers
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)

            # Move the pointer that points to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Example Usage
sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
