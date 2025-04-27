def M_Sum(a,b):
    try:
        return a + b
    except TypeError:
        print("You are giving a different value than numbers")
    else:
        return ""

def M_Sub(a,b):
    try:
        return a - b
    except TypeError:
        print("You are giving a different value than numbers")
    else:
        return ""

def M_Pro(a,b):
    try:
        return a * b
    except TypeError:
        print("You are giving a different value than numbers")
    else: 
        return ""

def M_Div(a,b):
    try:
        return a / b
    except TypeError:
        print("You are giving a different value than numbers")
    except ZeroDivisionError:
        print("You can not divide by zero")
    else:
        return ""