import sys

from Caminhos.caminho import caminho
from grafo import grafo


def ex(g):
    c = caminho()
    c.DFS_VISIT_Dinheros(g, g.get_vertice(1), 0)
    print(g.distancia)


def testeuri2666():
    cidade, carga = map(int, (input().split(" ")))
    g = grafo()
    dinheiro = input().split(" ")
    n = 1
    for i in dinheiro:
        v = g.inserir_vertice(n)
        # g.inserir_aresta(n, n, 0)
        v.set_ouro(int(i))
        ouro_t = int(i)
        n += 1
    for x in range(0, cidade - 1):
        qq, xx, yy = map(int, input().split(" "))
        g.inserir_aresta(qq, xx, yy)
    g.carga_t = int(carga)
    ex(g)


testeuri2666()
