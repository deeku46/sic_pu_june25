number = input("Enter a number: ")
largest = 0

for digit in number:
    d = int(digit)
    if d > largest:
        largest = d

print(largest)
