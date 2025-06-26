number=int(input("Enter the number "))
str_num=str(number)
max=str_num[0]
for i in str_num:
    if i >= max:
        max = i
print("Maximum number is = ",max)
