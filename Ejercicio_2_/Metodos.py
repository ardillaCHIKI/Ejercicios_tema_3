def determinante_recursivo(matriz):
    if len(matriz) == 1:
        return matriz[0][0]
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    determinante = 0
    for col in range(len(matriz)):
        
        submatriz = [fila[:col] + fila[col + 1:] for fila in matriz[1:]]
        
        determinante += ((-1) ** col) * matriz[0][col] * determinante_recursivo(submatriz)

    return determinante

def determinante_iterativo(matriz):
    if len(matriz) != 3 or len(matriz[0]) != 3:
        raise ValueError("Este método solo funciona para matrices 3x3.")
    
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    
    return (a * e * i + b * f * g + c * d * h) - (c * e * g + b * d * i + a * f * h)