# Criar as paredes como vertices
# Os sinalizadores são vertices
# Se a distaancia euclidiana dele for menor ou igual ao raio de acesso ligar como arestas
# Verificar conectividade da parede de A chega na parede B
import math

from Caminhos.caminho import caminho
from grafo import grafo


def ex(g, i, f, f2):
    c = caminho()
    t = c.BFS2(g, i, f, f2)
    if t:
        print('N')
    else:
        print('S')


def testeuri2962():
    g = grafo()
    j = grafo()
    i, j, k = (map(int, input().split(" ")))
    # eegde = int(input())
    l = list()
    parede1 = list()
    parede2 = list()
    p1 = g.inserir_vertice(1)
    p2 = g.inserir_vertice(2)
    p3 = g.inserir_vertice(3)
    p4 = g.inserir_vertice(4)
    q = 5
    parede1.append(('?', 0))
    parede1.append(('?', i))

    parede2.append((0, '?'))
    parede2.append((j, '?'))

    for x in range(0, k):
        i, j, k = (map(int, input().split(" ")))
        l.append((i, j, k, q))
        q += 1

    for i in l:
        peso = ((i[1] - parede1[0][1]) ** 2)
        peso = peso ** (1 / 2)
        if i[2] - peso >= 0:
            g.inserir_aresta(p1.get_id(), i[3], peso)

        peso = ((i[1] - parede1[1][1]) ** 2)
        peso = peso ** (1 / 2)
        if i[2] - peso >= 0:
            g.inserir_aresta(p2.get_id(), i[3], peso)

        peso = ((i[0] - parede2[0][0]) ** 2)
        peso = peso ** (1 / 2)
        if i[2] - peso >= 0:
            g.inserir_aresta(p3.get_id(), i[3], peso)

        peso = ((i[0] - parede2[1][0]) ** 2)
        peso = peso ** (1 / 2)
        if i[2] - peso >= 0:
            g.inserir_aresta(p4.get_id(), i[3], peso)

        for j in l:
            peso = ((i[0] - j[0]) ** 2) + ((i[1] - j[1]) ** 2)
            peso = peso ** (1 / 2)
            if i != j:
                if i[2] + j[2] >= peso:
                    g.inserir_aresta(i[3], j[3], peso)

        # for j in range(0, len(l)):
        #    if i != j:
        #        peso = ((l[i][0] - l[j][0]) ** 2) + ((l[i][1] - l[j][1]) ** 2)
        #        peso = math.sqrt(peso)
        #       g.inserir_aresta(i, j, peso)
    ex(g, p1.get_id(), p2.get_id(), p3.get_id())
    # eegde = int(input())


testeuri2962()
