# 1) balanced binary tree: A balanced binary tree is a binary tree in which the height of the left and right
#  subtrees of any node differ by not more than 1. This means that the tree is roughly the same height on all
#  sides, which makes it efficient for operations such as searching, insertion, and deletion.

# 2) binary search tree: A binary search tree (BST) is a rooted binary tree data structure with the key of each
#  internal node being greater than all the keys in the respective node's left subtree and less than the ones in
#  its right subtree. The time complexity of operations on the binary search tree is linear with respect to the height of the tree.

# 3) balanced binary search tree: A balanced binary search tree is a binary search tree in which the height of the
#  left and right subtrees of any node differ by not more than 1.

# 1) balanced binary search tree + 2) binary search tree => balanced binary search tree


# Question : make a BALANCED BINARY SEARCH TREE from given sorted list of key value pairs

class Player:
    def __init__(self, name, club, age):
        self.name = name
        self.club = club
        self.age = age
    
    def __repr__(self) -> str:
        return "PLAYER(name:{},club:{},age:{})".format(self.name,self.club,self.age)

    def __str__(self) -> str:
        return self.__repr__()


# structure to store player in (--LINEAR-MANNER--)
class PlayerDB:
    def __init__(self):
        self.players:list[Player] = []
    
    def insert(self, player:Player):
        i = 0
        while i < len(self.players):
            if player.name < self.players[i].name:
                break
            i+=1
        self.players.insert(i,player)
    
    def list(self):
        return self.players
    
    def update(self, player:Player):
        target:Player = self.find(player.name)
        target.club, target.age = player.club, player.age

    def find(self, name)->Player:
        return next((p for p in self.players if p.name == name), None)

martinelli = Player("martinelli","arsenal",24)
rashford = Player("rashford","manchester united",24)
gernacho = Player("gernacho","manchester united",22)
saka = Player("saka","arsenal",22)
jesus = Player("jesus","manchester city",27)

db = PlayerDB()
print("initial list: ",db.list())
db.insert(martinelli)
db.insert(rashford)
db.insert(gernacho)
db.insert(saka)
db.insert(jesus)
print(db.find("martinelli"))
db.update(Player("martinelli","arsenal",25))
print("after populating",db.list())

print([d.name, d for d in db])