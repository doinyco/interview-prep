# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

class Solution:
    def __init__(self):
        self.root = None

    def search_bst(self, root, val):
        current = root

        while current:
            if current.val == val:
                return current
            elif current.val < val:
                current = current.right
            else:
                current = current.left

        return None
    

# Instantiate Solution class
sol = Solution()
# Create a binary search tree
sol.root = TreeNode(4)
sol.root.left = TreeNode(2)
sol.root.right = TreeNode(7)
sol.root.left.left = TreeNode(1)
sol.root.left.right = TreeNode(3)


# Test search_bst method
print(sol.search_bst(sol.root, 2)) # TreeNode object with value 2

