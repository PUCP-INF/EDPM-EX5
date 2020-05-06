from typing import List

from arbol import _NodoArbol
from bosque import Bosque


def num_hojas(b: Bosque) -> int:
    num = 0
    node = b.nodo
    while node is not None:
        if len(node.primog) == 0:
            num += 1
        else:
            num += num_hojas(node.primog)
        node = node.sig_herm
    return num


def grado_bosque(b: Bosque) -> int:
    max_grado = 0
    node = b.nodo
    while node is not None:
        if len(b) != 0:
            size = len(b)
            max_grado = max(max_grado, size)
        grado_bosque(node.primog)
        node = node.sig_herm
    return max_grado


def num_nodos(b: Bosque) -> int:
    # se incluye el nodo raiz
    total = 1
    node = b.nodo
    while node is not None:
        if len(node.primog) != 0:
            total += num_nodos(node.primog) - 1
        total += 1
        node = node.sig_herm
    return total


def altura(b: Bosque) -> int:
    if b.nodo is None:
        return 0
    total = 0

    return total


def get_valores(lst: List[_NodoArbol]) -> None:
    new_lst = [node.valor for node in lst]
    new_lst.reverse()
    print(new_lst)
