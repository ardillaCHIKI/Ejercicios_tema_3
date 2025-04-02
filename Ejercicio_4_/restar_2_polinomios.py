def restar(self, otro):
        # Resta dos polinomios
    resultado = self.terminos.copy()
    for exp, coef in otro.terminos.items():
        resultado[exp] = resultado.get(exp, 0) - coef
        if resultado[exp] == 0:
            del resultado[exp]
    return Polinomio(resultado)