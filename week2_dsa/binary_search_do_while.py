array = list(map(int,input("Enter the elements: ").split()))
key = int(input("Enter the search element: "))
array.sort()
low = 0
high = len(array)-1
found = False
while low <= high:
    mid = (low+high)//2
    if key == array[mid]:
        print("Element found at index: ",mid)
        found = True
        break
    elif key<array[mid]:
        high = mid-1
    else:
        low = mid+1
if not found:
    print("Element not found")
