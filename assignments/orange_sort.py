number_of_oranges = int(input("Enter the number of oranges: "))
diameters = list(map(int, input("Enter the diameters: ").split()))
k = 0
pivot = diameters[-1]
for i in range(number_of_oranges - 1):
    if diameters[i] <= pivot:
        diameters[i], diameters[k] = diameters[k], diameters[i]
        k += 1
diameters[k], diameters[-1] = diameters[-1], diameters[k]
print(diameters)
