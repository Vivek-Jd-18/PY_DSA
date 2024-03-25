# example of preorder traversal
#      4
#   2     7
# 1  3  6  8
class Tree:
    def __init__(self, key:int)->None:
        self.left = None
        self.right = None
        self.key = key


data = ((1,2,3),4,(6,7,8))

def parse_tuple(data:tuple)->Tree:
    if isinstance(data, tuple) and len(data) == 3:
        node:Tree
        node = Tree(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node:Tree
        node = None
    else:
        node = Tree(data)
    return node

t = parse_tuple(data)

print(t.key)
# print(t.left.key)
# print(t.left.left.key)
# print(t.left.right.key)
# print(t.right.key)
# print(t.right.left.key)
# print(t.right.right.key)


def inorder_traversal(data):
    if data is None:
        return[]
    return (inorder_traversal(data.left)+[data.key]+inorder_traversal(data.right))

t = inorder_traversal(parse_tuple(data))

print(t)