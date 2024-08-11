class LinkedEntry:
    def __init__(self, key, value, rest = None):
        self.key = key
        self.value = value
        self.next = rest 

class DynamicHashtable():
    def __init__(self, size = 10):
        self.table = [None]*size
        self.size = size
        self.num_count = 0

        self.load_factor = 0.75
        self.threshold = min(size*self.load_factor, size-1)
        
    def put(self, key, value):
        hash_code = hash(key) % self.size
        entry = self.table[hash_code]
        
        while entry:
            if entry.key == key:
                entry.value = value
                return
            entry = entry.next

        self.table[hash_code] = LinkedEntry(key, value, self.table[hash_code])
        self.num_count += 1

        if self.num_count >= self.threshold:
            self.resize(2*self.size + 1)
        
    def resize(self, new_size):
        temp_table = DynamicHashtable(new_size)
        for n in self.table:
            while n:
                temp_table.put(n.key, n.value)
                n.next
        self.table = temp_table.table
        self.size = temp_table.size
        self.threshold = self.load_factor * self.size
    
    