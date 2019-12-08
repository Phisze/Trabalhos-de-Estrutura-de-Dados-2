from Caminhos.caminho import caminho
from grafo import grafo
from utils import caminho_minino
from Caminhos.minimo import minimo

""""
7 9
0 6
0 1 1
0 2 1
0 3 2
0 4 3
1 5 2
2 6 4
3 6 2
4 6 4
5 6 1
4 6
0 2
0 1 1
1 2 1
1 3 1
3 2 1
2 0 3
3 0 2
6 8
0 1
0 1 1
0 2 2
0 3 3
2 5 3
3 4 2
4 1 1
5 1 1
3 0 1
0 0
"""


def ex(g, i, f):
    if g.get_vertice(f):
        c = caminho()

        t = c.BFS(g, i, f)
        if len(t) > 1:
            t.sort()
            q = t[0]
            for i in t:
                if i > q:
                    print(i)
                    break
        else:
            print(-1)
    else:
        print(-1)


def testuri1391():
    fist_l = input()
    while fist_l != '0 0':
        second_l = input()
        n_aresta = int(fist_l[2])
        n_vertice = int(fist_l[0])
        inicio = second_l[0]
        fim = second_l[2]
        g = grafo(True)
        for i in range(0, n_vertice):
            g.inserir_vertice(str(i))

        for i in range(0, n_aresta):
            arestas = input()
            de = arestas[0]
            para = arestas[2]
            peso = int(arestas[4])
            g.inserir_aresta(de, para, peso)

        ex(g, inicio, fim)
        fist_l = input()


testuri1391()
