from Caminhos.caminho import caminho
from grafo import grafo


def ex1(g, i, f):
    c = caminho()

    l = c.BFS(g, i, f)
    if l:
        print("Lets que lets")
    else:
        print("Deu ruim")
    # print(l)


def teste(g):
    c = caminho()
    c.BFSS(g, '1')


def peg(g, i, f):
    if g.get_vertice(i).get_visitado() and g.get_vertice(f).get_visitado():
        print("Lets que lets")
    else:
        print("Deu ruim")


def testeuri2959():
    fist_l = input()
    fist_l = fist_l.split()
    n_aresta = int(fist_l[1])
    n_vertice = int(fist_l[0])
    n_perguntas = int(fist_l[2])
    g = grafo()
    for i in range(0, n_vertice):
        g.inserir_vertice(str(i + 1))

    for i in range(0, n_aresta):
        arestas = input()
        arestas = arestas.split()
        de = arestas[0]
        para = arestas[1]
        g.inserir_aresta(de, para, 1)
    teste(g)
    for i in range(0, n_perguntas):
        perguntas = input()
        perguntas = perguntas.split()
        initial = perguntas[0]
        final = perguntas[1]
        peg(g, initial, final)
        # ex1(g, initial, final)


testeuri2959()
