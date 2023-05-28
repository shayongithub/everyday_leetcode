from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if root is None:
        return True

    def isNodeSame(node1, node2):
        if node1 is None and node2 is None:
            return True

        if node1 is None or node2 is None:
            return False

        if node1.val != node2.val:
            return False

        return isNodeSame(node1.left, node2.right) and isNodeSame(
            node1.right, node2.left
        )

    return isNodeSame(root.left, root.right)
