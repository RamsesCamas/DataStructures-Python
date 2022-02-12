from typing import Any
from my_array import Array

class Grid():
    def __init__(self,rows: int, columns:int, fill_value:Any=None) -> None:
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self) -> int:
        return len(self.data)

    def get_width(self)-> int:
        return len(self.data[0])

    def __getitem__(self,index:int) -> Any:
        return self.data[index]

    def __str__(self) -> str:
        result = ''

        for row in range(self.get_height()):
            for column in range(self.get_width()):
                result += str(self.data[row][column]) + ' '
            result += '\n'
        
        return str(result)