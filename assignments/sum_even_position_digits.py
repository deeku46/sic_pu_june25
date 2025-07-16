number = input("Enter a number: ")
sum_even_position = 0
length = len(number)

for i in range(length):
    position = length - i
    digit = int(number[i])
    if position % 2 == 0:
        sum_even_position += digit

print(sum_even_position)
