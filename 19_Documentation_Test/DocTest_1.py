import doctest


def sum(a,b):
    """The function sum(a,b) receive two parameters a and b return the sum of both
    
    >>> sum(5,10)
    15
    """
    return a+b


def palindrom(word):
    """This function receive a word if the word is a palindrome it returns True, otherwise return False
    
    >>> palindrom("radar")
    True

    >>> palindrom("somos")
    True

    >>> palindrom("Hola")
    False

    >>> palindrom("Ana")
    True
    """
    if word.lower() == word[::-1].lower():
        return True
    else:
        return False



print(doctest.testmod())