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


# Expression data steucture to represent mathematical expression
class Value:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
    def eval(self):
        return self.value
    
class Expression:
    def __init__(self, function, left, right):
        self.function = function
        self.left = left
        self.right = right
    
    def __str__(self):
        return '( {}{}{} )'.format(self.left, self.function.__doc__, self.right)
    
    def eval(self):
        return self.function(self.left.eval(), self.right.eval())
    
def add(left, right):
    """ + """
    return left+right
def mul(left, right):
    """ * """
    return left*right

a = Expression(add, Value(4), Value(5))
b = Expression(mul, a, Value(9))
c = Expression(mul, a, b)
print(c, '=', c.eval())
