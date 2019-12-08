from Caminhos.aplicacoes import app
from Caminhos.caminho import caminho
from Caminhos.minimo import minimo
from grafo import grafo
from utils import caminho_minino

"""
            Grafo Fortemente Conexo
1 - Busca em profundiade do 1: DFS_VISIT1(grafo, '1', 0)
        Todos os vertices foram visitados
            Não return False
            Sim continue
2 - Calcular grafo transitivo
3 - Busca em profundidade com o grafo transitivo do 1:   DFS_VISIT1(grafoTransitivo, '1', 0)
        Todos os vertices foram visitados
            Não return False
            Sim return True
"""


def ex(g):
    a = app()
    t = a.componetesConexos(g)

    if t:
        print(1)
    else:
        print(0)


def testeuri1128():

    fist_l = input()
    while fist_l != '0 0':
        n_aresta = int(fist_l[2])
        n_vertice = int(fist_l[0])
        g = grafo(True)
        for i in range(0, n_vertice):
            g.inserir_vertice(str(i+1))

        for i in range(0, n_aresta):
            arestas = input()
            de = arestas[0]
            para = arestas[2]
            peso = int(arestas[4])
            if peso == 1:
                g.inserir_aresta(de, para, 1)
            elif peso == 2:
                g.inserir_aresta(de, para, 1)
                g.inserir_aresta(para, de, 1)

        ex(g)
        fist_l = input()

testeuri1128()
