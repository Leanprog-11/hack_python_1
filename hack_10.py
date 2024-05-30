"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result = result.upper()
    nueva_palabra =[]
    for letra in result:
        if letra == "O":
            nueva_palabra.append("0") 
        elif letra == "I":
            nueva_palabra.append("1")
        elif letra == "A":
            nueva_palabra.append("@")
        else:
            nueva_palabra.append(letra)
    return nueva_palabra