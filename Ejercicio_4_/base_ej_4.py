from funciones import restar
from funciones import existe_termino
from funciones import dividir, eliminar_termino, restar
from funciones import Polinomio
# Ejemplo de uso
def ejercicio4():
    p1 = Polinomio({3: 4, 2: 3, 0: 5})  # 4x^3 + 3x^2 + 5
    p2 = Polinomio({1: 2, 0: 1})        # 2x + 1

    print("Polinomio 1:", p1)
    print("Polinomio 2:", p2)

    # Restar
    resta = restar(p1, p2)
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