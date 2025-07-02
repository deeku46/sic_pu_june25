N = int(input('Enter number of elements of the array: '))
try:
    numbers = [float(num) for num in input().split()]
    print(numbers)
except ValueError as err:
    print("Ypu may have entered an invalid float number")
numbers.sort