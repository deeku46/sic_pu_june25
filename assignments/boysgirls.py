t = int(input("Number of test cases: "))
for j in t:
    n=int(input("Number of boys and girls: "))
    boys_height=list(map(int(input("Enter boys height: ").split())))
    girls_height=list(map(int(input("Enter girls height: ").split())))

boys_height.sort()
girls_height.sort()
arrangement_of_boys_and_girls = []
for i in n:
    arrangement_of_boys_and_girls.append(girls_height[i])
    arrangement_of_boys_and_girls.append(boys_height[i])

print(arrangement_of_boys_and_girls)