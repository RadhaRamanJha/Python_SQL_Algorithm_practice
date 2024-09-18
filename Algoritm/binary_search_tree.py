class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        self.root = self._add_newnode(self.root, value)
    
    def _add_newnode(self, node, value):
        if node is None:
            self.root = BinaryNode(value)
        
        if value <= node.value:
            node.left = self._add_newnode(node.left, value)
        
        elif value >= node.value:
            node.right = self._add_newnode(node.right, value)
        
        return node

    def __contains__(self, target):
        """Determing wheter binary search tree contains a value iterativly"""
        node = self.root
        while node:
            if target == node.value:
                return True
            
            if target < node.value:
                node = node.left
            
            else:
                node = node.right
        return False
    
    def _remove_min(self, node):
        """Helper funcction to remove the minimum value"""
        if node.left is None:
            return node.right
        node.left = self._remove_min(node.left)
        return node
    
    def remove(self, value):
        self.root = self._remove(self.root, value)
    
    def _remove(self, node, value):
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._remove(node.left, value)

        elif value > node.value:
            node.right = self._remove(node.right, value)
        
        else: 
            if node.left is None: 
                return node.right
            
            if node.right is None: 
                return node.left
            
            orignal = node

            node = node.right

            while node.left:
                node = node.left

        
        node.right = self._remove_min(orignal.right)
        node.left = orignal.left
        
        return node