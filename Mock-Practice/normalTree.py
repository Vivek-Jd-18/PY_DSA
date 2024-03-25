class Tree:
    def __init__(self, key:int) -> None:
        self.left = None
        self.right = None
        self.key = key

# node0:Tree = Tree(5)
# node0.left = 1
# node0.right = 6


# print(node0.key)
# print(node0.left)
# print(node0.right)


# Parsing tuple to Tree
tulpe1: tuple = (((1,2,3),4,None),5,(6,7,8))

def parse_tupl(data:tuple) -> Tree:
    if isinstance(data,tuple) and len(data) == 3:
        node = Tree(data[1])
        node.left = parse_tupl(data[0])
        node.right = parse_tupl(data[2])
    elif data is None:
        node = None
    else:
        node = Tree(data)
    return node

new_node = parse_tupl(tulpe1)

print(new_node.key)
print(new_node.left.right)
print(new_node.left.right)
print(new_node.right.left.key)