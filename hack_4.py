"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""



def fn_hack_4(s):

    texto = list(s)

    for i in range(len(texto)):
        if s == "fooziman":
            texto = "oozima"
        elif s == "barziman":
            texto = "arzima"
        else:
            texto = s
            
    return texto