# base_ej_2.py

# Método recursivo para calcular el determinante de una matriz
def determinante_recursivo(matriz):
    if len(matriz) == 1:
        return matriz[0][0]
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    determinante = 0
    for i in range(len(matriz)):
        submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
        determinante += ((-1) ** i) * matriz[0][i] * determinante_recursivo(submatriz)
    return determinante

# Método iterativo para calcular el determinante de una matriz 3x3
def determinante_iterativo(matriz):
    if len(matriz) != 3 or len(matriz[0]) != 3:
        raise ValueError("Este método solo funciona para matrices 3x3.")
    
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    
    return (a * e * i + b * f * g + c * d * h) - (c * e * g + b * d * i + a * f * h)

# Ejemplo de uso
if __name__ == "__main__":
    matriz = [
        [2, 4, 3],
        [1, 5, 7],
        [6, 8, 9]
    ]
    
    print("Determinante (recursivo):", determinante_recursivo(matriz))
    print("Determinante (iterativo):", determinante_iterativo(matriz))