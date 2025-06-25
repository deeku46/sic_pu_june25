a,b,c = input("Enter the 3 distinct numbers").split()
a = int(a)
b = int(b)
c = int(c)
if a <= b and a<=c:
    print("{} is the smallest number".format(a))
elif b <= a and b <= c:
    print("{} is the smallest number".format(b))
else:
    print("{} is the smallest number".format(c))