"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    nueva_palabra= ""
    for letra in result:
        if letra == 'o':
            nueva_palabra = nueva_palabra +'0'
        elif letra == 'i':
            nueva_palabra = nueva_palabra + '1'
        elif letra == "a":
            nueva_palabra = nueva_palabra + '@'
        else:
            nueva_palabra = nueva_palabra + letra
    return nueva_palabra