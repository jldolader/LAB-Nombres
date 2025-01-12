from nombres import *

def test_leer_frecuencias_nombres(ruta_fichero):
    return leer_frecuencias_nombres(ruta_fichero)

def test_filtrar_por_genero(lfn, genero):
    print(filtrar_por_genero(lfn, genero))

def test_calcular_nombres(lfn, genero = None):
    print(calcular_nombres(lfn, genero))

def test_calcular_top_nombres_de_año(lfn, anyo, lim = 10, genero = None):
    print(calcular_top_nombres_de_año(lfn, anyo, lim, genero))

def test_calcular_nombres_ambos_generos(lfn):
    print(calcular_nombres_ambos_generos(lfn))

def test_calcular_nombres_compuestos(lfn, genero = None):
    print(calcular_nombres_compuestos(lfn, genero))
    
def test_calcular_frecuencia_media_nombre_años(lfn, nombre, anyo_ini, anyo_fin) -> float:
    print(calcular_frecuencia_media_nombre_años(lfn, nombre, anyo_ini, anyo_fin))
    
def test_calcular_nombre_mas_frecuente_año_genero(lfn, anyo, genero):
    print(calcular_nombre_mas_frecuente_año_genero(lfn, anyo, genero))
    
def test_calcular_año_mas_frecuencia_nombre(lfn, nombre):
    print(calcular_año_mas_frecuencia_nombre(lfn, nombre))
    
def test_calcular_nombres_mas_frecuentes(lfn, genero, decada, n = 5):
    print(calcular_nombres_mas_frecuentes(lfn, genero, decada, n))

def test_calcular_año_frecuencia_por_nombre(lfn, genero):
    print(calcular_año_frecuencia_por_nombre(lfn, genero))

def test_calcular_nombre_mas_frecuente_por_año(lfn, genero):
    print(calcular_nombre_mas_frecuente_por_año(lfn, genero))

def test_calcular_frecuencia_por_año(lfn, nombre):
    print(calcular_frecuencia_por_año(lfn, nombre))

def test_mostrar_evolucion_por_año(lfn, nombre):
    mostrar_evolucion_por_año(lfn, nombre)

def test_calcular_frecuencias_por_nombre(lfn):
    print(calcular_frecuencias_por_nombre(lfn))

def test_mostrar_frecuencias_nombres(lfn, limite=10):
    mostrar_frecuencias_nombres(lfn, limite)
    
if __name__ == '__main__':
    lfn = test_leer_frecuencias_nombres('data/frecuencias_nombres.csv')
    #test_filtrar_por_genero(lfn, 'Hombre')
    #test_calcular_nombres(lfn, 'Mujer')
    #test_calcular_top_nombres_de_año(lfn, 2005)
    #test_calcular_nombres_ambos_generos(lfn)
    #test_calcular_nombres_compuestos(lfn, 'Hombre')
    #test_calcular_frecuencia_media_nombre_años(lfn, 'RAFAEL', 2002, 2006)
    #test_calcular_nombre_mas_frecuente_año_genero(lfn, 2005, 'Hombre')
    #test_calcular_año_mas_frecuencia_nombre(lfn, 'JULIA')
    #test_calcular_nombres_mas_frecuentes(lfn, 'Hombre', 2010)
    #test_calcular_año_frecuencia_por_nombre(lfn, 'Hombre')
    #test_calcular_nombre_mas_frecuente_por_año(lfn, 'Hombre')
    #test_calcular_frecuencia_por_año(lfn, 'RAFAEL')
    #test_mostrar_evolucion_por_año(lfn, 'JULIA')
    #test_calcular_frecuencias_por_nombre(lfn)
    test_mostrar_frecuencias_nombres(lfn, 8)