from Caminhos.AGM import AGM
from grafo import grafo


def ex(g, total):
    a = AGM()
    t = a.KruskalMST(g)
    print(total - t)


def testeuri1152():
    vertx, eegde = map(int, (input().split(" ")))
    total = 0
    while vertx != 0 and eegde != 0:
        g = grafo()
        for x in range(0, vertx):
            g.inserir_vertice(x)
        for x in range(0, eegde):
            qq, xx, yy = map(int, input().split(" "))
            g.inserir_aresta(qq, xx, yy)
            total += yy

        ex(g, total)
        vertx, eegde = map(int, (input().split(" ")))


testeuri1152()
