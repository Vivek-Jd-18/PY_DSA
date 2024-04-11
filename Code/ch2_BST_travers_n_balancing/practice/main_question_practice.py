# Q. as a senior backend engineer you are asked to create fast in-memory data structure to manage
#  profile information (username, name and email) for 100 million users, it should allow the following
# operations to be done efficiently

# 1) Insert the profile information for a new user
# 2) Find the profile information of a user, given their username
# 3) Update the profile information of a user, given their username
# 4) List all the profile information of all the users, sorted by username

# you can assume that the username is unique 

# SOLUTION:
#  we will create a generic class TreeNode, which supports all the operations
# defined in given problem, in python friendly way.


class Player:
    def __init__(self, name, club, age) -> None:
        self.name = name
        self.club = club
        self.age = age
    
    def __repr__(self) -> str:
        return f"Player({self.name}, {self.club}, {self.age})"
    
    def __str__(self) -> str:
        return self.__repr__()
    
# players data
iniesta = Player("iniesta", "Barcelona", 41)
xabi = Player("xabi", "Madrid", 40)
lampard = Player("lampard", "Chelsea", 43)
scholes = Player("scholes", "Manchester united", 45)
zidane = Player("zidane", "Madrid", 48)
ronaldinho = Player("ronaldinho", "Milan",46)

class PlayerNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# insert
def insert(node:PlayerNode, key:str, value:PlayerNode)->PlayerNode:
    if node is None:
        return PlayerNode(key,value)
    if node.key > key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    if node.key < key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node  

# find
def find(node:PlayerNode, key:str)->PlayerNode:
    if node is None:
        return None
    if node.key == key:
        return node
    if node.key < key:
        return find(node.right, key)
    if node.key > key:
        return find(node.left, key)

# list_all
def list_all(node:PlayerNode)->list[PlayerNode]:
    if node is None:
        return []
    return list_all(node.left)+[(node.key, node.value)]+list_all(node.right)

# update
def update(node:PlayerNode, key:str, value:PlayerNode)->None:
    player = find(node, key)
    if player is not None:
        player.value = value

def total_users(node:PlayerNode):
    if node is None:
        return 0
    return total_users(node.left)+ 1 +total_users(node.right)

# make_balanced_tree
def make_balanced_tree(data:list[PlayerNode], low = 0, high = None, parent = None):
    if high is None:
        high = len(data)-1
    if low > high:
        return None
    
    mid = (low+high) // 2
    key, value = data[mid]
    player = PlayerNode(key, value)
    player.parent = parent
    player.left = make_balanced_tree(data, low, mid-1, player)
    player.right = make_balanced_tree(data, mid+1, high, player)
    return player

# display all nodes
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

players = [iniesta, xabi, zidane, lampard, ronaldinho, scholes]

class TreeMap:
    def __init__(self) -> None|PlayerNode:
        self.root = None
    # setitem, getitem, iter, len, display
    def __setitem__(self, key, value):
        target = find(self.root, key)
        if not target:
            self.root = insert(self.root, key, value)
            self.root = make_balanced_tree(list_all(self.root))
        else:
            update(self.root, key, value)

    def __getitem__(self, key):
        return find(self.root, key)
    
    def __iter__(self)->list[PlayerNode]:
        return (i for i in list_all(self.root))
    
    def __len__(self):
        return total_users(self.root)
    
    def display(self):
        return display_keys(self.root)
    
player_tree = TreeMap()

# insertion
player_tree['iniesta'] = iniesta
player_tree['scholes'] = scholes
player_tree['zidane'] =  zidane

# length
print(len(player_tree))

# display all in tree form
player_tree.display()

# fetch single item
print(player_tree['iniesta'].value)

# iter through all players
for key, val in player_tree:
    print("Legend: ", key, val)