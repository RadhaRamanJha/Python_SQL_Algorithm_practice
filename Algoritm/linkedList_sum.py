class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
# Iterative sum
def iterative_sum(n):
    total = 0
    while n:
        total += n.value
        n = n.next
    return total

# Recurssive sum
def recursive_sum(n):
    if n is None:
        return 0
    return n.value + recursive_sum(n.next)