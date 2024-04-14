# collision avoidance with linear probing
MAX_LEN = 10
# hash_map = [None] * MAX_LEN

# normal indexing
def get_index(key:str, list)->int:
    res = 0
    for i in key:
        res += ord(i)
    index = res % len(list)
    return index

def get_probing_index(key, list):
    index = get_index(key, list)
    
    while True:
        key_val = list[index]
        if key_val is None:
            return index
        k,v = key_val
        if k == key:
            return index
        index += 1 

        if len(list) == index:
            index = 0

class HashMap:
    def __init__(self, max_len = MAX_LEN):
        self.hash_data = [None] * max_len
    
    def insert(self, key, value):
        i = get_probing_index(key, self.hash_data)
        self.hash_data[i] = key, value
    
    def insert(self, key, value):
        i = get_probing_index(key, self.hash_data)
        self.hash_data[i] = key, value
    
    def find(self, key):
        i = get_probing_index(key,self.hash_data)
        return self.hash_data[i]
    
    def get_all(self):
        return (data for data in self.hash_data if data is not None)

hash_map = HashMap()
hash_map.insert("virat",18)
hash_map.insert("smith",27)
hash_map.insert("kane",10)
hash_map.insert("rohit",45)
for i,j in hash_map.get_all():
    print("key: ",i," value: ",j) 

print(hash_map.find("virat"))



# Hash Table Improvements
 