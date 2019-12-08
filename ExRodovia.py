from Caminhos.aplicacoes import app
from grafo import grafo


def ex(g):
    a = app()
    t = a.componetesConexos(g)

    if t:
        print('S')
    else:
        print('N')


def testeuri2429():
    fist_l = input()
    n_vertice = int(fist_l)
    g = grafo(True)
    for i in range(0, n_vertice):
        g.inserir_vertice(str(i + 1))

    for i in range(0, n_vertice):
        arestas = input()
        arestas = arestas.split()
        de = arestas[0]
        para = arestas[1]
        g.inserir_aresta(de, para, 1)

    ex(g)


testeuri2429()
