import math

from Caminhos.AGM import AGM
from grafo import grafo
from utils import computeGCD


def ex(g, moeda):
    a = AGM()
    total = a.KruskalMST(g)
    print(total * moeda)


def testeuri2725():
    g = grafo()
    total = int(input())
    l = list()

    for i in range(0, total):
        eegde, moeda = map(int, (input().split(" ")))
        for x in range(0, eegde):
            i, j = (map(int, input().split(" ")))
            l.append((i, j))

        for i in range(0, len(l)):
            for j in range(0, len(l)):
                if i != j:
                    peso = 1#? computeGCD(l[i][0], l[j][0])+computeGCD(l[i][1], l[j][1])
                    g.inserir_aresta(i, j, peso)
        ex(g, moeda)


testeuri2725()

""""5 6
0 0
10 0
6 24
0 48
10 48"""