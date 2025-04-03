def restar(terminos1, terminos2):
    resultado = terminos1.copy()
    for exp, coef in terminos2.items():
        resultado[exp] = resultado.get(exp, 0) - coef
        if resultado[exp] == 0:
            del resultado[exp]  # Elimina términos con coeficiente 0
    return resultado

def dividir(terminos1, terminos2):
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
    if exponente in terminos:
        del terminos[exponente]

def existe_termino(terminos, exponente):
    return exponente in terminos