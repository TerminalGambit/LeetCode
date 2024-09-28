# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Helper function to recursively build the BST
        def buildBST(left, right):
            if left > right:  # Base case: no elements to consider
                return None

            # Choose the middle element as the root
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            # Recursively build the left and right subtrees
            node.left = buildBST(left, mid - 1)
            node.right = buildBST(mid + 1, right)

            return node

        # Call the helper function with the entire range of the input array
        return buildBST(0, len(nums) - 1)