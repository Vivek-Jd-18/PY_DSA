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
# print("initial list: ",db.list())
db.insert(martinelli)
db.insert(rashford)
db.insert(gernacho)
db.insert(saka)
db.insert(jesus)
# print(db.find("martinelli"))
db.update(Player("martinelli","arsenal",25))
# print("after populating",db.list())

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

data = ([(d.name, d) for d in db.list()])

class PlayerNode:
    def __init__(self, key:str, value:Player) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def make_balanced_bst(data:list[PlayerNode], low = 0, high = None, parent = None):
    if high is None:
        high = len(data)-1
    if low > high:
        return None
    
    mid = (low + high) // 2
    key, value = data[mid]
    root = PlayerNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, low, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, high, root)

    return root

bbst = make_balanced_bst(data)
# display_keys(bbst)

# Practiced ::
# def make_balanced_bst2(data, low=0, high=None, parent=None):
#     if high is None:
#         high = len(data)-1
#     if low > high:
#         return None
#     mid = (low+high) // 2
#     key, value = data[mid]

#     root:PlayerNode = PlayerNode(key, value)
#     root.left = make_balanced_bst2(data, low, mid-1, parent)
#     root.right = make_balanced_bst2(data, mid+1, high, parent)
#     root.parent = parent

#     return root

# display_keys(make_balanced_bst2(data))


# Overview of Complexities of Balanced binary Search Tree:

# - Insertion: O(n) + O(log n) = O(n) , because we first have to sort the data O(n) before inserting it in balanced binary search tree O(log n)
# - update   : O(log n)
# - find(search an element) = O(log n)
# - list all : O(n)

# we can overcome insertion complexity which is O(n), we can perform balancing peridically, 
# assuming we can balance our tree at each 1000th insertion. or balancing it at every each hour

# so what's the real imporvement between O(n) and O(log n) ??

# lets try it out

# suppose we have 100 million users to keep record of

import math
import time

print(math.log(100000000, 2))

start_time = time.time()
for i in range(26):
    j = i
end_time = time.time()
time_taken_bbst = end_time - start_time

print("bbst: {:.9f} seconds".format(time_taken_bbst))
# bbst: 0.000003338 seconds

start_time = time.time()
for i in range(100000000):
    j = i
end_time = time.time()
time_taken_linear = end_time - start_time

print("linear: {:.9f} seconds".format(time_taken_linear))
# linear: 6.639140606 seconds

# this is 300,000 faster than linear approach


