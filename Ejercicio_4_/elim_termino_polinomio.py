def eliminar_termino(self, exponente):
        # Elimina un término específico del polinomio
    if exponente in self.terminos:
        del self.terminos[exponente]