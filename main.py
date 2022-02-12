from my_array import Array
from my_array2D import Grid
from my_cube import Cube


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

def test_cube():
    cube = Cube(3,3,3)
    for row in range(cube.get_height()):
        for column in range(cube.get_width()):
            for depth in range(cube.get_depth()):
                cube[row][column][depth] = row + column + depth + 1

    print(cube.__str__())
    print(f'Cube Height {cube.get_height()}')
    print(f'Cube Width {cube.get_width()}')
    print(cube.__getitem__(2)[1])
    print(cube.__getitem__(2)[1][2])


if __name__ == '__main__':
    test_cube()