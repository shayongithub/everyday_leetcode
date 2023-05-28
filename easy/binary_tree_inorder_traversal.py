from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:

    ans = []

    if root is None:
        return []

    def loopTree(node):
        if node.left is None:
            if node.right is None:
                ans.append(node.val)
                return node.val
            else:
                loopTree(node.right)
                ans.append(node.right.val)
        else:
            loopTree(node.left)
            ans.append(node.left.val)

    loopTree(root)

    return ans


if __name__ == "__main__":

    three = TreeNode(3)
    two = TreeNode(2, left=three)
    root = TreeNode(1, right=two)

    print(inorderTraversal(root))