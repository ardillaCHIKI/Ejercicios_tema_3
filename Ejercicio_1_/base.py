def hanoi(n, origen, destino, auxiliar):
    """
    Resuelve el problema de las Torres de Hanoi.

    :param n: Número de piedras a mover.
    :param origen: Nombre de la columna origen.
    :param destino: Nombre de la columna destino.
    :param auxiliar: Nombre de la columna auxiliar.
    """
    if n == 1:
        mover_piedra(origen, destino)
        return
    hanoi(n - 1, origen, auxiliar, destino)
    mover_piedra(origen, destino)
    hanoi(n - 1, auxiliar, destino, origen)

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
    hanoi(num_piedras, "Columna A", "Columna C", "Columna B")

# Número de piedras preciosas
num_piedras = 74

# Resolver el problema
resolver_hanoi(num_piedras)