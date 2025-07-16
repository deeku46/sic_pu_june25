number = input("Enter a number: ")
unique_digits = []

for digit in number:
    digit = int(digit)
    if digit not in unique_digits:
        unique_digits.append(digit)

for i in range(len(unique_digits)):
    for j in range(i + 1, len(unique_digits)):
        if unique_digits[j] < unique_digits[i]:
            unique_digits[i], unique_digits[j] = unique_digits[j], unique_digits[i]

if len(unique_digits) < 2:
    print("No second smallest digit")
else:
    print(unique_digits[1])
    