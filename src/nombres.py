from collections import namedtuple
import csv

from matplotlib import pyplot as plt

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
    lista = [f for f in filtrar_por_genero(lfn, genero) if f.año == anyo]
    return max(lista, key = lambda f: f.frecuencia).nombre if lista else ''

def calcular_año_mas_frecuencia_nombre(lfn: list[FrecuenciaNombre], nombre: str) -> int:
    lista = [f for f in lfn if f.nombre.lower() == nombre.lower()]
    return max(lista, key = lambda f: f.frecuencia).año if lista else 0

def calcular_nombres_mas_frecuentes(lfn: list[FrecuenciaNombre], genero: str, decada: int, n: int = 5) -> list[str]:
    lista = [f for f in lfn if decada <= f.año <= decada + 10 and f.genero.lower() == genero.lower()]
    return sorted(lista, key = lambda f: f.frecuencia, reverse = True)[:n]

def calcular_año_frecuencia_por_nombre(lfn: list[FrecuenciaNombre], genero: str) -> dict[str, list[tuple[int, int]]]:
    dic = {}
    
    for f in filtrar_por_genero(lfn, genero):
        if f.nombre not in dic:
            dic[f.nombre] = []
        dic[f.nombre].append((f.año, f.frecuencia))
    
    return dic

def calcular_nombre_mas_frecuente_por_año(lfn: list[FrecuenciaNombre], genero: str) -> list[tuple[int, str, int]]:
    resultado = []
    años = set(f.año for f in lfn)
    for año in años:
        nombre_mas_frecuente = calcular_nombre_mas_frecuente_año_genero(lfn, año, genero)
        if nombre_mas_frecuente:
            frecuencia = next(f.frecuencia for f in lfn if f.año == año and f.nombre == nombre_mas_frecuente and f.genero == genero)
            resultado.append((año, nombre_mas_frecuente, frecuencia))
    return resultado

def calcular_frecuencia_por_año(lfn: list[FrecuenciaNombre], nombre: str) -> list[tuple[int, int]]:
    return [(f.año, f.frecuencia) for f in lfn if f.nombre.lower() == nombre.lower()]

def mostrar_evolucion_por_año(lfn: list[FrecuenciaNombre], nombre: str):
    años, frecuencias = zip(*calcular_frecuencia_por_año(lfn, nombre))
    plt.plot(años, frecuencias)
    plt.title("Evolución del nombre '{}'".format(nombre))
    plt.show()

def calcular_frecuencias_por_nombre(lfn: list[FrecuenciaNombre]) -> dict[str, int]:
    frecuencias = {}
    for f in lfn:
        if f.nombre in frecuencias:
            frecuencias[f.nombre] += f.frecuencia
        else:
            frecuencias[f.nombre] = f.frecuencia
    return frecuencias

def mostrar_frecuencias_nombres(lfn: list[FrecuenciaNombre], limite: int = 10):
    dicc = calcular_frecuencias_por_nombre(lfn)
    nombres_frecuencias = sorted(dicc.items(), key=lambda item: item[1], reverse=True)[:limite]
    nombres, frecuencias = zip(*nombres_frecuencias)
    
    plt.bar(nombres, frecuencias)
    plt.xticks(rotation=80)
    plt.title("Frecuencia de los {} nombres más comunes".format(limite))
    plt.show()