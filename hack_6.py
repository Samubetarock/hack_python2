"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    resultado = s.copy()

    if not resultado:
        resultado = ["0"]
        
    else:
        for i in range(len(resultado)+1):
            if  i % 2 == 0:
                resultado[i-1:i+1] = "-"
            else:
                resultado[i-1:i+1] = [str(i)]
    return resultado
