number = int(input("Enter the number: "))
str_num = str(number)
count = 0
for i in str_num:
    d = int(i)
    if d > 1:
        n = 0
        for j in range(2, d):
            if d % j == 0:
                n += 1
        if n == 0:
            count += 1
print("Number of prime digits are =", count)
