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
                
    def in_order_traversel(self):
        elements = []
        
        if self.left:
            elements += self.in_order_traversel()
        
        elements.append(self.data)
        
        if self.right:
            elements += self.in_order_traversel()
        
        return elements
            