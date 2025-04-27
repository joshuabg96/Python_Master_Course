# Create a function called relation that based on two numbers do the following
# if the first is greater than second return 1
# if the first is less than second return -1
# if both are equal return 0
# check with 5 and 10, 10 and 5, 5 and 5

def relation(first, second):
    if first > second:
        return 1
    elif first < second:
        return -1
    else:
        return 0
    
print(relation(5,10))
print(relation(10,5))
print(relation(5,5))