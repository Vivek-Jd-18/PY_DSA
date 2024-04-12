# hash table from scratch in python
# handling collision using linear probing 
# replicate python dictionaries


# a dictionaries in python are implemented using a data structure called "hash table",
# it uses a list/arrays to store a key-value pair and uses a hashing function to determine 
# an index for given key to store or retrieve the data associated with it.


# use a  dictionary to store and retireve people's phone number:

# phoneNumber = {
#     'tanishq':'2232222121',
#     'suraj': '3384722635',
#     'mayank':'2293000938'
# }

# fetching a keys
# print(phoneNumber['suraj'])

# adding values
# phoneNumber['om'] = '3384766253'
# print(phoneNumber['om'])


# for i in phoneNumber:
#     print("key: ",i, "value: ",phoneNumber[i])



# Q. objective to implement  HashTable class which supports following operations:
# Insert(a new key-value pair), Find(a value associated with that key), 
# Update(a value associated with that key), List(all keys stored in a hash table)



# Hash Function:
users = [None] * 200

def get_index(word, data_list):
    result = 0
    for char in word:
        data = ord(char)
        result += data
    index = result % len(data_list)
    return index


# index = get_index("hemant", users)

# users[index] = ('hemant','3374655142')

# print(users[index])

MAX_LEN = 4
class BasicHashTable:
    def __init__(self, max_len = MAX_LEN) -> None:
        self.hash_table = [None] * max_len
    
    def insert(self, key, value):
        index = get_index(key, self.hash_table)
        self.hash_table[index] = key, value

    def update(self, key, value):
        index = get_index(key, self.hash_table)
        self.hash_table[index] = key, value

    def find(self, key):
        index = get_index(key,self.hash_table)
        kv = self.hash_table[index]
        if kv is not None:
            key, value = kv
            return kv
        else:
            return None
    
    def get_all(self):
        return (ele for ele in self.hash_table if ele is not None)


hash_instance = BasicHashTable()

hash_instance.insert("vivek", '7990226787')
hash_instance.insert("jovian", '3384766354')
hash_instance.insert("tambien", "3384756654")
hash_instance.insert("yohan", "0098765437")

# print(hash_instance.find("vivek"))
hash_instance.update("tambien","000000000")
for i in hash_instance.get_all():
    print(i)


# there wil be a cases where collisions will occur, like in given case
print(get_index("listen", users), get_index("silent",users)) # 55,55

# we will use linear probing for it
