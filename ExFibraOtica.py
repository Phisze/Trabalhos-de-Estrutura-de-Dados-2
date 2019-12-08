from Caminhos.AGM import AGM
from grafo import grafo


def ex(g, j):
    a = AGM()
    grafo, t = a.KruskalMSTT(g, j)
    print(t)


def testeuri2941():
    g = grafo()
    q = grafo()
    cont = 1
    l = list()
    total_v = int(input())
    for i in range(0, total_v):
        g.inserir_vertice((i))
        q.inserir_vertice((i))
    for i in range(0, total_v):
        z = input().split(" ")
        for j in range(0, len(z)):
            if i < j:
                g.inserir_aresta((i), (j), int(z[j]))
            elif i > j:
                if z[j] == '1':
                    l.append((i, j))

    for i in l:
        de = i[1]
        para = i[0]
        vert = g.get_vertice(de)
        peso = vert.get_peso(g.get_vertice(para))
        q.inserir_aresta(de, para, peso)
    ex(g, q)


testeuri2941()
