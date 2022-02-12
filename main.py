from my_array import Array


size_array = int(input('Enter the size of the array: '))
menu = Array(size_array)
print(menu.__len__())
for i in range(menu.__len__()):
    menu[i] = i**3

print(menu.__str__())
print(menu.__getitem__(4))
menu.__setitem__(3,100)
print(menu.__str__())