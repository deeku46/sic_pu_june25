n=int(input("Enter the size of the triangle: "))
for i in range(n):
    for j in range(n):
        if i+j>=n:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    for k in range(i-1):
        print("*",end=" ")
    print()