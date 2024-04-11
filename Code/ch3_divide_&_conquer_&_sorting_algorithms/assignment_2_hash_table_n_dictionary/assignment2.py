# hash table from scratch in python
# handling collision using linear probing 
# replicate python dictionaries


# a dictionaries in python are implemented using a data structure called "hash table",
# it uses a list/arrays to store a key-value pair and uses a hashing function to determine 
# an index for given key to store or retrieve the data associated with it.


# use a  dictionary to store and retireve people's phone number:

phoneNumber = {
    'tanishq':'2232222121',
    'suraj': '3384722635',
    'mayank':'2293000938'
}

# fetching a keys
# print(phoneNumber['suraj'])

# adding values
phoneNumber['om'] = '3384766253'
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


index = get_index("uno", users)

users[index] = 