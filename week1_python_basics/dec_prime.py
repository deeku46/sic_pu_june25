n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))
for i in range (m,n,-1):
    num=0
    for j in range(2,i):
        if i%j == 0:
             num+=1
    if num == 0:
        print(i, end=' ')