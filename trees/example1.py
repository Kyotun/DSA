class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        # You can check if it's already exists.
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = ' ' * self.get_level()
        
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    
def build_product_tree():
    root = TreeNode(data="Electronics")
    
    laptop = TreeNode(data="Laptop")
    laptop.add_child(TreeNode(data="Mac"))
    laptop.add_child(TreeNode(data="Surface"))
    laptop.add_child(TreeNode(data="Thinkpad"))
    
    cellphone = TreeNode(data="Cell Phone")
    cellphone.add_child(TreeNode(data="iPhone"))
    cellphone.add_child(TreeNode(data="Google Pixel"))
    cellphone.add_child(TreeNode(data="Vivo"))
    
    tv = TreeNode(data="TV")
    tv.add_child(TreeNode(data="Samsung"))
    tv.add_child(TreeNode(data="LG"))
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    return root
    