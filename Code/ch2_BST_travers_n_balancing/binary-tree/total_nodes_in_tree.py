# tree height
#      4
#   2     7
# 1  3  6  8

class Tree:
    def __init__(self, key:int)->None:
        self.key = key
        self.left = None
        self.right = None

data = ((1,2,3),4,(6,7,8))

def parse_tree(data:tuple)-> Tree:
    if isinstance(data,tuple) and len(data) == 3:
        node:Tree = Tree(data[1])
        node.left = parse_tree(data[0])
        node.right = parse_tree(data[2])
    elif data is None:
        node:Tree = None
    else:
        node:Tree = Tree(data)
    return node

t = parse_tree(data)

def total_nodes(data:Tree)->int:
    if data is None:
        return 0
    return total_nodes(data.left) + 1 + total_nodes(data.right)

print(total_nodes(t))