class BinarySearchTreeNode:
    def __init__(self, data:int) -> None:
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, child:int):
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
    
    def find_min(self) -> int:
        if self.left:
            return self.left.find_min()
        return self.data
    
    def find_max(self) -> int:
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
    # countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    # country_tree = build_tree(countries)

    # print("UK is in the list? ", country_tree.search("UK"))
    # print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())
            