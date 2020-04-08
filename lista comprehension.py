# list comprehension

x = [1, 2, 3, 4, 5]
y = [1**2 for i in x]
z = [i for i in x if i%2==1]

print(z)

