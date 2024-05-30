"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    lista = [1, 3, 5, 7, 9]
    result = lista[1:-1]
    return result  