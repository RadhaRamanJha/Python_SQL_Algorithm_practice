class Entry:
    def __init__(self, key, value) -> None:
        self.key = key         # key to access the value of an entry 
        self.value = value     # value assosiated with an entry

class HashTable:
    def __init__(self, size = 15) -> None:
        self.table = [None]*size        # Hash table to store all values
        self.size = size                # Size of Hash table
    
    def get(self, key):                 # Locate the entry assosiated with the hashed key
                                        # (to be calculated !) and return value if already present

        hash_code = hash(key) % self.size                   # index calculated for the entered key
        return self.table[hash_code].value if self.table[hash_code] else None # return the value if present
                                                                                    # if not return None 
    
    def put(self, key, value):         # Calculates the hashed value for the key entered
                                       # if Hash index already present over writes the value
                                       # else stores a new entry

        hash_code = hash(key) % self.size                   # Calculate the hashed index for entry
        entry = self.table[hash_code]                       # Locates the entry assosiated with the hash code
        if entry:
            if entry.key == key:      
                entry.value = value    # Overwrites the value if the key value is already present                          
            else:
                raise RuntimeError('Key Collision: {} and {}'.format(key, entry.key))
                                       # Raises runtime error if the hash value of 
                                       # entred key and a key already present are same
                                       # but entered key and key already present are not the same
        else:
            self.table[hash_code] = Entry(key, value)       # New entry 

table = HashTable(25)
table.put("August",31)
table.put("June", 30)
table.put("January",31)
print(table.get("September"))
print(table.get("June"))

## Open addressing implementation of Hashtable
class open_address_HashTable():
    def  __init__(self, size):
        self.table = [None]*size
        self.size = size
        self.Key_numbers = 0           # To keep runnning count of number of keys so that we donot runout of empty bukets in hash table
    
    def get(self, key):                                    # The modification in this get function
        hash_code = hash(key)%self.size
        while self.table[hash_code]:     
            if self.table[hash_code].key == key:
                return self.table[hash_code].value
            hash_code = (hash(key)+1) % self.size
        return None

    def put(self, key, value):
        hash_code = hash(key) % self.size
        while self.table[hash_code] :
            if self.table[hash_code].key == key :
                self.table[hash_code].value = value
                return
            hash_code = ( hash_code + 1 ) % self.size

        if self.Key_numbers >= self.size - 1 :
            raise RuntimeError("Table is Full")
        
        self.table[hash_code] = Entry(key, value)
        self.N += 1
