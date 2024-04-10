# normal player structure
class Player:
    def __init__(self, name, club, age):
        self.name = name
        self.club = club
        self.age = age

# player db with CRUD
class PlayerDB:
    def __init__(self)->None:
        self.players:list[Player] = []
    
    def insert(self, player:Player)->None:
        p = 0
        while p < len(self.players):
            if self.players[p] > player.name:
                break
            p+=1
        self.players.insert(p, player)
    
    def find(self, name:str)->Player:
        for p in self.players:
            if name == p.name:
                return p

    def update(self, player:Player)->None:
        p = self.find(player)
        if p.name == player.name:
            p.name, p.club, p.age = player.name, player.club, player.age
    
    def list_all(self)->list[Player]:
        return self.players

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

t = insert_in_bst(None,silva.name,silva)
insert_in_bst(t,dias.name,dias)
insert_in_bst(t,grealish.name,grealish)
insert_in_bst(t,walker.name,walker)
insert_in_bst(t,foden.name,foden)
insert_in_bst(t,alvarez.name, alvarez)
insert_in_bst(t,zinchenko.name, zinchenko)
insert_in_bst(t,kane.name,kane)

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

# find the element(player) 
def find(node:PlayerBST, key:str)->PlayerBST:
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left,key)
    if key > node.key:
        return find(node.right, key)


print(find(t, "alvarez").value.club)

# update element(player) from tree
def update(node, player:Player, key:str)->None:
    p = find(node, key)
    if p is not None:
        p.key, p.value = player.name, player

update(t, Player("Havertz","CHE",26),"alvarez")
print(inorder(t))