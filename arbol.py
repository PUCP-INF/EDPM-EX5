from __future__ import annotations


class _NodoArbol:
    # El método privado para crear un nodo de árbol
    def __init__(self, valor, primog):
        self.valor = valor
        self.primog = primog
        self.sig_herm = None

    # El método privado para considerar el nodo como un árbol
    def arbol(self):
        return Arbol(self)


class Arbol:
    # Planta un árbol en el bosque
    def __init__(self, elem, bosque=None):
        if bosque is None:      # el nodo ya existe, su dirección está en elem
            self.nodo = elem
        else:
            self.nodo = _NodoArbol(elem, bosque)

    # Consulta la raíz de un árbol
    def raiz(self):
        return self.nodo.valor

    # Consulta la sucesión de hijos de un árbol (un bosque)
    def hijos(self):
        return self.nodo.primog

    # Calcula el número de hijos de un árbol
    def num_hijos(self):
        return len(self.nodo.primog)

    # Determina si un árbol es una hoja
    def es_hoja_(self):
        return self.num_hijos() == 0
