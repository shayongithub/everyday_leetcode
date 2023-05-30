from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(self, root: Optional[TreeNode]) -> int:
    def maxNode(root):
        return (
            max(maxNode(root.left), maxNode(root.right)) + 1 if root is not None else 0
        )

    return maxNode(root)
