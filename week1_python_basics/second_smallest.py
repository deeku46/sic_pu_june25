number = int(input("Enter the number "))
str_num = str(number)
min = 10
sec_min = 10
for i in str_num:
    d = int(i)
    if d < min:
        sec_min = min
        min = d
    elif min < d < sec_min:
        sec_min = d
print("Second smallest digit is", sec_min)
