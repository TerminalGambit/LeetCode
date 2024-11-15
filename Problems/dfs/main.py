# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        # Helper function to get the leaf sequence
        def dfs(node: TreeNode):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return dfs(node.left) + dfs(node.right)
