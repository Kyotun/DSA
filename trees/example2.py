class TreeNode:
    def __init__(self, name:str, designation:str) -> None:
        self.name = name
        self.designation = designation
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
    
    def decide_print_form(self, call:str):
        if call == "name":
            return self.name
        elif call == "designation":
            return self.designation
        elif call == "both":
            return self.name + '(' + self.designation + ')'
        else:
            raise Exception("Unvalid command. Valid commands -> 'name', 'designation', 'both'.")
        
    def print_tree(self, call:str):
        preifx = self.print_indent()
        if self.parent:
            preifx += "|___"
        to_print = self.decide_print_form(call=call)
        print(preifx + to_print)
        if self.children:
            for child in self.children:
                child.print_tree(call)
    
def build_product_tree():
    ceo = TreeNode(name="Nilupul", designation="CEO")

    cto = TreeNode(name="Chinmay", designation="CTO")
    infra_head = TreeNode(name="Vishwa", designation="Infrastructure Head")
    cloud_manager = TreeNode(name="Dhaval", designation="Cloud Manager")
    app_manager = TreeNode(name="Abhijit", designation="App Manager")
    
    application_head = TreeNode(name="Aamir", designation="Application Head")

    hr_head = TreeNode(name="Gels", designation="HR Head")
    recruitment_manager = TreeNode(name="Peter", designation="Recruitment Manager")
    policy_manager = TreeNode(name="Waqas", designation="Policy Manager")
    
    ceo.add_child(child=cto)
    ceo.add_child(child=hr_head)
    
    cto.add_child(child=infra_head)
    cto.add_child(child=application_head)
    hr_head.add_child(child=recruitment_manager)
    hr_head.add_child(child=policy_manager)
    
    infra_head.add_child(child=cloud_manager)
    infra_head.add_child(child=app_manager)
    
    return ceo
    
if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree(call="asd")