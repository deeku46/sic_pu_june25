num = int(input("Enter a positive integer: "))
if num > 0 and int(num ** 0.5) ** 2 == num:
    print("Perfect Square")
else:
    print("Not a Perfect Square")
