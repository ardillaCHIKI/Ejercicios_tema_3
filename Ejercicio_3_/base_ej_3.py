# Lista de naves espaciales
naves = [
    {"nombre": "Cometa Veloz", "longitud": 120, "tripulantes": 10, "pasajeros": 50},
    {"nombre": "Titán del Cosmos", "longitud": 200, "tripulantes": 15, "pasajeros": 100},
    {"nombre": "GX-1 Explorer", "longitud": 150, "tripulantes": 8, "pasajeros": 20},
    {"nombre": "Estrella Fugaz", "longitud": 180, "tripulantes": 12, "pasajeros": 80},
    {"nombre": "GX-2 Voyager", "longitud": 140, "tripulantes": 9, "pasajeros": 60},
    {"nombre": "Nebulosa Azul", "longitud": 160, "tripulantes": 11, "pasajeros": 40},
]

def ordenar_naves_por_nombre_y_longitud(naves):
    return sorted(naves, key=lambda x: (x["nombre"], -x["longitud"]))

def obtener_info_naves(naves, nombres):
    return [nave for nave in naves if nave["nombre"] in nombres]

def obtener_naves_con_mas_pasajeros(naves, cantidad=5):
    return sorted(naves, key=lambda x: x["pasajeros"], reverse=True)[:cantidad]

def obtener_nave_con_mas_tripulacion(naves):
    return max(naves, key=lambda x: x["tripulantes"])

def obtener_naves_por_prefijo(naves, prefijo):
    return [nave for nave in naves if nave["nombre"].startswith(prefijo)]

def obtener_naves_con_minimo_pasajeros(naves, minimo):
    return [nave for nave in naves if nave["pasajeros"] >= minimo]

def obtener_nave_mas_pequena(naves):
    return min(naves, key=lambda x: x["longitud"])

def obtener_nave_mas_grande(naves):
    return max(naves, key=lambda x: x["longitud"])

# Resultados
def ejercicio3():
    naves_ordenadas = ordenar_naves_por_nombre_y_longitud(naves)
    info_cometa_titan = obtener_info_naves(naves, ["Cometa Veloz", "Titán del Cosmos"])
    naves_mas_pasajeros = obtener_naves_con_mas_pasajeros(naves)
    nave_mas_tripulacion = obtener_nave_con_mas_tripulacion(naves)
    naves_gx = obtener_naves_por_prefijo(naves, "GX")
    naves_seis_pasajeros = obtener_naves_con_minimo_pasajeros(naves, 6)
    nave_mas_pequena = obtener_nave_mas_pequena(naves)
    nave_mas_grande = obtener_nave_mas_grande(naves)

    print("Naves ordenadas por nombre ascendente y longitud descendente:")
    for nave in naves_ordenadas:
        print(nave)

    print("\nInformación de 'Cometa Veloz' y 'Titán del Cosmos':")
    for nave in info_cometa_titan:
        print(nave)

    print("\nCinco naves con mayor cantidad de pasajeros:")
    for nave in naves_mas_pasajeros:
        print(nave)

    print("\nNave que requiere mayor cantidad de tripulación:")
    print(nave_mas_tripulacion)

    print("\nNaves cuyo nombre comienza con 'GX':")
    for nave in naves_gx:
        print(nave)

    print("\nNaves que pueden llevar seis o más pasajeros:")
    for nave in naves_seis_pasajeros:
        print(nave)

    print("\nNave más pequeña:")
    print(nave_mas_pequena)

    print("\nNave más grande:")
    print(nave_mas_grande)
