# Task:
# develop a in-memory data structure to manage profile information (name, username and email)
# for 100 million users it should allow the following operations to be done efficiently


# 1)State problem clearly, identify the input and output formats
# 1. Insert: the profile information for a new user
# 2. Find:the profile information of a user, givenb their username
# 3. Update: the profile information of a user, given their username
# 4. List: all the profile information of all the users, sorted by username

# 2)Come up with Example I/P and O/Ps
# name = "vivek" email = "vivek@gmail.com"
# name = "vivek" email = "vivek@gmail.com"
# name = "vivek" email = "vivek@gmail.com"

# 1. insert
# 2. find
# 3. update
# 4. list

# 3) comeup with a correct solution. state it in a plain english
# Solution: we will store Users in Sorted list by name
# and variouos functions can be implemmented as:
# 1. Insert: loop through users and insert element in way it keeps the list sorted e.g.('farhan' < 'tushar')
# 2. Find:   loop through the list and find match
# 3. Update: loop through the list and findd matching query and update that user
# 4: List:   return all users 

# 4)Implement the solution and tets with example I/P and O/Ps


# after acknowledging inefficiency of linear datastructure example, 
# we need a structure like bellow given example (Binary-Tree):


'''          ________10________
           /                   \
       ___5___               ___15___
      /       \             /        \
     3         7          12         20
    / \       / \        /  \       /  \
   1   4     6   8     11   13    17   25
              \               \        /
               9              14      19 

            ________Harry________
           /                     \
      ____David____           ____Lily____
     /            \         /            \
   Alex         Emma      James         Sarah
  /   \           /          \            /   \
Adam  Bob     Emily        Jack       Olivia Tom
'''

# for this example we will use Binary-Tree as our data structure
# 1)keys and values: keys are user names and values are User objects, it often reffered as 
# keymap or treemap
# 2) Binary Search Tree: a binary tree in which each node has at most two children,
# the left child is less than the parent and the right child is greater than the parent,
# in other words, the left subtree of a node contains only nodes with keys less than the node's key
# 3) Balanced Tree: a binary tree in which the difference between the height of the left subtree
# and the right subtree is not more than one, in other words, the difference between the height

# Height of a binary tree: the number of leaves in the tree
# for a tree of height k: here's the list of numbers of nodes at each level
'''
    Level 0: 1
    Level 1: 2
    Level 2: 4 i.e. 2^2
    Level 3: 8 i.e. 2^3 
    ...
    Level k-1: 2^(k-1)
    Level k: 2^k

    # here what we are trying to determine is what is a relationship between the height of the tree and
    the total number of nodes in that tree

    if the total number of nodes in tree is n, then it follows that
    N = 1 + 2^1 + 2^2 + 2^3 + ... + 2^(k-1)
    BST time complexity
    N+1=2^ k-1+2 ^k-1

    N+1=> 2^k-1 + 2^k-1
    N+1=> 2*(2^k-1)
    N+1=> 2^1⋅2^k-1
    N+1=> 2^k

    k = log(N+1)

'''


# Q. create a basic tree data structre in python

class Tree():
    def __init__(self,key) -> None:
        self.key = key
        self.left = None
        self.right = None

node0 = Tree(1)
node1 = Tree(0)
node2 = Tree(2)

node0.left = node1
node0.right = node2

# print(node0.left.key)
# print(node0.key)
# print(node0.right.key)

# print(node1.left) # None
# print(node2.righ) # None

 

# Q. implement a binary tree in python and show it's usage with appropriate examples(for given tree)

'''
          ________10________
           /                   \
       ___5___               ___15___
      /       \             /        \
     3         7          12         20
    / \                      \        /
   1   4                     13      17   
'''
# tree1 = (((1,3,4),5,7),10,((None,12,13),15,(17,20,None)))

# def parse_tuple(data):
#     if isinstance(data,tuple) and len(data) == 3:
#         node = Tree(data[1])
#         node.left = parse_tuple(data[0])
#         node.right = parse_tuple(data[2])
#     elif data is None:
#         node = None
#     else:
#         node = Tree(data)
#     return node

# n = parse_tuple(tree1)

# print("   ",n.key)
# print("  ",n.left.key," ",n.right.key)
# print(" ",n.left.left.key,n.left.right.key," ",n.right.left.key,n.right.right.key)
# print(n.left.left.left.key,n.left.left.right.key," ",n.right.left.right.key,n.right.right.left.key)


# # function to display keys back into tuple form
# def display_keys(node, space = '\t', level = 0):
#     if node is None:
#         print(space*level + '*')
#         return
#     if node.left is None and node.right is None:
#         print(space*level + str(node.key))
#         return
    
#     display_keys(node.right,space, level+1)
#     print(space*level + str(node.key))
#     display_keys(node.left,space,level+1)

# display_keys(n)












# practicing simple binary tree
class BinaryTree:
    def __init__(self,key) -> None:
        self.key = key
        self.left = None
        self.right = None
    
node0 = BinaryTree(1)
node1 = BinaryTree(2)
node2 = BinaryTree(3)

node0.left = node1
node0.right = node2
# print(node0.left.key, node0.key, node0.right.key) # 2 1 3 

# taking tree in form of tuple (based on a bellow reference bellow)
'''
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
'''
tup1 = ((1,3,(4,6,7)),8,(None,10,(13,14,None)))

def create_binary_tree(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = BinaryTree(data[1])
        node.left = 