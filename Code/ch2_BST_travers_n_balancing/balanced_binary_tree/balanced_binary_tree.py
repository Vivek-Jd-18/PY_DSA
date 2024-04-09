# check if binary tree is balanced??

# normal player structure
class Player:
    def __init__(self, name, club, age):
        self.name = name
        self.club = club
        self.age = age

# structure to store player in binary tree form
class PlayerBST:
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# functio to storing players in DB (binary search DB)
def insert_in_bst(node:None|PlayerBST, key:str, value:str)->PlayerBST:
    if node is None:
        return PlayerBST(key,value)
    if key > node.key:
        node.right = insert_in_bst(node.right, key, value)
        node.right.parent = node
    if key < node.key:
        node.left = insert_in_bst(node.left, key, value)
        node.left.parent = node
    return node

alvarez = Player("alvarez","MCI",21)
silva = Player("silva","MCI",29)
dias = Player("dias","MCI",28)
foden = Player("foden","MCI",23)
grealish = Player("grealish","MCI",27)
walker = Player("walker","MCI",30)
zinchenko = Player("zinchenko","ARS",28)
kane = Player("kane","BAY",30)

t = insert_in_bst(None,alvarez.name, alvarez)
insert_in_bst(t,dias.name,dias)
insert_in_bst(t,foden.name,foden)
insert_in_bst(t,grealish.name,grealish)
insert_in_bst(t,kane.name,kane)
insert_in_bst(t,silva.name,silva)
insert_in_bst(t,walker.name,walker)
insert_in_bst(t,zinchenko.name, zinchenko)

def display_keys(node, space = '\t', level = 0):
    if node is None:
        print(space*level + '*')
        return
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    display_keys(node.right,space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space,level+1)

display_keys(t)

def inorder(node:PlayerBST)->list[PlayerBST|None]:
    if node is None:
        return []
    return (inorder(node.left) + [{node.key: [{"club": node.value.club} ,{"age":node.value.age}]}] + inorder(node.right))

print(inorder(t))

def is_balanced(node:PlayerBST):
    if node is None:
        return True, 0
    balance_left, height_l = is_balanced(node.left) 
    balance_right, height_r = is_balanced(node.right)
    balanced = balance_left and balance_right and abs(height_l- height_r) <= 1
    height = 1 + max(height_l, height_r)
    return balanced, height

print("jovian approach: ",is_balanced(t))

def is_balanced2(node:PlayerBST,index:int, number_nodes:int)->bool:
    if node is None:
        return True     
    # If index assigned to current nodes is more than
    # number of nodes in tree, then tree is not complete
    if index >= number_nodes :
        return False     
    # Recur for left and right subtrees
    return (is_balanced2(node.left , 2*index+1 , number_nodes)and is_balanced2(node.right, 2*index+2, number_nodes))

def total_nodes(node:PlayerBST)->int:
    if node is None:
        return 0
    return 1 + total_nodes(node.left) + total_nodes(node.right)

print("gfg approach: ",is_balanced2(t,0,total_nodes(t)))