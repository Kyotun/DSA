from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Buffer is empty.")
        return self.buffer.pop()
    
    def is_empty(self) -> bool:
        return len(self.buffer) == 0
    
    def size(self) -> int:
        return len(self.buffer)

my_queue = Queue()

def place_order(user_list):
    for element in user_list:
        print("Incoming order: ", element)
        my_queue.enqueue(val=element)
        time.sleep(0.5)

def serve_order():
    time.sleep(1.0)
    while my_queue.is_empty() == False:
        print("Now serving:", my_queue.dequeue())
        time.sleep(2.0)

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve_order)

    t1.start()
    t2.start()
        
        