import sys
class Tree:
    def __init__(self,key) -> None:
        self.key = key
        self.right = None
        self.left = None

# tree_data = ((1,2,3),4,(5,6,7))
# tree_data = ((1,3,2),4,(5,6,7))
# tree_data = (4,7,9)
tree_data = (None, 1, 6)

def parse_tuple(nodes:tuple)-> Tree:
    if isinstance(nodes, tuple) and len(nodes) == 3:
        node:Tree = Tree(nodes[1])
        node.left = parse_tuple(nodes[0])
        node.right = parse_tuple(nodes[2])
    elif nodes is None:
        node:Tree = None
    else:
        node:Tree = Tree(nodes)
    return node

tree0 = parse_tuple(tree_data)

# check if tree is bst or not using general approach
def is_bst(node:Tree, min_val:int, max_val:int) -> bool:
    print((node.key if node is not None else None), min_val, max_val)
    if node == None:
        return True
    if node.key >= max_val or node.key <=min_val:
        return False
    return (is_bst(node.right, node.key, max_val) and is_bst(node.left, min_val, node.key))

print(is_bst(tree0, -2**31-1, 2**31))