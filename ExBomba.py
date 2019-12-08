import sys

from Caminhos.caminho import caminho
from grafo import grafo


def ex(g, i, f):
    c = caminho()
    t = c.DFS_Bomba(g, g.get_vertice(i), f, 0, 0)
    print(t)


def testeuri2426():
    g = grafo(True)
    w = -1
    q = -1
    vertice, entrada, saida, eegde = map(int, (input().split(" ")))
    for i in range(0, eegde):
        x, y, p = map(int, (input().split(" ")))
        if x == q and y == w:
            g.inserir_aresta(x, y, 2)
        else:
            g.inserir_aresta(x, y, p)
        q = x
        w = y
    ex(g, entrada, saida)


testeuri2426()
