N = list(map(int, input("Enter the elements of the array: ").split()))
for i in range(0, len(N)):
    sorted = True
    for j in range(1, len(N) - i - 1):
        if N[j] > N[j + 1]:
            N[j], N[j + 1] = N[j + 1], N[j]
            sorted = False
    if sorted:
        break

print("Sorted array is:", N)