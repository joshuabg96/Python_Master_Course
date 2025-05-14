import numpy as np

def Hi():
    print("Hi, Hi fro Hi.Hi()")

def Test():
    print("This is a test from new version")

def Generate_Array(numbers):
    return np.arange(numbers)

class HI:
    def __init__(self):
        print("Hi I'm saying Hi from HI.__init__()")

if __name__ == '__main__':
    print(Generate_Array(5))