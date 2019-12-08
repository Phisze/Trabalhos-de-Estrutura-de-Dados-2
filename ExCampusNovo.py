from Caminhos.AGM import AGM
from grafo import grafo


def ex1(g, conjunto_t):
    a = AGM()
    conjunto_v, t = a.KruskalMSTCampus(g)
    if conjunto_t == conjunto_v:
        print(t)
    else:
        print("impossivel")


def testeuri2550():
    fist_l = input().split(" ")
    conjuto_t = set()
    while True:
        try:
            n_aresta = int(fist_l[1])
            n_vertice = int(fist_l[0])
            g = grafo()
            for i in range(0, n_vertice):
                g.inserir_vertice(i)
                conjuto_t.add(i)

            for i in range(0, n_aresta):
                arestas = input().split(" ")
                de = arestas[0]
                para = arestas[1]
                peso = arestas[2]
                g.inserir_aresta(int(de)-1, int(para)-1, int(peso))

            ex1(g, conjuto_t)
            fist_l = input().split(" ")

        except EOFError:
            break


testeuri2550()
