from __future__ import annotations
from arbol import Arbol, _NodoArbol


class Bosque:
    # Crea un bosque vacío
    def __init__(self):
        self.nodo: _NodoArbol = None

    # Añadir un árbol al bosque
    def add_arbol(self, a: Arbol):
        a.nodo.sig_herm = self.nodo
        self.nodo = a.nodo

    # Calcula la longitud de un bosque
    def __len__(self):
        c = self.nodo
        n = 0
        while c is not None:
            n += 1
            c = c.sig_herm
        return n

    # Consulta el i-ésimo árbol en el bosque
    def __getitem__(self, indice) -> Arbol:
        assert indice != 0, "Índice no válido"
        h = self.nodo
        assert h is not None, "Índice no válido"
        j = 1
        while h and j != indice:
            j += 1
            h = h.sig_herm
        assert h is not None, "Índice no válido"
        return h.arbol()
