from bosque import Bosque
from arbol import Arbol
from recorridos import preorden, postorden, niveles, frontera
from operaciones import get_valores, grado, altura, num_nodos, num_hojas


def ej_prof():

    b1 = Bosque()        # el bosque vacío

    #                       _nodo
    #   b1: ---------      --------
    #       |   *---|----->| None |
    #       ---------      --------

    assert(len(b1) == 0), "--> Error en __len__ de bosque"

    a1 = Arbol(10, b1)     # plantar el árbol
    print(b1)

    #                       _nodo           _valor _primog _sig_herm
    #   a1: ---------      ----------      --------------------------
    #       |   *---|----->|   *----|----->|  10  |   *   |  None   |
    #       ---------      ----------      -----------|--------------
    #                                                 |
    #                                                 v
    #                                               _nodo (apuntado por b1)
    #                                              --------
    #                                              | None |
    #                                              --------

    assert(a1.raiz() == 10), "--> Error en raíz() de árbol"
    assert(len(a1.hijos()) == 0), "--> Error en hijos() de árbol"
    assert(a1.num_hijos() == 0), "--> Error en núm_hijos() de árbol"
    assert(a1.es_hoja_()), "--> Error en es_hoja_() de árbol"

    b1.add_arbol(a1)     # añadir el árbol al bosque

    #                       _nodo           _valor _primog _sig_herm
    #   a1: ---------      ----------      --------------------------
    #       |   *---|----->|   *----|----->|  10  |   *   |  None   |
    #       ---------      ----------      -----------|--------------
    #                                      ^          |
    #                                      |          v
    #                       _nodo          |        _nodo (ya no apuntado por b1)
    #   b1: ---------      ----------      |       --------
    #       |   *---|----->|   *----|------|       | None |
    #       ---------      ----------              --------

    assert(len(b1) == 1), "--> Error en __len__ de bosque"

    a2 = Arbol(20, b1)     # plantar el árbol

    #                       _nodo           _valor _primog _sig_herm
    #   a2: ---------      ----------      --------------------------
    #       |   *---|----->|   *----|----->|  20  |   *   |  None   |
    #       ---------      ----------      -----------|--------------
    #                                                 |
    #                                                 v
    #                                               _nodo (apuntado por b1)
    #                                              --------
    #                                              |  *---|-----> _valor (10)
    #                                              --------

    assert(a2.raiz() == 20), "--> Error en raíz() de árbol"
    assert(len(a1.hijos()) == 1), "--> Error en hijos() de árbol"
    assert(a1.num_hijos() == 1), "--> Error en núm_hijos() de árbol"
    assert(not a1.es_hoja_()), "--> Error en es_hoja_() de árbol"

    b3 = Bosque()         # el bosque vacío
    a3 = Arbol(30, b3)     # plantar el árbol
    b3.add_arbol(a3)

    #                       _nodo           _valor _primog _sig_herm
    #   a3: ---------      ----------      --------------------------
    #       |   *---|----->|   *----|----->|  30  |   *   |  None   |
    #       ---------      ----------      -----------|--------------
    #                                                 |
    #                                                 v
    #                                               _nodo (apuntado por b3)
    #                                              --------
    #                                              | None |
    #                                              --------

    b4 = Bosque()         # el bosque vacío
    a4 = Arbol(40, b4)     # plantar el árbol

    b5 = Bosque()         # el bosque vacío
    b5.add_arbol(a3)       # añadir el árbol al bosque
    assert(len(b5) == 1), "--> Error en __len__ de bosque"

    b5.add_arbol(a4)       # añadir el árbol al bosque
    assert(len(b5) == 2), "--> Error en __len__ de bosque"

    a5 = Arbol(50, b5)     # plantar el árbol
    assert(a5.raiz() == 50), "--> Error en raíz() de árbol"
    assert(len(a5.hijos()) == 2), "--> Error en hijos() de árbol"
    assert(a5.num_hijos() == 2), "--> Error en núm_hijos() de árbol"
    assert(not a5.es_hoja_()), "--> Error en es_hoja_() de árbol"

    # try:
    #     print(b5[0])
    # except AssertionError:
    #     pass

    assert(b5[1].raiz() == 40), "--> Error en añ_árbol() de bosque"
    assert(b5[2].raiz() == 30), "--> Error en añ_árbol() de bosque"

    print('All tests are ok')


def main():
    # Primero se crea el bosque
    b_a = Bosque()
    # Luego el arbol que contendra al bosque
    a_a = Arbol('A', b_a)

    b_b = Bosque()
    a_b = Arbol('B', b_b)
    b_c = Bosque()
    a_c = Arbol('C', b_c)
    b_d = Bosque()
    a_d = Arbol('D', b_d)

    b_a.add_arbol(a_b)
    b_a.add_arbol(a_c)
    b_a.add_arbol(a_d)
    assert a_c.es_hoja_(), 'C no es un bosque vacio'
    assert len(b_a) == 3, '--> Error al agregar los arboles B,C,D al bosque'

    b_e = Bosque()
    a_e = Arbol('E', b_e)

    b_f = Bosque()
    a_f = Arbol('F', b_f)

    b_b.add_arbol(a_e)
    b_b.add_arbol(a_f)
    assert a_e.es_hoja_(), 'E no es un bosque vacio'
    assert len(b_b) == 2, '--> Error al agregar los arboles E,F al bosque'

    b_j = Bosque()
    a_j = Arbol('J', b_j)
    b_k = Bosque()
    a_k = Arbol('K', b_k)
    b_l = Bosque()
    a_l = Arbol('L', b_l)

    b_f.add_arbol(a_j)
    b_f.add_arbol(a_k)
    b_f.add_arbol(a_l)
    assert len(b_f) == 3, '--> Error al agregar los arboles J,K,L al bosque'

    b_g = Bosque()
    a_g = Arbol('G', b_g)
    b_h = Bosque()
    a_h = Arbol('H', b_h)
    b_i = Bosque()
    a_i = Arbol('I', b_i)

    b_d.add_arbol(a_g)
    b_d.add_arbol(a_h)
    b_d.add_arbol(a_i)
    assert a_h.es_hoja_(), 'C no es un bosque vacio'
    assert len(b_d) == 3, '--> Error al agregar los arboles J,K,L al bosque'

    b_m = Bosque()
    a_m = Arbol('M', b_m)

    b_g.add_arbol(a_m)
    assert len(b_g) == 1, '--> Error al agregar el arbol G al bosque'

    b_p = Bosque()
    a_p = Arbol('P', b_p)
    b_q = Bosque()
    a_q = Arbol('Q', b_q)

    b_m.add_arbol(a_p)
    b_m.add_arbol(a_q)
    assert len(b_m) == 2, '--> Error al agregar los arboles P,Q al bosque'

    b_n = Bosque()
    a_n = Arbol('N', b_n)
    b_o = Bosque()
    a_o = Arbol('O', b_o)

    b_i.add_arbol(a_n)
    b_i.add_arbol(a_o)
    assert len(b_i) == 2, '--> Error al agregar los arboles N,O al bosque'

    print("Numero de nodos: %d" % num_nodos(a_a))
    print("Numero de hojas :%d" % num_hojas(a_a))
    print("Maximo grado: %d" % grado(a_a))
    print("Altura del arbol: %d" % altura(a_a))
    print('Recorrido preorden: ', end='')
    get_valores(preorden(a_a))
    print('Recorrido postorden: ', end='')
    get_valores(postorden(a_a))
    print('Recorrido niveles: ', end='')
    get_valores(niveles(a_a))
    print('Recorrido frontera: ', end='')
    get_valores(frontera(a_a))


if __name__ == "__main__":
    main()
