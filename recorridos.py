from bosque import Bosque
from arbol import Arbol


def preorden_bosque(b: Bosque) -> list:
    if b.nodo is None:
        return []
    lst = []
    node = b.nodo
    while node is not None:
        lst += preorden_bosque(node.primog) + [node.valor]
        node = node.sig_herm
    return lst


def postorden_bosque(b: Bosque) -> list:
    if b.nodo is None:
        return []
    lst = []
    node = b.nodo
    while node is not None:
        lst += [node.valor] + postorden_bosque(node.primog)
        node = node.sig_herm
    return lst


def niveles_bosque(b: Bosque) -> list:
    if b.nodo is None:
        return []
    lst = []
    node = b.nodo
    b3 = Bosque()
    while node is not None:
        lst += [node.valor]
        b3 = unir(b3, node.primog)
        node = node.sig_herm
    lst += niveles_bosque(b3)
    return lst


def frontera_bosque(b: Bosque) -> list:
    if b.nodo is None:
        return []
    lst = []
    node = b.nodo
    while node is not None:
        if not frontera_bosque(node.primog):
            lst += [node.valor]
        else:
            lst += frontera_bosque(node.primog)
        node = node.sig_herm
    return lst


def unir(b1: Bosque, b2: Bosque) -> Bosque:
    if b1.nodo is None:
        return b2
    if b2.nodo is None:
        return b1
    b3 = Bosque()
    node = b1.nodo
    while node is not None:
        b3.add_arbol(Arbol(node.valor, node.primog))
        node = node.sig_herm
    node = b2.nodo
    while node is not None:
        b3.add_arbol(Arbol(node.valor, node.primog))
        node = node.sig_herm
    return b3


def preorden(a: Arbol) -> list:
    return preorden_bosque(a.nodo.primog) + [a.nodo.valor]


def postorden(a: Arbol) -> list:
    return [a.nodo.valor] + postorden_bosque(a.nodo.primog)


def niveles(a: Arbol) -> list:
    return niveles_bosque(a.nodo.primog) + [a.nodo.valor]


def frontera(a: Arbol) -> list:
    if a.nodo.primog is None:
        return [a.nodo.valor]
    return frontera_bosque(a.nodo.primog)
