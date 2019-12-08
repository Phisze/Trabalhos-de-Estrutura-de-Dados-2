import math

from Caminhos.AGM import AGM
from Caminhos.caminho import caminho
from grafo import grafo
from utils import computeGCD


def ex(g, j):
    a = AGM()
    grafo, t = a.KruskalMSTT(g, j)  # KruskalMSTDistancia(g, j)
    c = caminho()
    dist = c.DFS_VISITDengue(grafo, grafo.get_vertice(1), 0, 0)
    y = 0
    print(dist)


def testeuri2885():
    g = grafo()
    b = grafo()
    t = grafo()
    l = list()

    eegde = int(input())
    while eegde != 0:
        for i in range(0, eegde + 1):
            g.inserir_vertice(i)
            t.inserir_vertice(i)

        for x in range(0, eegde + 1):
            i, j = (map(int, input().split(" ")))
            l.append((i, j))

        for i in range(0, len(l)):
            for j in range(0, len(l)):
                if i != j:
                    peso = ((l[i][0] - l[j][0]) ** 2) + ((l[i][1] - l[j][1]) ** 2)
                    peso = math.sqrt(peso)
                    g.inserir_aresta(i, j, peso)
        ex(g, b)
        eegde = int(input())


testeuri2885()
