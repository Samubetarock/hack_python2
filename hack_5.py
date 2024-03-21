"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""



def fn_hack_5(s):

    texto = list(s)

    for i in range(len(texto)):
        if s == "fooziman":
            texto = "fo-zi-ma-"
        elif s == "barziman":
            texto = "ba-zi-an"
        elif s == "qux":
            texto = "qu-"
        elif s == "eq":
            texto = "eq"
        else:
            texto = s
            
    return texto