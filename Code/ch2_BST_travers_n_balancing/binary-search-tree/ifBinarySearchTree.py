# import sys
# class Tree:
#     def __init__(self,key) -> None:
#         self.key = key
#         self.right = None
#         self.left = None

# # tree_data = ((1,2,3),4,(5,6,7))
# # tree_data = ((1,3,2),4,(5,6,7))
# # tree_data = (4,7,9)
# tree_data = (None, 1, 6)

# #         1
# #    None   6

# def parse_tuple(nodes:tuple)-> Tree:
#     if isinstance(nodes, tuple) and len(nodes) == 3:
#         node:Tree = Tree(nodes[1])
#         node.left = parse_tuple(nodes[0])
#         node.right = parse_tuple(nodes[2])
#     elif nodes is None:
#         node:Tree = None
#     else:
#         node:Tree = Tree(nodes)
#     return node

# tree0 = parse_tuple(tree_data)

# # check if tree is bst or not using general approach
# def is_bst(node:Tree, min_val:int, max_val:int) -> bool:
#     if node.left is None != node.right is None:
#         return False
#     if node == None:
#         return True
#     if node.key >= max_val or node.key <= min_val:
#         return False
#     return (is_bst(node.right, node.key, max_val) and is_bst(node.left, min_val, node.key))

# print(is_bst(tree0, -2**31-1, 2**31))




# ---------------------------------------------------------------------------------------------------------------------------------
# structure for Tree
class Tree:
    def __init__(self,key) -> None:
        self.key = key
        self.left = None
        self.right = None

# data to be parsed to form a tree
data = ((1,3,5), 8, (9, 10, 12))

# function to parse a tuple into a tree
def parse_tree(data:tuple)->Tree:
    if isinstance(data, tuple) and len(data) == 3:
        node:Tree = Tree(data[1])
        node.left = parse_tree(data[0])
        node.right = parse_tree(data[2])
    elif data is None:
        node = None
    else:
        node = Tree(data)
    return node

t1 = parse_tree(data)
print(t1.right.left.key) # 9 verified

# sorting a tree

# 1) inorder
def inorder_traversal(data:Tree)->list[int]:
    if data is None:
        return []
    return (inorder_traversal(data.left)+[data.key]+inorder_traversal(data.right))
print("inorder traversal:   ",inorder_traversal(t1))

# 2) preorder
def preorder_traversal(data:Tree)->list[int]:
    if data is None:
        return []
    return ([data.key]+preorder_traversal(data.left)+preorder_traversal(data.right))
print("preorder traversal:  ",preorder_traversal(t1))

# 3) postorder
def postorder_traversal(data:Tree)->list[int]:
    if data is None:
        return []
    return (preorder_traversal(data.left)+preorder_traversal(data.right)+[data.key])
print("postorder traversal: ",postorder_traversal(t1))


# height of Tree
def height(tree:Tree)->int:
    if tree is None:
        return 0
    return 1 + max(height(tree.left),height(tree.right))
print("height: ",height(t1))

# total nodes
def total(tree:Tree)->int:
    if tree is None:
        return 0
    return 1+(total(tree.left)+total(tree.right))
print("total nodes: ",total(t1))