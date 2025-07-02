def binary_search(array, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if key == array[mid]:
        return mid
    elif key < array[mid]:
        return binary_search(array, key, low, mid - 1)
    else:
        return binary_search(array, key, mid + 1, high)

array = list(map(int, input("Enter the elements: ").split()))
key = int(input("Enter the key: "))
array.sort() 
low = 0
high = len(array) - 1

result = binary_search(array, key, low, high)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
