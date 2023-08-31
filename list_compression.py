'''
@author: Google Jr
@program: list compression
'''

# list compression
# list compression is a way to create a list using a single line of code

# example 1
numbers = [i ** 2 for i in range(0, 11)]
print(numbers) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# example 2
names = ["Andile", "Mzie", "Ayanda", "Zola", "Olwethu", "Nondyebo"]
first_letters = [name[0] for name in names]
print(first_letters) # ['A', 'M', 'A', 'Z', 'O', 'N']

# example 3
numbers = [i * 2 for i in range(0, 11) if i % 2 == 0]
print(numbers) # [0, 4, 8, 12, 16, 20]

# example 4
numbers = [i * 2 if i % 2 == 0 else i * 3 for i in range(0, 11)]
print(numbers) # [0, 3, 4, 9, 8, 15, 12, 21, 16, 27, 20]

# example 5
numbers = [i * 2 if i % 2 == 0 else i * 3 for i in range(0, 11) if i % 3 == 0]
print(numbers) # [0, 9, 12, 27]

# example 6
numbers = [i * 2 if i % 2 == 0 else i * 3 for i in range(0, 11) if i % 3 == 0 and i % 2 == 0]
print(numbers) # [0, 12]

# example 7: More complex list compression
numbers = [i for i in range(1, 101) if i % 12 == 0]
print(numbers) # [12, 24, 36, 48, 60, 72, 84, 96]
