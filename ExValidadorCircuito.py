from Caminhos.aplicacoes import app
from Caminhos.caminho import caminho
from grafo import grafo


def ex(g, start, final):
    a = app()

    if a.is_Cyclic(g):
        for i in g.get_vertices():
            if i.get_final():
                if len(i.get_vertices_adjacentes()) == 0:
                    print("u.u")
        if len(start) == len(final):
            print("o.o")
        else:
            print("u.u")
    else:
        print("u.u")


def testeuri1956():
    fist_l = input()
    fist_l = fist_l.split()
    start = list()
    final = list()
    contador = 0
    cont = 0
    n_vertice_i = int(fist_l[0])
    n_vertice_m = int(fist_l[1])
    n_vertice_f = int(fist_l[2])
    g = grafo(True)
    for i in range(0, n_vertice_i):
        g.inserir_vertice(str(i + 1), initial=True)
        start.append(i + 1)
        contador = i + 1

    middleInitial = contador + 1
    for i in range(contador, contador + n_vertice_m):
        g.inserir_vertice(str(i + 1))
        contador = i + 1
    middleFinal = contador + 1

    for i in range(contador, contador + n_vertice_f):
        g.inserir_vertice(str(i + 1), final=True)
        final.append(i + 1)

    while cont != n_vertice_m:
        aresta = input()
        aresta = aresta.split()
        for i in range(0, int(aresta[0])):
            if middleInitial != middleFinal:
                g.inserir_aresta(aresta[i + 1], str(middleInitial))

        middleInitial += 1
        cont += 1

    arestaFinal = input()
    arestaFinal = arestaFinal.split()
    for i in arestaFinal:
        g.inserir_aresta(i, str(middleFinal))
        middleFinal += 1
    ex(g, start, final)


testeuri1956()
