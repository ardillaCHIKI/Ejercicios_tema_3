# base_ej_2.py

# Ejemplo de uso
if __name__ == "__main__":
    matriz = [
        [2, 4, 3],
        [1, 5, 7],
        [6, 8, 9]
    ]
    
    print("Determinante (recursivo):", determinante_recursivo(matriz))
    print("Determinante (iterativo):", determinante_iterativo(matriz))