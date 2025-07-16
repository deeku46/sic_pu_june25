def fibonacci(term):
    if term == 1:
        return 1
    if term == 2:
        return 2
    return fibonacci(term - 1) + fibonacci(term - 2)


number_of_terms = int(input("Enter how many terms you want: "))

for i in range(1, number_of_terms + 1):
    print(fibonacci(i), end=' ')
