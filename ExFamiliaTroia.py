from Caminhos.caminho import caminho
from grafo import grafo


def ex1(g):
    c = caminho()
    l = c.allBrigdges(g)
    print(l)


def testeuri2440():
    fist_l = input()
    fist_l = fist_l.split()
    n_aresta = int(fist_l[1])
    n_vertice = int(fist_l[0])
    g = grafo(True)
    for i in range(0, n_vertice):
        g.inserir_vertice(str(i + 1))
    for i in range(0, n_aresta):
        arestas = input()
        arestas = arestas.split()
        de = arestas[0]
        para = arestas[1]
        g.inserir_aresta(de, para, 1)

    ex1(g)


""""g = grafo(True)

g.inserir_vertice('1')
g.inserir_vertice('2')
g.inserir_vertice('3')
g.inserir_vertice('4')

g.inserir_aresta('1', '2', 1)
g.inserir_aresta('2', '3', 1)
g.inserir_aresta('3', '4', 1)
g.inserir_aresta('4', '1', 1)

ex1(g)

q = grafo(True)

q.inserir_vertice('1')
q.inserir_vertice('2')
q.inserir_vertice('3')
q.inserir_vertice('4')
q.inserir_vertice('5')
q.inserir_vertice('6')
q.inserir_vertice('7')
q.inserir_vertice('8')

q.inserir_aresta('1', '2', 1)
q.inserir_aresta('2', '3', 1)
q.inserir_aresta('3', '6', 1)
q.inserir_aresta('6', '5', 1)
q.inserir_aresta('5', '4', 1)
q.inserir_aresta('4', '3', 1)
q.inserir_aresta('6', '7', 1)
q.inserir_aresta('7', '8', 1)
q.inserir_aresta('8', '1', 1)
q.inserir_aresta('1', '5', 1)

ex1(q)

w = grafo(True)

w.inserir_vertice('1')
w.inserir_vertice('2')
w.inserir_vertice('3')
w.inserir_vertice('4')
w.inserir_vertice('5')
w.inserir_vertice('6')
w.inserir_vertice('7')
w.inserir_vertice('8')

w.inserir_aresta('1', '2', 1)
w.inserir_aresta('2', '3', 1)
w.inserir_aresta('3', '6', 1)
w.inserir_aresta('4', '3', 1)
w.inserir_aresta('6', '5', 1)
w.inserir_aresta('7', '8', 1)
w.inserir_aresta('1', '4', 1)
w.inserir_aresta('6', '2', 1)

8 10
1 2
2 3
3 6
6 5
5 4
4 3
6 7
7 8
8 1
1 5


ex1(w)"""

testeuri2440()
