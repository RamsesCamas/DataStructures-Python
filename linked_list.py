from typing import Any

from numpy import delete
from node import Node

class SinglyLinkedList():

    def __init__(self) -> None:
        self.tail: Node = None
        self.size:int = 0

    def append(self, data:Any):
        node = Node(data)

        if self.tail == None:
            self.tail = node
        else:
            current: Node = self.tail

            while current.next:
                current = current.next
            current.next = node
        self.size += 1
    
    def size(self) -> str:
        return str(self.size)

    def iter(self) -> Any:
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val
        
    def delete(self, data:Any) -> Any:
        current = self.tail
        previous = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data
            previous = current
            current = current.next

    def search(self,data: Any):
        found = False 
        for node in self.iter():
            if data == node:
                print(f'Data {data} found')
                found = True
                break

        if not found:
            print(f'Data not found')

    def clear(self):
        self.tail = None
        self.head = None
        self.size = None