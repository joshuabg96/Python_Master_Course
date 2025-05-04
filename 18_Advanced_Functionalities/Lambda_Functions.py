
# Traditional method
def double(num):
    result = num * 2
    return result

print(double(5))

# Simply function
def double_2(num): return num*2

print(double_2(5))


# Lambda function
Double_3 = lambda num: num*2

print(Double_3(4))


odd = lambda num: num%2 != 0
print(odd(5))


revert = lambda S: S[::-1]
print(revert("Hi"))


Sum = lambda x,y : x + y
print(Sum(5,6))