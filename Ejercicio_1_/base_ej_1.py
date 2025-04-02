def hanoi_iterativo(n, origen, destino, auxiliar):
    """
    Resuelve el problema de las Torres de Hanoi de forma iterativa.

    :param n: Número de piedras a mover.
    :param origen: Nombre de la columna origen.
    :param destino: Nombre de la columna destino.
    :param auxiliar: Nombre de la columna auxiliar.
    """
    # Crear una pila para simular la recursión
    pila = []
    pila.append((n, origen, destino, auxiliar))

    while pila:
        n, origen, destino, auxiliar = pila.pop()
        if n == 1:
            mover_piedra(origen, destino)
        else:
            # Simular las llamadas recursivas en orden inverso
            pila.append((n - 1, auxiliar, destino, origen))
            pila.append((1, origen, destino, auxiliar))
            pila.append((n - 1, origen, auxiliar, destino))

def mover_piedra(origen, destino):
    """
    Imprime el movimiento de una piedra de una columna a otra.

    :param origen: Nombre de la columna origen.
    :param destino: Nombre de la columna destino.
    """
    print(f"Mueve la piedra de {origen} a {destino}")

def resolver_hanoi(num_piedras):
    """
    Resuelve el problema de las Torres de Hanoi para un número dado de piedras.

    :param num_piedras: Número de piedras preciosas.
    """
    hanoi_iterativo(num_piedras, "Columna A", "Columna C", "Columna B")

# Número de piedras preciosas
num_piedras = 10  # Ajusta el número según sea necesario

# Resolver el problema
resolver_hanoi(num_piedras)