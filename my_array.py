from typing import Any, Iterator


class Array:
    def __init__(self, capacity: int, fill_value:Any =None) -> None:
        self.items = list()
        for _ in range(capacity):
            self.items.append(fill_value)

    def __len__(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)

    def __iter__(self) -> Iterator:
        return iter(self.items)

    def __getitem__(self, index:int) -> Any:
        return self.items[index]

    def __setitem__(self, index:int, new_item:Any):
        self.items[index] = new_item