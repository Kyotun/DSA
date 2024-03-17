class BinarySearchTreeNode:
    def __init__(self, data:int) -> None:
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, child:int):
        if self.data == child:
            return
        
        if self.data > child:
            self.left = child
        else:
            self.right = child