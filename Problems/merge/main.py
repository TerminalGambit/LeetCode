from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Indices for nums1, nums2, and the end of the merged array
        i = m - 1  # Last element in the initial part of nums1
        j = n - 1  # Last element in nums2
        k = m + n - 1  # Last position in nums1 to fill

        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2, fill them in nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

