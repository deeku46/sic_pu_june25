def sum_of_digits(number):
    if number == 0:
        return 0
    return (number % 10) + sum_of_digits(number // 10)


user_number = int(input("Enter a number: "))
result = sum_of_digits(user_number)
print("Sum of digits:", result)
