# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        # 1) total sum
        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)

        total = total_sum(root)

        # 2) try cutting above each subtree
        best = 0

        def sub_sum(node):
            nonlocal best
            if not node:
                return 0
            s = node.val + sub_sum(node.left) + sub_sum(node.right)
            best = max(best, s * (total - s))
            return s

        sub_sum(root)
        return best % MOD