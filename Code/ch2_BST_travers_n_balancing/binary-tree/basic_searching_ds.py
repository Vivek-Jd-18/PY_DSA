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

class User:    
    def __init__(self,username,name,email) -> None:
        self.username = username
        self.name = name
        self.email = email
    
    def __repr__(self) -> str:
        return "User(username:{}, name:{}, email:{}) ".format(self.username,self.name, self.email)
    
    def __str__(self) -> str:
        return self.__repr__()
    

class UserDB:

    def __init__(self) -> None:
        self.users = []        
    
    def insert(self,user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i+=1
        self.users.insert(i,user)

    def get(self, username):
        for i in self.users:
            if username == i.username:
                return i

    def update(self, user):
        u = self.get(user.username)
        u.name = user.name
        u.email = user.email

    def list(self):
        return self.users
    
# creating users
yuvraj = User(username="yuvi",name="yuvaraj",email="yuvi3@gmail.com")
raina = User("raina","raina","raina3@gmail.com")
sehwag = User("sehi","sehwag","seh11@gmail.com")
irfaan = User("irfaan","irfaan","irfan8@gmail.com")

# print(yuvraj,'\n',raina,'\n',sehwag,'\n',irfaan)

# creating db instance
db = UserDB()

#inserting user in db
db.insert(yuvraj)
db.insert(raina)
db.insert(sehwag)
db.insert(irfaan)

# listing all users
print(db.list())

# getting single user
print(db.get('sehi'))

# updating user
sehwag2 = User(username = "sehi",name = "sehwag 2",email = "sehi@gmail.com")
db.update(sehwag2)
print(db.get('sehi'))

print(db.list())




# 5) Analyze algorithms complexities and identify inefficiencies 
# thus the complexities of all operatrions are as:
# 1. insert: O(n) 
# 2. get:    O(n)
# 3. update: O(n)
# 4. list:   O(n)

# result: above given solution is so inefficient: assume would it be betteer to travers all 
# 10 million users for every opearions??

# Exercise/Requirement/Assignment : verify that the time complexity of each opearion is O(1) 

# we need a structure like bellow given example (Binary-Tree):

#             ________10________
#            /                   \
#        ___5___               ___15___
#       /       \             /        \
#      3         7          12         20
#     / \       / \        /  \       /  \
#    1   4     6   8     11   13    17   25
#               \               \        /
#                9              14      19 

#             ________Harry________
#            /                     \
#       ____David____           ____Lily____
#      /            \         /            \
#    Alex         Emma      James         Sarah
#   /   \           /          \            /   \
# Adam  Bob     Emily        Jack       Olivia Tom

