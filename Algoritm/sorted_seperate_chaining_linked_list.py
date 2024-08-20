class LinkedEntry:
    def __init__(self, key, value, rest = None ):
        self.key = key
        self.value = value
        self.next = rest
class HashTable_variant():
    def __init__(self, size = 10):
        self.table = [None]*size
        self.size = size
        self.key_counts = 0

    def get(self, key):
        hash_code = hash(key)%self.size
        entry = self.table[hash_code]
        while entry:
            if entry.key == key:
                return entry.value

