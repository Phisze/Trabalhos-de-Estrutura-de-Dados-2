from grafo import grafo
from utils import caminho_min
from Caminhos.minimo import minimo


# TERMINAR
def ex(g, i, f):
    m = minimo()
    m.dijkstra(g, i)
    v = g.get_vertice(f)
    t = caminho_min(v)
    distancia = v.get_distancia()
    if distancia - 120 <= 0:
        print('Will not be late. Travel time - ' + str(distancia) + ' - best way - ', end='')
        for i in t:
            if t[len(t) - 1] == i:
                print(str(i))
            else:
                print(str(i) + ' ', end='')
        #print()
    else:
        print('It will be ' + str(distancia - 120) + ' minutes late. Travel time - ' + str(distancia) + ' - best way - ',
            end='')
        for i in t:
            if t[len(t) - 1] == i:
                print(str(i))
            else:
                print(str(i) + ' ', end='')


def testuri2731():
    fist_l = input()
    while fist_l != '0 0':
        fist_l = fist_l.split()
        n_aresta = int(fist_l[1])
        n_vertice = int(fist_l[0])
        g = grafo()
        for i in range(0, n_vertice):
            g.inserir_vertice(str(i))

        for i in range(0, n_aresta):
            arestas = input()
            arestas = arestas.split()
            de = arestas[0]
            para = arestas[1]
            peso = int(arestas[2])
            g.inserir_aresta(de, para, peso)
        final = input()
        ex(g, '1', final)
        fist_l = input()


testuri2731()
