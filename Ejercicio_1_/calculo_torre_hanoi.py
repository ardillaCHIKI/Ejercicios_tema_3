def torre_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print("Mover disco 1 desde", origen, "hasta", destino)
        return 1
    else:
        combinaciones = 0
        combinaciones += torre_hanoi(n-1, origen, auxiliar, destino)
        print("Mover disco", n, "desde", origen, "hasta", destino)
        combinaciones += 1
        combinaciones += torre_hanoi(n-1, auxiliar, destino, origen)
        return combinaciones