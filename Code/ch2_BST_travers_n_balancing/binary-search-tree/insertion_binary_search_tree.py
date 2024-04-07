# creating a user class
class User:
    def __init__(self,username, name, email) -> None:
        self.username = username
        self.name = name
        self.email = email
    
    def __repr__(self) -> str:
        return "User(usernamed={}, name={}, email={})\n".format(self.username,self.name,self.email)
    
    def __str__(self) -> str:
        return self.__repr__()

rohan = User("rohan111","rohan","rohan@gmail.com")
sohan = User("sohan111","sohan","sohan@gmail.com")
mohan = User("mohan111","mohan","mohan@gmail.com")

# print(rohan,sohan)

# creating a DB class
class UserDatabase:
    def __init__(self) -> None:
        self.users:User = []
    
    def insert(self, user:User):
        i=0
        while i < len(self.users):
            # find the first username which is greater than new username    
            if self.users[i].username > user.username:
                break
            i+=1
        self.users.insert(i,user)
    
    def find(self, username)-> User:
        for u in self.users:
            if u.username == username:
                return u
    
    def update(self, user:User)->None:
        u = self.find(user.username)
        u.name, u.email = user.name, user.email

    def list(self):
        return self.users
    
# db = UserDatabase()
# print("users initially: ",len(db.users), db.list())

# db.insert(rohan)
# db.insert(mohan)
# print("users after: ", len(db.users), db.list())

# # changing mannu from mohan
# mannu = User("mohan111","mannu","mannu@gmail.com")
# db.update(mannu)
# print("users after update : ", len(db.users), db.list())


# architecture of a Tree for a User based nodes

class BSTNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

bst:BSTNode = BSTNode(rohan.username, rohan)
bst.left = BSTNode(sohan.username, sohan)
bst.left.parent=bst
bst.right = BSTNode(mohan.username, mohan)
bst.right.parent=bst

# print("node: ",bst.key)
# print("left: ",bst.left.parent.key)
# print("right: ",bst.right.parent.key)

# function to display elements in tree from
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

# display_keys(bst)

# function to insert nodes in sorted and efficient manner
def insert(node:BSTNode, key, value)->BSTNode:
    if node is None:
        return BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left,key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

# creating nodes for BST tree
alvarez = User("alvarez","Julian","jalvarez@gmail.com")
silva = User("silva","Bernardo","bsilva@gmail.com")
dias = User("dias","Ruben","rdias@gmail.com")
foden = User("foden","Phil","pfoden@gmail.com")
grealish = User("grealish","Jack","jgrealish@gmail.com")
walker = User("walker","kyle","kwalker@gmail.com")
zinchenko = User("zinchenko","olekzandr","ozinchenko@gmail.com")
kane = User("kane","Harry","hkane@gmail.com")

t = insert(None,silva.username,silva)
insert(t,dias.username,dias)
insert(t,grealish.username,grealish)
insert(t,walker.username,walker)
insert(t,foden.username,foden)
insert(t,alvarez.username, alvarez)
insert(t,zinchenko.username, zinchenko)

# print("a normal example: ")
# display_keys(t)

t = insert(None,alvarez.username, alvarez)
insert(t,dias.username,dias)
insert(t,foden.username,foden)
insert(t,grealish.username,grealish)
insert(t,silva.username, silva)
insert(t,walker.username,walker)
insert(t,zinchenko.username, zinchenko)

# print("skewed tree example: ")
# display_keys(t)

def find_in_bst(node:BSTNode, key:str)->BSTNode:
    if node is None:
        return None
    if node.key == key:
        return node
    if node.key < key:
        return find_in_bst(node.right, key)
    if node.key > key:
        return find_in_bst(node.left, key)

# res:BSTNode = find_in_bst(t, "silva")
# print(res.key,res.parent.key)

# res:BSTNode = find_in_bst(t, "thiago")
# print(res)

def update_user(node:BSTNode, key:str, value:User)->None:
    target = find_in_bst(node, key)
    if target is not None:
        print("found!!!",target.value.username)
        target.value = value

# update_user(t,"silva",User("Silva","Thiago","tsilva123@gmail.com"))
# find_:BSTNode = find_in_bst(t,"silva")
# print(find_.value.name)

# the list can be listed in sorted order by performing a inorder traversal
def inorder(node:BSTNode)->list[int]:
    if node is None:
        return []
    return (inorder(node.left)+[(node.key, node.value)]+inorder(node.right)) 


t = insert(None,silva.username,silva)
insert(t,dias.username,dias)
insert(t,grealish.username,grealish)
insert(t,walker.username,walker)
insert(t,foden.username,foden)
insert(t,alvarez.username, alvarez)
insert(t,zinchenko.username, zinchenko)
insert(t,kane.username,kane)

print(inorder(t))