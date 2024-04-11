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

# basic user class
class User:
    def __init__(self,username, name, email) -> None:
        self.username = username
        self.name = name
        self.email = email
    def __repr__(self) -> str:
        return f"User({self.username}, {self.name}, {self.email})"
    
    def __str__(self) -> str:
        return self.__repr__()

# basic node for User class
class UserNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

# insert into binary search tree
def insert(node:UserNode, key:str, value:UserNode):
    if node is None:
        return UserNode(key, value)
    if key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    if key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    return node

# find in binary search tree
def find(node:UserNode, key:str):
    if node is None:
        return None
    if node.key == key:
        return node
    if node.key > key:
        return find(node.left, key)
    if node.key < key:
        return find(node.right, key)

# update in binary search tree
def update(node:UserNode, key:str, value:UserNode):
    user = find(node,key)
    if user is not None:
        user.key, user.value = key, value

# returns all users in ordered manner
def list_all(node:UserNode):
    if node is None:
        return []
    return list_all(node.left)+[(node.key, node.value)]+ list_all(node.right)

# returns total numbers of users
def total_nodes(node:UserNode):
    if node is None:
        return 0
    return total_nodes(node.left)+1+total_nodes(node.right)

# gives graphical representation of a tree
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

# function to balance Binary Tree
def make_balanced_bst(data:list[UserNode], low = 0, high = None, parent = None):
    if high is None:
        high = len(data)-1
    if low > high:
        return None
    
    mid = (low + high) // 2
    key, value = data[mid]
    root = UserNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, low, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, high, root)

    return root

# main class which is a modal for an ideal BALANCED-BINARY-SEARCH-TREE modal 
class TreeNode:
    def __init__(self) -> None:
        self.root = None

    def __setitem__(self, key, value)->None:
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = make_balanced_bst(list_all(self.root))            
        else:
            update(self.root, key, value)
    
    def __getitem__(self,key)->UserNode:
        return find(self.root, key)
    
    def __iter__(self)->list[UserNode]:
        return (user for user in list_all(self.root))
    
    def __len__(self)->int:
        return total_nodes(self.root)
    
    def display(self):
        return display_keys(self.root)

# crating an instance of TreeNode Class
treenode = TreeNode()

# creating users to be inserted
anil = User("anil","anil","anil@gmail.com")
sunil = User("sunil","sunil","sunil@gmail.com")
sumit = User("sumit","sumit","sumit@gmail.com")

treenode['anil'] = anil
treenode['sunil'] = sunil
treenode['sumit'] = sumit

for key, value in treenode:
    print(key)

# presumably a bug, not certain about, but gotta check