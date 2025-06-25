n=int(input('Enter a positive integer: '))
if n>0:
    root = n**0.5
    if root*root==n:
        print("{} is a perfect square".format(n))
else:
    print('Invalid input')