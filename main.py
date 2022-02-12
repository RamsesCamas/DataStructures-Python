from my_array import Array
from my_array2D import Grid

def test_array():
    size_array = int(input('Enter the size of the array: '))
    menu = Array(size_array)
    print(menu.__len__())
    for i in range(menu.__len__()):
        menu[i] = i**3

    print(menu.__str__())
    print(menu.__getitem__(4))
    menu.__setitem__(3,100)
    print(menu.__str__())


def test_grid():
    matrix = Grid(3,3)
    for row in range(matrix.get_height()):
        for column in range(matrix.get_width()):
            matrix[row][column] = row * column
    print(matrix.__str__())
    print(f'Matrix Height {matrix.get_height()}')
    print(f'Matrix Width {matrix.get_width()}')
    print(matrix.__getitem__(2)[1])


if __name__ == '__main__':
    test_grid()