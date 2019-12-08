from grafo import grafo
from Caminhos.caminho import caminho
from Caminhos.aplicacoes import app
from Caminhos.minimo import minimo
from utils import caminho_minino, caminho_min
import sys


class peso_negativo(Exception):
    pass


def test():
    print('Testando grafo de exemplo do livro Algoritmos 3rd (Cormen), página 480.')

    g = grafo(direcionado=True)

    g.inserir_vertice('a')
    g.inserir_vertice('b')
    g.inserir_vertice('c')
    g.inserir_vertice('d')
    g.inserir_vertice('e')

    g.inserir_aresta('a', 'b', 10)
    g.inserir_aresta('a', 'c', 5)
    g.inserir_aresta('b', 'd', 1)
    g.inserir_aresta('b', 'c', 2)
    g.inserir_aresta('c', 'b', 3)
    g.inserir_aresta('c', 'e', 2)
    g.inserir_aresta('c', 'd', 9)
    g.inserir_aresta('d', 'e', 4)
    g.inserir_aresta('e', 'a', 7)
    g.inserir_aresta('e', 'd', 6)

    d = dict()
    l = list()
    for i in g.get_vertices():
        for j in i.get_vertices_adjacentes():
            l.append(j.get_id())
        d.update({i.get_id(): l.copy()})
        l.clear()

    m = minimo()
    m.dijkstra(g, 'a')

    c = caminho()
    # c.BFS(g, 'd')
    v = g.get_vertice('a')
    w = g.get_vertice('e')
    q = list()
    q.append(w.get_id())
    distancia = w.get_distancia()

    # while w.get_anterior() != None:
    #    q.append(w.get_anterior().get_id())
    #    w = w.get_anterior()
    print('O menor caminho é:' + str(caminho_min(w)) + 'com custo: ' + str(distancia))

    # for v in g.get_vertices():
    #    w = [v.get_id()]
    ##   caminho_minino(v, w)
    # print('O menor caminho é: %s com custo %d.' % (w, v.get_distancia()))


if __name__ == "__main__":
    test()
