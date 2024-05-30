"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = []
    lista = [1,2,3]
    i = 0
    while i < len(lista):
        result.append(lista[i])
        result.append('@')
        i += 1
    return result