n = int(input("Enter the size of the Rhombus: "))
for i in range(n):
    for j in range(n):
        if i+j==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for k in range(i-1):
        if k == i-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n-2,0,-1):
    for j in range(n):
        if i+j==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for k in range(i-1):
        if k ==i-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()