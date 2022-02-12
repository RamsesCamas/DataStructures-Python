from typing import Any
from node import TwoWayNode
#This version has a O(!) complexity
class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data:Any):
        new_node = TwoWayNode(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.count += 1
    
    def dequeue(self) -> Any:
        current = self.head

        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None

        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

        return current.data