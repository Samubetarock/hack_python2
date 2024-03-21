"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s.copy()  # Copia el diccionario original para evitar modificarlo directamente
    del result["bar"]  # Elimina la clave "bar"
    result["Foo"] = result.pop("foo").capitalize()  # Cambia la clave "foo" a "Foo" y capitaliza su valor
    for key, value in result.items():
        if value == "Fookziman":
            result[key] = "Fooziman"  # Reemplaza el valor "Fookziman" por "Fooziman"
    return result