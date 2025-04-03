def restar(terminos1, terminos2):
    """
    Resta dos polinomios representados como diccionarios.
    :param terminos1: Diccionario del primer polinomio {exponente: coeficiente}.
    :param terminos2: Diccionario del segundo polinomio {exponente: coeficiente}.
    :return: Diccionario con el resultado de la resta.
    """
    resultado = terminos1.copy()
    for exp, coef in terminos2.items():
        resultado[exp] = resultado.get(exp, 0) - coef
        if resultado[exp] == 0:
            del resultado[exp]  # Elimina términos con coeficiente 0
    return resultado

def dividir(terminos1, terminos2):
    """
    Divide dos polinomios representados como diccionarios.
    :param terminos1: Diccionario del dividendo {exponente: coeficiente}.
    :param terminos2: Diccionario del divisor {exponente: coeficiente}.
    :return: Dos diccionarios, el cociente y el residuo.
    """
    dividendo = terminos1.copy()
    divisor = terminos2
    cociente = {}

    while dividendo and max(dividendo) >= max(divisor):
        exp_dividendo = max(dividendo)
        exp_divisor = max(divisor)
        coef_dividendo = dividendo[exp_dividendo]
        coef_divisor = divisor[exp_divisor]

        exp_cociente = exp_dividendo - exp_divisor
        coef_cociente = coef_dividendo / coef_divisor
        cociente[exp_cociente] = coef_cociente

        # Resta el término obtenido del dividendo
        for exp, coef in divisor.items():
            exp_actual = exp + exp_cociente
            dividendo[exp_actual] = dividendo.get(exp_actual, 0) - coef * coef_cociente
            if dividendo[exp_actual] == 0:
                del dividendo[exp_actual]

    return cociente, dividendo

def eliminar_termino(terminos, exponente):
    """
    Elimina un término específico de un polinomio.
    :param terminos: Diccionario del polinomio {exponente: coeficiente}.
    :param exponente: Exponente del término a eliminar.
    """
    if exponente in terminos:
        del terminos[exponente]

def existe_termino(terminos, exponente):
    """
    Verifica si un término específico existe en un polinomio.
    :param terminos: Diccionario del polinomio {exponente: coeficiente}.
    :param exponente: Exponente del término a verificar.
    :return: True si el término existe, False en caso contrario.
    """
    return exponente in terminos