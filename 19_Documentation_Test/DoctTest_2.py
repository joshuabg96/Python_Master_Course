import doctest

def double(L):
    """Double the value of the element on a list
    >>> L = [1,2,3,4,5]
    >>> double(L)
    [2, 4, 6, 8, 10]

    >>> L = []
    >>> for i in range(10):
    ...     L.append(i)
    >>> double(L)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    """
    return [n*2 for n in L]


print(doctest.testmod())