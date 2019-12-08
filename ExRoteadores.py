from Caminhos.AGM import AGM
from grafo import grafo


def ex(g):
    a = AGM()
    t = a.KruskalMST(g)
    print(t)


def testeuri1774():
    vertx, eegde = map(int, (input().split(" ")))
    g = grafo()
    for x in range(0, vertx):
        g.inserir_vertice(x)
    for x in range(0, eegde):
        qq, xx, yy = map(int, input().split(" "))
        g.inserir_aresta(qq - 1, xx - 1, yy)

    ex(g)


testeuri1774()
