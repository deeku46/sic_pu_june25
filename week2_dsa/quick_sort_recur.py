def quick_sort(array,low,high):
    if low<high:
        pivot_index = partition(array,low,high)
        quick_sort(array,low,pivot_index-1)
        quick_sort(array,pivot_index+1,high)

def partition(array,low,high):
    pivot = array[low]
    key = low+1
    for i in range (low+1,high+1):
        if array[i]<pivot:
            array[key],array[i]=array[i],array[key]
            key+=1
    array[low],array[key-1]=array[key-1],array[low]
    return key-1

array = list(map(int, input("Enter the elements: ").split()))
low = 0
high = len(array)-1
quick_sort(array,low,high)
print("Sorted array = ",array)