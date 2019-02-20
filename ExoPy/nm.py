""" 4 operation
 de base """

def add(a,b):
    """addition"""
    return a + b


def sou(a,b):
    """soustraction"""
    return a - b


def mul(a,b):
    """multiplication"""
    return a * b



def div(a,b):
    """division"""
    if(b != 0):
        return a/b
    else:
        return "div impossible"

if (__name__=="__main__"):
    print(add(1,5))