from Caminhos.AGM import AGM
from Caminhos.caminho import caminho
from grafo import grafo


def ex(g, j):
    a = AGM()
    j = a.KruskalMST(g, j)
    return j


def ex1(g, i, f):
    c = caminho()
    maior = c.BFS_Distancia(g, i, f)
    if maior != None:
        print(maior)
    else:
        print(0)


def testeuri2933():
    vertx, eegde = map(int, (input().split(" ")))
    g = grafo()
    j = grafo()
    for x in range(0, eegde):
        qq, xx, yy = map(int, input().split(" "))
        g.inserir_aresta(qq, xx, yy)

    ex(g, j)

    perg = int(input())
    for i in range(0, perg):
        inicio, fim = map(int, input().split(" "))
        ex1(j, inicio, fim)


testeuri2933()
