# Create a function called cut that receive 3 parameters 
# first is the number to cut
# second lower limit
# third upper limit
# you have to return the lower limit if the number is less than the limit
# you have to return the upper limit if the number is greater than the limit
# return the number with no changes if the number do not go out the limits

def cut(number, lower, upper):
    if number < lower:
        return lower
    elif number > upper:
        return upper
    else:
        return number
    
print(cut(15, 0 ,10))
print(cut(15, 0 ,16))