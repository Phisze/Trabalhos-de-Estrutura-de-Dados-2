import math

from Caminhos.AGM import AGM
from grafo import grafo
from utils import computeGCD


def ex(g, j):
    a = AGM()
    t = a.KruskalMST(g)#KruskalMSTDistancia(g, j)
    print(t)


def testeuri2885():
    g = grafo()
    t = grafo()
    l = list()

    eegde, capitais = map(int, (input().split(" ")))
    for i in range(0, eegde):
        if i < capitais:
            g.inserir_vertice(i, False, False, True)
        else:
            g.inserir_vertice(i, False, False, False)

    for x in range(0, eegde):
        i, j = (map(int, input().split(" ")))
        l.append((i, j))

    for i in range(0, len(l)):
        for j in range(0, len(l)):
            if i != j:
                peso = (l[i][0] - l[j][0]) ** 2 + (l[i][1] - l[j][1]) ** 2
                peso = math.sqrt(peso)
                g.inserir_aresta(i, j, peso)
    ex(g, t)


testeuri2885()
