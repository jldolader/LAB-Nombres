from collections import namedtuple
import csv


FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')

def leer_frecuencias_nombres(ruta_fichero: str) -> list[FrecuenciaNombre]:
    with open(ruta_fichero, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)        
        return [FrecuenciaNombre(
                año = int(d[0]),
                nombre = str(d[1]),
                frecuencia = int(d[2]),
                genero = str(d[3])
            ) 
            for d in reader
        ]
        
def filtrar_por_genero(lfn: list[FrecuenciaNombre], genero: str) -> list[FrecuenciaNombre]:
    return [f for f in lfn if f.genero == genero]

def calcular_nombres(lfn: list[FrecuenciaNombre], genero: str|None = None) -> set[str]:
    pass

def calcular_top_nombres_de_año(lfn: list[FrecuenciaNombre], anyo: int, lim: int = 10, genero: str|None = None) -> list[tuple[str, int]]:
    pass

'''
def calcular_nombres_ambos_generos() -> :
    pass

def calcular_nombres_compuestos() -> :
    pass

def calcular_frecuencia_media_nombre_años() -> :
    pass

def calcular_nombre_mas_frecuente_año_genero() -> :
    pass

def calcular_año_mas_frecuencia_nombre() -> :
    pass

def calcular_nombres_mas_frecuentes() -> :
    pass

def calcular_año_frecuencia_por_nombre() -> :
    pass

def calcular_nombre_mas_frecuente_por_año() -> :
    pass

def calcular_frecuencia_por_año() -> :
    pass

def mostrar_evolucion_por_año() -> :
    pass
'''