# Traditional method
L = []
for letter in 'casa':
    L.append(letter)

print(L)

# List comprehension Method
L = [letter for letter in 'casa']
print(L)


# Traditional method
L = []
for number in range(0,11):
    L.append(number**2)
print(L)

# List comprehension Method
L= [number**2 for number in range(0,11)]
print(L)


# Traditional method
L = []
for number in range(0,11):
    if number % 2 == 0:
        L.append(number)
print(L)

# List comprehension Method
L = [ number for number in range(0,11) if number % 2 == 0]
print(L)



# Traditional method
L = []
for number in range(0,11):
    L.append(number**2)

even = []
for number in L:
    if number % 2 == 0:
        even.append(number)
print(even)


# List comprehension Method
even = [number for number in [number ** 2 for number in range(0,11)] if number % 2 == 0]
print(even)