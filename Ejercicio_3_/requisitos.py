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