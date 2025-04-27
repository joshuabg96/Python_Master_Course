# Create a function called split that takes a list of int numbers and return two sorted list
# first with even numbers and the second with odd numbers

def split(list):
    even = []
    odd = []
    list.sort()
    for number in list:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return even, odd

numbers = [-12, 84, 13, 20, -33, 101, 9]
print(split(numbers))
print(split([6,5,2,1,7]))