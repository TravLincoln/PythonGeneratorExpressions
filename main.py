# Generator Expression = Similar to list comprehension but uses () instead of []
#                        Creates a generator (iterator) that yields values one at a time
#                        No need to define a function or use yield
#                        Less flexible than a general function and not reusable
#                        Useful when reading a file
#                        object = (expression for value in iterable if condition)


number = int(input("Enter a number to square up to: "))

even_squares = (x ** 2 for x in range(1, number + 1) if x % 2 == 0)

for square in even_squares:
    print(square)



'''
file_path = "C:\\Users\\travi\\OneDrive\\Documents\\TLOR.txt"

with open(file_path) as file:
    lines = (line.strip() for line in file)
    for line in lines:
        print(line)
'''



'''

number = int(input("Enter a number to count up to: "))

# object name will be counter
counter = (count for count in range(1, number + 1))

for n in counter:
    print(n)
'''