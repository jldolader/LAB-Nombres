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
            ) for d in reader]
        
def filtrar_por_genero(lfn: list[FrecuenciaNombre], genero: str) -> list[FrecuenciaNombre]:
    return [f for f in lfn if f.genero == genero]

def calcular_nombres(lfn: list[FrecuenciaNombre], genero: str|None = None) -> set[str]:
    return set(f.nombre for f in lfn if genero is None or f.genero == genero)

def calcular_top_nombres_de_año(lfn: list[FrecuenciaNombre], anyo: int, lim: int = 10, genero: str|None = None) -> list[tuple[str, int]]:
    return sorted((f.nombre, f.frecuencia) for f in lfn if f.año == anyo and (genero is None or f.genero == genero))[:lim]

def calcular_nombres_ambos_generos(lfn: list[FrecuenciaNombre]) -> set[str]:
    return {f.nombre for f in lfn if f.genero == 'Hombre'} & {f.nombre for f in lfn if f.genero == 'Mujer'}

def calcular_nombres_compuestos(lfn: list[FrecuenciaNombre], genero: str|None = None) -> set[str]:
    return set(f.nombre for f in lfn if ' ' in f.nombre and (genero is None or f.genero == genero))

def calcular_frecuencia_media_nombre_años(lfn: list[FrecuenciaNombre], nombre: str, anyo_ini: int, anyo_fin: int) -> float:
    frecuencia = [f.frecuencia for f in lfn if f.nombre.lower() == nombre.lower() and anyo_ini <= f.año <= anyo_fin]
    return sum(frecuencia) / len(frecuencia) if frecuencia else 0.0

def calcular_nombre_mas_frecuente_año_genero(lfn: list[FrecuenciaNombre], anyo: int, genero: str) -> str:
    lista = [f for f in lfn if f.año == anyo and f.genero.lower() == genero.lower()]
    return max(lista, key = lambda f: f.frecuencia).nombre if lista else ''

def calcular_año_mas_frecuencia_nombre(lfn: list[FrecuenciaNombre], nombre: str) -> int:
    lista = [f for f in lfn if f.nombre.lower() == nombre.lower()]
    return max(lista, key = lambda f: f.frecuencia).año if lista else 0