# Accept a number from user and print its math table
input_number = int(input("Enter a number to print its math table: "))
for i in range(1,11):
    print('%2d * %02d = %03d'%(input_number,i,input_number*i))