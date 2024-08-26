class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        def cumsum_bidirectional(nums):
            n = len(nums)

            # List for cumulative sum from left to right
            left_to_right_cumsum = [0] * n
            # List for cumulative sum from right to left
            right_to_left_cumsum = [0] * n

            # Initialize the first value for the left-to-right cumulative sum
            if n > 0:
                left_to_right_cumsum[0] = nums[0]
                right_to_left_cumsum[n - 1] = nums[n - 1]

            # Calculate the cumulative sum from left to right
            for i in range(1, n):
                left_to_right_cumsum[i] = left_to_right_cumsum[i - 1] + nums[i]

            # Calculate the cumulative sum from right to left
            for i in range(n - 2, -1, -1):
                right_to_left_cumsum[i] = right_to_left_cumsum[i + 1] + nums[i]

            return left_to_right_cumsum, right_to_left_cumsum

        left_to_right_cumsum, right_to_left_cumsum = cumsum_bidirectional(nums)

        def subtract_lists(A, B):
            # Check if the lists have the same length
            if len(A) != len(B):
                raise ValueError("Lists must be of the same length")

            # Generate the result list by subtracting corresponding elements
            result = [a - b for a, b in zip(A, B)]
            return result

        result = subtract_lists(left_to_right_cumsum, right_to_left_cumsum)

        def find_index_of_zero(nums):
            try:
                # Return the index of the first occurrence of 0
                return nums.index(0)
            except ValueError:
                # Return -1 if 0 is not in the list
                return -1

        return find_index_of_zero(result)
