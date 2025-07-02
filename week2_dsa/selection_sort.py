array = list(map(int,input("Enter the array elements: ").split()))
for i in range (1,len(array)):
    element = array[i-1]
    position = i-1
    for j in range (i-1,len(array)):
        if array[j]<element:
            element = array[j]
            position = j
    array[position],array[i-1]=array[i-1],array[position]
print("Sorted array = ",array)