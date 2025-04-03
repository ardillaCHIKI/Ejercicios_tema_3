from .requisitos import ordenar_naves_por_nombre_y_longitud,obtener_info_naves, obtener_naves_con_mas_pasajeros
from .requisitos import obtener_nave_con_mas_tripulacion, obtener_naves_por_prefijo, obtener_naves_con_minimo_pasajeros 
from .requisitos import obtener_nave_mas_pequena, obtener_nave_mas_grande


# Lista de naves espaciales
naves = [
    {"nombre": "Cometa Veloz", "longitud": 120, "tripulantes": 10, "pasajeros": 50},
    {"nombre": "Titán del Cosmos", "longitud": 200, "tripulantes": 15, "pasajeros": 100},
    {"nombre": "GX-1 Explorer", "longitud": 150, "tripulantes": 8, "pasajeros": 20},
    {"nombre": "Estrella Fugaz", "longitud": 180, "tripulantes": 12, "pasajeros": 80},
    {"nombre": "GX-2 Voyager", "longitud": 140, "tripulantes": 9, "pasajeros": 60},
    {"nombre": "Nebulosa Azul", "longitud": 160, "tripulantes": 11, "pasajeros": 40},
]


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

    print("|-------- Naves ordenadas por nombre ascendente y longitud descendente --------|")
    for nave in naves_ordenadas:
        print(nave)

    print()

    print("|-------- Información de 'Cometa Veloz' y 'Titán del Cosmos'--------|")
    for nave in info_cometa_titan:
        print(nave)

    print()

    print("|-------- Cinco naves con mayor cantidad de pasajeros --------|")
    for nave in naves_mas_pasajeros:
        print(nave)

    print()

    print("|-------- Nave que requiere mayor cantidad de tripulación --------|")
    print(nave_mas_tripulacion)

    print()

    print("|-------- Naves cuyo nombre comienza con 'GX' --------|")
    for nave in naves_gx:
        print(nave)

    print()

    print("|-------- Naves que pueden llevar seis o más pasajeros --------|")
    for nave in naves_seis_pasajeros:
        print(nave)

    print()

    print("|-------- Nave más pequeña --------|")
    print(nave_mas_pequena)

    print()

    print("|-------- Nave más grande --------|")
    print(nave_mas_grande)
