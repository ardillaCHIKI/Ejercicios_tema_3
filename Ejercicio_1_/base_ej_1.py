import sys
import os

# Agregar el directorio raíz al PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from calculo_torre_hanoi import torre_hanoi

def ejercicio1():
    n = 5
    total_combinaciones = torre_hanoi(n, 'A', 'C', 'B')
    print("Total de combinaciones:", total_combinaciones)
