# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return
        queue = [root]
        result = []
        while queue:
            l = len(queue)
            onelist = []
            for _ in range(l):
                node = queue.pop(0)
                onelist.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(onelist)
        return result[::-1]

# Runtime: 20 ms, faster than 99.82% of Python3 online submissions for Binary Tree Level Order Traversal II.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal II.