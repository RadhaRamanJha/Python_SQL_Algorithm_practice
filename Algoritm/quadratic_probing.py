class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class alt_open_address:
    def __init__(self, N = 1):
        self.size = 2**N
        self.table = [None]*self.size
        self.key_numbers = 0
        self.existing_keys = set() # Declare a set to store existing keys
    
    def put(self, key, value):
        num = 0
        hash_code = hash(key) % self.size
        
    
        # if self.key_numbers >= self.size-1:
        #     raise RuntimeError("The hash table is full")
        
        while self.table[hash_code] :
            if self.table[hash_code].key == key:  # To Handle :- Table full updating key value 
                self.table[hash_code].value = value # To Handle :- Table full adding a new key value 
                return
            num += 1
            hash_code = self.update_hash_code(hash_code, num)

        # if self.key_numbers >= self.size-1:
        #     raise RuntimeError("The hash table is full")
        
        self.table[hash_code] = Entry(key, value)
        self.existing_keys.add(key)        # add the key of dictionary in set 
        self.key_numbers += 1
            
        
    def get(self, key):
        num = 0
        hash_code = hash(key) % self.size
        while self.table[hash_code]:
            if self.table[hash_code].key == key:
                return self.table[hash_code].value
            num += 1
            hash_code = self.update_hash_code(hash_code, num)
        return None
    
    def update_hash_code(self, hash_code, num):
        delta = num*(num+1)/2
        hash_code = (hash_code + delta) % self.size
        return hash_code