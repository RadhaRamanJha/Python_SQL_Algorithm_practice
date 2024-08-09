class LinkedEntry:
    def __init__(self, key, value, rest = None):
        self.key = key
        self.value = value
        self.next = rest      # optional parameter which allows a newly created to to get linked directly to the list which is already pointed to by rest

# Seperate Chaining implementation of Hash Table
class HashTable():
    def __init__(self, size = 15):
        self.table = [None]*size
        self.size = size
        self.key_counts = 0
    
    def get(self, key):
        hash_code = hash(key) % self.size
        entry = self.table[hash_code]
        while entry:
            if entry.key == key :
                return entry.value
            entry = entry.next
        return None
    
    def put(self, key, value):
        hash_code = hash(key) % self.size
        entry = self.table[hash_code]
        while entry:
            if entry.key == key:
                entry.value = value
                return
            entry = entry.next

        self.table[hash_code] = LinkedEntry(key, value, self.table[hash_code])
        self.key_counts += 1