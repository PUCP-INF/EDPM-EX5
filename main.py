from bosque import Bosque
from arbol import Arbol
from recorridos import preorden, postorden, niveles, frontera
from operaciones import num_hojas, grado_arbol, num_nodos, get_valores


def main():
    #
    # b1 = Bosque()        # el bosque vacío
    #
    # #                       _nodo
    # #   b1: ---------      --------
    # #       |   *---|----->| None |
    # #       ---------      --------
    #
    # assert(len(b1) == 0), "--> Error en __len__ de bosque"
    #
    # a1 = Arbol(10, b1)     # plantar el árbol
    # print(b1)
    #
    # #                       _nodo           _valor _primog _sig_herm
    # #   a1: ---------      ----------      --------------------------
    # #       |   *---|----->|   *----|----->|  10  |   *   |  None   |
    # #       ---------      ----------      -----------|--------------
    # #                                                 |
    # #                                                 v
    # #                                               _nodo (apuntado por b1)
    # #                                              --------
    # #                                              | None |
    # #                                              --------
    #
    # assert(a1.raiz() == 10), "--> Error en raíz() de árbol"
    # assert(len(a1.hijos()) == 0), "--> Error en hijos() de árbol"
    # assert(a1.num_hijos() == 0), "--> Error en núm_hijos() de árbol"
    # assert(a1.es_hoja_()), "--> Error en es_hoja_() de árbol"
    #
    # b1.add_arbol(a1)     # añadir el árbol al bosque
    #
    # #                       _nodo           _valor _primog _sig_herm
    # #   a1: ---------      ----------      --------------------------
    # #       |   *---|----->|   *----|----->|  10  |   *   |  None   |
    # #       ---------      ----------      -----------|--------------
    # #                                      ^          |
    # #                                      |          v
    # #                       _nodo          |        _nodo (ya no apuntado por b1)
    # #   b1: ---------      ----------      |       --------
    # #       |   *---|----->|   *----|------|       | None |
    # #       ---------      ----------              --------
    #
    # assert(len(b1) == 1), "--> Error en __len__ de bosque"
    #
    # a2 = Arbol(20, b1)     # plantar el árbol
    #
    # #                       _nodo           _valor _primog _sig_herm
    # #   a2: ---------      ----------      --------------------------
    # #       |   *---|----->|   *----|----->|  20  |   *   |  None   |
    # #       ---------      ----------      -----------|--------------
    # #                                                 |
    # #                                                 v
    # #                                               _nodo (apuntado por b1)
    # #                                              --------
    # #                                              |  *---|-----> _valor (10)
    # #                                              --------
    #
    # assert(a2.raiz() == 20), "--> Error en raíz() de árbol"
    # assert(len(a1.hijos()) == 1), "--> Error en hijos() de árbol"
    # assert(a1.num_hijos() == 1), "--> Error en núm_hijos() de árbol"
    # assert(not a1.es_hoja_()), "--> Error en es_hoja_() de árbol"
    #
    # b3 = Bosque()         # el bosque vacío
    # a3 = Arbol(30, b3)     # plantar el árbol
    # b3.add_arbol(a3)
    #
    # #                       _nodo           _valor _primog _sig_herm
    # #   a3: ---------      ----------      --------------------------
    # #       |   *---|----->|   *----|----->|  30  |   *   |  None   |
    # #       ---------      ----------      -----------|--------------
    # #                                                 |
    # #                                                 v
    # #                                               _nodo (apuntado por b3)
    # #                                              --------
    # #                                              | None |
    # #                                              --------
    #
    # b4 = Bosque()         # el bosque vacío
    # a4 = Arbol(40, b4)     # plantar el árbol
    #
    # b5 = Bosque()         # el bosque vacío
    # b5.add_arbol(a3)       # añadir el árbol al bosque
    # assert(len(b5) == 1), "--> Error en __len__ de bosque"
    #
    # b5.add_arbol(a4)       # añadir el árbol al bosque
    # assert(len(b5) == 2), "--> Error en __len__ de bosque"
    #
    # a5 = Arbol(50, b5)     # plantar el árbol
    # assert(a5.raiz() == 50), "--> Error en raíz() de árbol"
    # assert(len(a5.hijos()) == 2), "--> Error en hijos() de árbol"
    # assert(a5.num_hijos() == 2), "--> Error en núm_hijos() de árbol"
    # assert(not a5.es_hoja_()), "--> Error en es_hoja_() de árbol"
    #
    # # try:
    # #     print(b5[0])
    # # except AssertionError:
    # #     pass
    #
    # assert(b5[1].raiz() == 40), "--> Error en añ_árbol() de bosque"
    # assert(b5[2].raiz() == 30), "--> Error en añ_árbol() de bosque"
    #
    # print('All tests are ok')
    b_a = Bosque()
    a_a = Arbol('A', b_a)
    #
    b_b = Bosque()
    a_b = Arbol('B', b_b)
    b_c = Bosque()
    a_c = Arbol('C', b_c)
    b_d = Bosque()
    a_d = Arbol('D', b_d)

    b_a.add_arbol(a_b)
    b_a.add_arbol(a_c)
    b_a.add_arbol(a_d)

    b_e = Bosque()
    a_e = Arbol('E', b_e)

    b_f = Bosque()
    a_f = Arbol('F', b_f)

    b_b.add_arbol(a_e)
    b_b.add_arbol(a_f)

    get_valores(preorden(a_a))
    get_valores(postorden(a_a))
    get_valores(niveles(a_a))
    get_valores(frontera(a_a))
    # print([node.valor for node in preorden(a_a)])
    # print([node.valor for node in postorden(a_a)])
    # print(b_a[3].nodo.primog[2].raiz())
    # return
    #
    # b_J = Bosque()
    # a_J = Arbol('J', b_J)
    # b_K = Bosque()
    # a_K = Arbol('K', b_K)
    # b_L = Bosque()
    # a_L = Arbol('L', b_L)
    #
    # b_f.add_arbol(a_J)
    # b_f.add_arbol(a_K)
    # b_f.add_arbol(a_L)
    #
    # b_G = Bosque()
    # a_G = Arbol('G', b_G)
    # b_H = Bosque()
    # a_H = Arbol('H', b_H)
    # b_I = Bosque()
    # a_I = Arbol('I', b_I)
    #
    # b_d.add_arbol(a_G)
    # b_d.add_arbol(a_H)
    # b_d.add_arbol(a_I)
    #
    # print("Recorrido preorden: ", end=' ')
    # print(preorden(a_a))
    # print("Recorrido postorden: ", end='')
    # print(postorden(a_a))
    # print(frontera(a_a))
    # print()


if __name__ == "__main__":
    main()
