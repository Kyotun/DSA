class BinarySearchTreeNode:
    def __init__(self, data:int) -> None:
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, child):
        if self.data == child:
            return
        
        if self.data > child:
            if self.left:
                self.left.add_child(child)
            else:
                self.left = BinarySearchTreeNode(data=child)
        else:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = BinarySearchTreeNode(child)
                
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
            
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        if self.right:
            elements += self.right.in_order_traversal()
            
        elements.append(self.data)
        return elements
    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        
        if self.left:
            elements += self.left.in_order_traversal()
            
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements
        
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val=val)
            else:
                return False
        elif val > self.data:
            if self.right:
                return self.right.search(val=val)
            else:
                return False
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
            
                
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data
    
    def calculate_sum(self) -> int:
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()
        
        sum += self.data
        
        if self.right:
            sum += self.right.calculate_sum()
        
        return sum
        
            
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range (1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.pre_order_traversal())
            