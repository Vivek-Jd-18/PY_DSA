# example of inorder traversal
#      4
#   2     7
# 1  3  6  8

class Tree:
    def __init__(self, key:int)->None:
        self.key = key
        self.left = None
        self.right = None

tree_data = ((1,2,3), 4, (6,7,8))

def parse_tree(data:tuple)->Tree:
    if isinstance(data, tuple) and len(data) == 3:
        node:Tree = Tree(data[1])
        node.left = parse_tree(data[0])
        node.right = parse_tree(data[2])
    elif data == None:
        node:Tree = None
    else:
        node:Tree = Tree(data)
    return node

t = parse_tree(tree_data)
# print(t.key)
# print(t.right.left.key)

def inorder_traversal(node:Tree)->list[int]:
    if node is None:
        return[]
    return ([node.key]+inorder_traversal(node.left)+inorder_traversal(node.right))

t = inorder_traversal(t)
print(t)