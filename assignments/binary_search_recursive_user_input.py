def binary_search(array, target, low, high):
    if low > high:
        return -1

    middle = (low + high) // 2

    if array[middle] == target:
        return middle
    elif array[middle] < target:
        return binary_search(array, target, middle + 1, high)
    else:
        return binary_search(array, target, low, middle - 1)


user_input = input("Enter sorted numbers separated by spaces: ")
number_list = list(map(int, user_input.strip().split()))

search_element = int(input("Enter the number to search: "))

index = binary_search(number_list, search_element, 0, len(number_list) - 1)

if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")
