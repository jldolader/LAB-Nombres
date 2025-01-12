from nombres import *

def test_leer_frecuencias_nombres(ruta_fichero):
    return leer_frecuencias_nombres(ruta_fichero)

def test_filtrar_por_genero(lfn: list[FrecuenciaNombre], genero: str) -> list[FrecuenciaNombre]:
    print(filtrar_por_genero(lfn, genero))

def test_calcular_nombres(lfn: list[FrecuenciaNombre], genero: str|None = None) -> set[str]:
    print(calcular_nombres(lfn, genero))

def test_calcular_top_nombres_de_año(lfn: list[FrecuenciaNombre], anyo: int, lim: int = 10, genero: str|None = None) -> list[tuple[str, int]]:
    print(calcular_top_nombres_de_año(lfn, anyo, lim, genero))

if __name__ == '__main__':
    lfn = test_leer_frecuencias_nombres('data/frecuencias_nombres.csv')
    test_filtrar_por_genero(lfn, 'Hombre')
    #test_calcular_nombres(frn, 'Mujer')
    #test_calcular_top_nombres_de_año(frn, 2005, 4)