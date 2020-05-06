from typing import List

from arbol import Arbol, _NodoArbol
from bosque import Bosque


def altura(a: Arbol) -> int:
    return 1 + altura_bosque(a.nodo.primog)


def num_nodos(a: Arbol) -> int:
    return 1 + num_nodos_bosque(a.nodo.primog)


def num_hojas(a: Arbol) -> int:
    return num_hojas_bosque(a.nodo.primog)


def grado(a: Arbol) -> int:
    return max(len(a.nodo.primog), grado_bosque(a.nodo.primog))


def num_hojas_bosque(b: Bosque) -> int:
    num = 0
    node = b.nodo
    while node is not None:
        if len(node.primog) == 0:
            num += 1
        else:
            num += num_hojas_bosque(node.primog)
        node = node.sig_herm
    return num


def grado_bosque(b: Bosque) -> int:
    max_grado = 0
    node = b.nodo
    while node is not None:
        if node.sig_herm is not None:
            if len(node.primog) > grado_bosque(node.sig_herm.primog):
                max_grado = len(b)
        node = node.sig_herm
    return max_grado


def num_nodos_bosque(b: Bosque) -> int:
    # se incluye el nodo raiz
    total = 0
    node = b.nodo
    while node is not None:
        if len(node.primog) != 0:
            total += num_nodos_bosque(node.primog)
        total += 1
        node = node.sig_herm
    return total


def altura_bosque(b: Bosque) -> int:
    total = 0
    node = b.nodo
    node_aux = b.nodo
    while node is not None:
        while len(node.primog) == 0:
            node = node.primog.nodo
            total += 1
    return total


def get_valores(lst: List[_NodoArbol]) -> None:
    new_lst = [node.valor for node in lst]
    new_lst.reverse()
    print(new_lst)
