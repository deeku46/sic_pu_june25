n, x, y = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
if numbers[y] > numbers[y - 1]:
    print(numbers[y] - numbers[y - 1] - 1)
else:
    print(0)
