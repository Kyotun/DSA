from collections import deque

class Stack:
    def __init__(self) -> None:
        self.container = deque()
    
    def push(self,val) -> None:
        self.container.append(val)
    
    def pop(self) -> None:
        if len(self.container) == 0:
            raise Exception("Container is empty.")
        return self.container.pop()
        
    def peek(self):
        if len(self.container) == 0:
            raise Exception("Container is empty.")
        return self.container[-1]
    
    def is_empty(self) -> bool:
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def get_sentence(self):
        sentence = ""
        for index in self.container:
            sentence += index
        return sentence
            
def reverse_string(string):
    my_stack = Stack()
    for char in string:
        my_stack.push(val=char)
        
    rstr = ""
    while my_stack.size() != 0:
        rstr += my_stack.pop()
    return rstr

def is_balanced(string) -> bool:
    my_dict = {
        '(':')',
        '{':'}',
        '[':']'
    }
    my_stack = Stack()
    for char in string:
        if char in my_dict:
            my_stack.push(val=char)
        elif my_dict[my_stack.pop()] != char or my_stack.size == 0:
            return False
    return my_stack.is_empty()
    