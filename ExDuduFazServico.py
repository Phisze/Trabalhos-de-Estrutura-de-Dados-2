from Caminhos.aplicacoes import app
from grafo import grafo
import time
import timeit

def ex(g):
    a = app()
    if a.is_Cyclic(g):
        print('SIM')
    else:
        print('NÃO')

def testuri1610():
    l = int(input())
    fist_l = input()
    for j in range(0, l):
        n_aresta = int(fist_l[2])
        n_vertice = int(fist_l[0])
        g = grafo(True)
        for i in range(0, n_vertice):
            g.inserir_vertice(str(i + 1))

        for i in range(0, n_aresta):
            arestas = input()
            de = arestas[0]
            para = arestas[2]
            g.inserir_aresta(de, para, 1)

        ex(g)
        fist_l = input()


    """"
    g = grafo(True)

    g.inserir_vertice('1')
    g.inserir_vertice('2')

    g.inserir_aresta('1', '2', 1)

    ex(g)

    q = grafo(True)

    q.inserir_vertice('1')
    q.inserir_vertice('2')

    q.inserir_aresta('1', '2', 1)
    q.inserir_aresta('2', '1', 1)
    ex(q)

    w = grafo(True)

    w.inserir_vertice('1')
    w.inserir_vertice('2')
    w.inserir_vertice('3')
    w.inserir_vertice('4')

    w.inserir_aresta('2', '3', 1)
    w.inserir_aresta('3', '4', 1)
    w.inserir_aresta('4', '2', 1)
    w.inserir_aresta('1', '3', 1)
    ex(w)
"""
testuri1610()
