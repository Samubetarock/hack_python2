"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):

    # Sustituyo
    sustituciones = {
        'a': '@',
        'e': '3',
        'i': '¡',
        'o': '0',
        'u': 'v',
        'm': 'm',
        'z': 'z',
        'r': 'r'
    }
    
    resultado = ""
    
    # Iterar sobre cada carácter en el texto de entrada
    for caracter in s:
        # Aplicar sustitución si el carácter está en el diccionario de sustituciones
        if caracter in sustituciones:
            resultado += sustituciones[caracter]
        else:
            # Si no hay sustitución, agregar el carácter en mayúsculas
            resultado += caracter.upper()
    
    return resultado