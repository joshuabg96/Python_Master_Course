

numbers = [2,5,10,23,50,33]
def mult(number):
    if number % 5 == 0:
        return True
    
filter(mult, numbers)
print(list(filter(mult, numbers)))

f = filter(mult, numbers)
print(next(f))
print(next(f))
print(next(f))