from calculo_torre_hanoi import torre_hanoi

def ejercicio1():
    n = 74
    total_combinaciones = torre_hanoi(n, 'A', 'C', 'B')
    print("Total de combinaciones:", total_combinaciones)
