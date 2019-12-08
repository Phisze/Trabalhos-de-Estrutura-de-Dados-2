from Caminhos.caminho import caminho
from grafo import grafo


def ex1(g, s, f, p):
    c = caminho()
    t = c.BFS_Proibido(g, s, f, p)
    print(t)


def testuri2528():
    fist_l = input().split(" ")
    while True:
        l = list()
        try:
            n_aresta = int(fist_l[1])
            n_vertice = int(fist_l[0])
            g = grafo()
            for i in range(0, n_vertice):
                g.inserir_vertice(str(i + 1))

            for i in range(0, n_aresta):
                arestas = input().split(" ")
                de = arestas[0]
                para = arestas[1]
                l.append((de, para))

                #g.inserir_aresta(de, para, 1)

            cidade = input().split(" ")
            start = cidade[0]
            fim = cidade[1]
            proibida = cidade[2]
            for i in l:
                if proibida not in i:
                    g.inserir_aresta(i[0], i[1], 1)
            ex1(g, start, fim, proibida)
            fist_l = input().split(" ")

        except EOFError:
            break


testuri2528()
