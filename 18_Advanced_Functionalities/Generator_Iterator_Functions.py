

[number for number in [0,1,2,3,4,5] if number %2 == 0]

[number for number in range(0,6) if number%2 == 0]

def even(n):
    for number in range(n+1):
        if number % 2 == 0:
            yield number

print(even(10))             # Generator object

for number in even(10):
    print(number)


print([number for number in even(10)])

even = even(10)
print(next(even))           #0
print(next(even))           #2
print(next(even))           #4
print(next(even))           #6
print(next(even))           #8
print(next(even))           #10