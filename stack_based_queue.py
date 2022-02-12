from typing import Any


class Queue:
    def __init__(self) -> None:
        self.inboud_stack = []
        self.outbound_stack = []

    def enqueue(self, data:Any):
        self.inboud_stack.append(data)

    def dequeue(self) -> Any:
        if not self.outbound_stack:
            while self.inboud_stack:
                self.outbound_stack.append(self.inboud_stack.pop())

        return self.outbound_stack.pop()
