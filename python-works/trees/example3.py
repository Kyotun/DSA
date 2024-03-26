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
    
    def print_indent(self):
        indent = '|'
        if self.get_level() == 1:
            return indent
        for level in range(self.get_level()-1):
            indent += '|' + ' ' * 3
        return indent
    
    def print_tree(self, level:int):
        if self.get_level() > level:
            return
        preifx = self.print_indent()
        if self.parent:
            preifx += "|___"
        print(preifx + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)
    
def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root
    
if __name__ == '__main__':
    root = build_location_tree()
    root.print_tree(level=2)