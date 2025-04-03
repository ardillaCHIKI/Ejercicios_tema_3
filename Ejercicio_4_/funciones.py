class Polinomio:
    def __init__(self, terminos=None):
        # terminos es un diccionario donde la clave es el exponente y el valor es el coeficiente
        self.terminos = terminos if terminos else {}

    def __str__(self):
        # Representación legible del polinomio
        return " + ".join(f"{coef}x^{exp}" if exp != 0 else f"{coef}"
                          for exp, coef in sorted(self.terminos.items(), reverse=True))

def existe_termino(self, exponente):
        # Determina si un término específico existe en el polinomio
    return exponente in self.terminos

def dividir(self, otro):
        # Divide dos polinomios (división sintética)
    dividendo = self.terminos.copy()
    divisor = otro.terminos
    resultado = {}

    while dividendo and max(dividendo) >= max(divisor):
        exp_dividendo = max(dividendo)
        exp_divisor = max(divisor)
        coef_dividendo = dividendo[exp_dividendo]
        coef_divisor = divisor[exp_divisor]

        exp_resultado = exp_dividendo - exp_divisor
        coef_resultado = coef_dividendo / coef_divisor
        resultado[exp_resultado] = coef_resultado

            # Resta el término obtenido del dividendo
        for exp, coef in divisor.items():
            exp_actual = exp + exp_resultado
            dividendo[exp_actual] = dividendo.get(exp_actual, 0) - coef * coef_resultado
            if dividendo[exp_actual] == 0:
                del dividendo[exp_actual]

    return Polinomio(resultado), Polinomio(dividendo)

def eliminar_termino(self, exponente):
        # Elimina un término específico del polinomio
    if exponente in self.terminos:
        del self.terminos[exponente]

def restar(self, otro):
        # Resta dos polinomios
    resultado = self.terminos.copy()
    for exp, coef in otro.terminos.items():
        resultado[exp] = resultado.get(exp, 0) - coef
        if resultado[exp] == 0:
            del resultado[exp]
    return Polinomio(resultado)