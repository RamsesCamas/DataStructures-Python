from typing import Any
from my_array import Array

class Cube(object):
    def __init__(self,rows:int, columns:int, depth: int, fill_value=None) -> None:
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns)
            for column in range(columns):
                self.data[row][column] = Array(depth, fill_value)

    def get_height(self) -> int:
        return len(self.data)

    def get_width(self) -> int:
        return len(self.data[0])

    def get_depth(self) -> int:
        return len(self.data[0][0])
    
    def __getitem__(self, index:int) -> Any:
        return self.data[index]

    def __str__(self) -> str:
        result = ''
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                for depth in range(self.get_depth()):
                    result += str(self.data[row][column][depth]) + ' '
            result += '\n'
        
        return str(result)