from grafo import grafo
from Caminhos.minimo import minimo


def ex1(g, j, i, f):
    m = minimo()
    m.dijkstra(g, str(i))
    m.dijkstra(j, str(i))
    distancia_g = g.get_vertice(f).get_distancia()
    distancia_j = j.get_vertice(f).get_distancia()
    if distancia_g > distancia_j:
        print(distancia_j)
    else:
        print(distancia_g)


def testeuri2731():
    fist_l = input()
    fist_l = fist_l.split()
    n_aresta = int(fist_l[1])
    n_vertice = int(fist_l[0])
    final = '1'
    initial = '1'
    g = grafo()
    j = grafo()
    for i in range(0, n_vertice):
        g.inserir_vertice(str(i + 1))
        j.inserir_vertice(str(i + 1))
        initial = i + 1
    for i in range(0, n_aresta):
        arestas = input()
        arestas = arestas.split()
        de = arestas[0]
        para = arestas[1]
        troca = int(arestas[2])
        peso = int(arestas[3])
        if troca == 0:
            g.inserir_aresta(de, para, peso)
        elif troca == 1:
            j.inserir_aresta(de, para, peso)

    ex1(g, j, initial, final)


testeuri2731()
