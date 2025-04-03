import sys
import os

# Agregar el directorio raíz al PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from funciones import restar, dividir, eliminar_termino, existe_termino

class Polinomio:
    def __init__(self, terminos=None):
        # terminos es un diccionario donde la clave es el exponente y el valor es el coeficiente
        self.terminos = terminos if terminos else {}

    def __str__(self):
        # Representación legible del polinomio
        return " + ".join(f"{coef}x^{exp}" if exp != 0 else f"{coef}"
                          for exp, coef in sorted(self.terminos.items(), reverse=True))

    def restar(self, otro):
        # Usa la función restar para restar dos polinomios
        resultado = restar(self.terminos, otro.terminos)
        return Polinomio(resultado)

    def dividir(self, otro):
        # Usa la función dividir para dividir dos polinomios
        cociente, residuo = dividir(self.terminos, otro.terminos)
        return Polinomio(cociente), Polinomio(residuo)

    def eliminar_termino(self, exponente):
        # Usa la función eliminar_termino para eliminar un término
        eliminar_termino(self.terminos, exponente)

    def existe_termino(self, exponente):
        # Usa la función existe_termino para verificar si un término existe
        return existe_termino(self.terminos, exponente)

# Ejemplo de uso
def ejercicio4():
    p1 = Polinomio({3: 4, 2: 3, 0: 5})  # 4x^3 + 3x^2 + 5
    p2 = Polinomio({1: 2, 0: 1})        # 2x + 1

    print("Polinomio 1:", p1)
    print("Polinomio 2:", p2)

    # Restar
    resta = p1.restar(p2)
    print("Resta:", resta)

    # Dividir
    cociente, residuo = p1.dividir(p2)
    print("Cociente:", cociente)
    print("Residuo:", residuo)

    # Eliminar término
    p1.eliminar_termino(2)
    print("Polinomio 1 después de eliminar término x^2:", p1)

    # Verificar existencia de término
    existe = p1.existe_termino(3)
    print("¿Existe el término x^3 en Polinomio 1?", existe)