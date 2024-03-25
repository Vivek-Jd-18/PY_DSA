# example of inorder traversal
#      4
#   2     7
# 1  3  6  8

class Tree:
    def __init__(self, key:int)-> None:
        self.left = None
        self.right = None
        self.key = key
    
data = ((1,2,3),4,(6,7,8))

def parse_tree(data:tuple)->Tree:
    if isinstance(data, tuple) and len(data) == 3:
        node:Tree = Tree(data[1])
        node.left = parse_tree(data[0])
        node.right = parse_tree(data[2])
    elif data is None:
        node:Tree = None
    else:
        node:Tree = Tree(data)
    return node

def postorder_traversal(node:Tree)-> list[int]:
    if node is None:
        return[]
    return (postorder_traversal(node.left) + postorder_traversal(node.right) + [node.key])

t = postorder_traversal(parse_tree(data))
print(t)