from datetime import datetime
def recursive_insertion_sort(array, n):
    if n <= 1:
        return
    recursive_insertion_sort(array, n - 1)
    key = array[n - 1]
    j = n - 2
    while j >= 0 and array[j] > key:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key
array = list(map(int, input("Enter the elements: ").split()))
start_time = datetime.now()
recursive_insertion_sort(array, len(array))
end_time = datetime.now()
print("Sorted array:", array)
print("Time taken:", end_time - start_time)
