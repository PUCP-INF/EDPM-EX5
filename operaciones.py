from typing import List

from arbol import Arbol, _NodoArbol
from recorridos import preorden, postorden, niveles, frontera


def num_hojas(a: Arbol) -> int:
    num = 0
    nodes = preorden(a)
    for node in nodes:
        if len(node.primog) == 0:
            num += 1
    return num


def grado_arbol(a: Arbol) -> int:
    max_grado = 0
    nodes = preorden(a)
    for node in nodes:
        if len(node.primog) > max_grado:
            max_grado = len(node.primog)
    return max_grado


def num_nodos(a: Arbol) -> int:
    return len(preorden(a))


def get_valores(lst: List[_NodoArbol]) -> None:
    print([node.valor for node in lst])


def altura(a: Arbol) -> int:
    pass
