import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
t_data = (1,2,3)

def parse_tree(data: tuple) -> TreeNode:
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tree(data[0])
        node.right = parse_tree(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node
n_data = parse_tree(t_data)
class Solution:
    def isValidBST(self, root) -> bool:
       return self.isValid(root, - 2**31-1, 2**31)
    
    def isValid(self,node, min_val, max_val):
        if node == None:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (self.isValid(node.left, min_val, node.val) and self.isValid(node.right, node.val, max_val))

s = Solution()
print(s.isValidBST(n_data)) 