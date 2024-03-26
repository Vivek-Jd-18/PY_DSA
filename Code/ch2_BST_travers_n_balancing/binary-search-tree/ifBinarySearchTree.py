class Tree:
    def __init__(self,key) -> None:
        self.key = key
        self.right = None
        self.left = None

tree_data = ((1,2,3),4,(5,6,7))

def if_tree_isbst(tree:Tree):
