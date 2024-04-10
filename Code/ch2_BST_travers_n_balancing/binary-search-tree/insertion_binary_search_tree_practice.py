class User:
    def __init__(self,username,name,email) -> None:
        self.username = username
        self.name = name
        self.email = email
    
    def __repr__(self) -> str:
        return "USER(username:{},name:{},email:{})".format(self.username,self.name,self.email)
    
    def __str__(self) -> str:
        return self.__repr__()
    
# linear modal
class UserDB:
    def __init__(self) -> None:
        self.users:list[User] = []

    def insert(self, user:User):
        i = 0
        while i < len(self.users):
            if user.username > self.users[i].username:
                break
            i+=1
        self.users.insert(i,user)
    
    def find(self, username)->User:
        return next((u for u in self.users if u.username == username), None)
    
    def update(self, user:User)->None:
        target:User = self.find(user.username)
        target.name,target.email = user.name, user.email
    
    def list(self)->list[User]:
        return self.users   

alvarez = User("alvarez","Julian","jalvarez@gmail.com")
silva = User("silva","Bernardo","bsilva@gmail.com")
dias = User("dias","Ruben","rdias@gmail.com")

db = UserDB()
db.insert(alvarez)
print(db.list())
print(db.find("alvarez"))
db.update(User(username="alvarez",name="Julian Alvarez",email="jalvarez009@gmail.com"))
print(db.list())


# binary tree node Model
class BSTNode:
    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def insert(node:BSTNode,key, value):
    if node is None:
        return BSTNode(key,value)
    if node.key < key:
        node.right = insert(node.right,key, value)
        node.right.parent = node
    if node.key > key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    return node


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
insert(t,kane.username,kane)
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

display_keys(t)

def inorder(node:BSTNode)->list[int]:
    if node is None:
        return []
    return (inorder(node.left)+[(node.key, node.value)]+inorder(node.right))

print(inorder(t))