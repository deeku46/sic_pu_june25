number = input("Enter a number: ")
sum_odd_position_even_digits = 0
length = len(number)

for i in range(length):
    position = length - i
    digit = int(number[i])
    if position % 2 != 0 and digit % 2 == 0:
        sum_odd_position_even_digits += digit

print(sum_odd_position_even_digits)
