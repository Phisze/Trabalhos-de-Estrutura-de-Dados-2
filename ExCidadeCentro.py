from grafo import grafo
from utils import caminho_minino
from Caminhos.minimo import minimo


def ex1(q):
    m = minimo()
    dist = list()
    for i in q.get_vertices():
        m.dijkstra(q, i.get_id())
        d = 0
        for v in q.get_vertices():
            w = [v.get_id()]
            caminho_minino(v, w)
            d += v.get_distancia()
        dist.append([d, i.get_id()])

    menor = [dist[0]]
    for i in range(1, len(dist)):
        if dist[i][0] == menor[0][0]:
            menor.append(dist[i])
        elif dist[i][0] < menor[0][0]:
            menor.clear()
            menor.append(dist[i])
    return menor


def testuri2676():
    fist_l = input()
    while fist_l != '0 0':
        n_aresta = int(fist_l[2])
        n_vertice = int(fist_l[0])
        g = grafo()
        for i in range(0, n_vertice):
            g.inserir_vertice(str(i + 1))

        for i in range(0, n_aresta):
            arestas = input()
            de = arestas[0]
            para = arestas[2]
            peso = int(arestas[4])
            g.inserir_aresta(de, para, peso)

        menor = ex1(g)
        for i in menor:
            print(str(i[1]) + " ", end="")
        print()
        fist_l = input()


testuri2676()
