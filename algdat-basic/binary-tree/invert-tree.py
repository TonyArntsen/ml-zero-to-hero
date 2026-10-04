import numpy as np
from binarytree import tree

def invertTree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

random_tree = tree(height=3, is_perfect=False)
print("Generated Random Binary Tree:")
print(random_tree)

inverted_tree = invertTree(random_tree)
print("\nInverted Binary Tree:")
print(inverted_tree)
