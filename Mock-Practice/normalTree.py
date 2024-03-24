class Tree:
    def __init__(self, key:int) -> None:
        self.left = None
        self.right = None
        self.key = key

node0:Tree = Tree(5)
node0.left = 1
node0.right = 6

print(node0.key)
print(node0.left)
print(node0.right)