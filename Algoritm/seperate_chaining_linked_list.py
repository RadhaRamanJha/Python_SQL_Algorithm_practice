class LinkedEntry:
    def __init__(self, key, value, rest = None):
        self.key = key
        self.value = value
        self.next = rest      # optional parameter which allows a newly created key value pair
                              # to get linked directly to the list which is already pointed to by rest

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

    def remove(self,key):
        hash_code = hash(key) % self.size
        entry = self.table[hash_code]                     # self.table[hash_code] - refers the first entry in linked list 
                                                          # assosiated with hash code
        prev = None
        while entry:                                      # Iterate as long as there are entries in the Linked List
            if entry.key == key:                          # Locate entry by comparing target key with key field of entry
                if prev:
                    prev.next = entry.next                # When found, if there is prev reference, 
                                                          # link around entry hence removing it from Linked List
                else:
                    self.table[hash_code] = entry.next    # set the linked list first entry to second node in Linked List
    
                self.key_counts -= 1                      # Decrement count of entries, N.
                return entry.value                        # Return the value of assosiated with the entry being removed
        
            prev, entry = entry, entry.next               # if key is not found continue iterating by
                                                          # setting prev to entry and entry to entry.next
        return None
    
    def __iter__(self):
        for entry in self.table:
            while entry:
                yield (entry.key, entry.value)
                entry = entry.next