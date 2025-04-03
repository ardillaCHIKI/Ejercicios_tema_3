import sys
import os

# Agregar el directorio raíz al PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Metodos import determinante_recursivo, determinante_iterativo

# Ejemplo de uso
def ejercicio2():
    matriz = [
        [2, 4, 3],
        [1, 5, 7],
        [6, 8, 9]
    ]
    print("Determinante (recursivo):", determinante_recursivo(matriz))
    print()
    print("Determinante (iterativo):", determinante_iterativo(matriz))
