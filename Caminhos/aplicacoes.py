from operator import attrgetter

from Caminhos.caminho import caminho
from grafo import grafo


class app():

    def __init__(self):
        self.c = caminho()
        super().__init__()

    def __grafoTransitivo(self, g):
        grafo_transitivo = grafo(True)
        for i in g.get_vertices():
            grafo_transitivo.inserir_vertice(str(i.get_id()))

        #Fazer tranistividade
        for i in g.get_vertices():
            for j in i.get_vertices_adjacentes():
                grafo_transitivo.inserir_aresta(j.get_id(), i.get_id(), i.get_peso(j))

        return grafo_transitivo

    def componetesConexos(self, g):
        if not self.is_Cyclic(g):
            return False
        c = caminho()
        c.DFS_VISIT1(g, g.get_vertice('1'), 0)
        for i in g.get_vertices():
            if not i.get_visitado():
                return False

        grafoT = self.__grafoTransitivo(g)

        c.DFS_VISIT1(grafoT, grafoT.get_vertice('1'), 0)
        for i in grafoT.get_vertices():
            if not i.get_visitado():
                return False

        return True

    def topologicalSort(self, g):
        c = caminho()
        if c.DFS(g):
            u = g.get_vertices()
            t = sorted(u, key=attrgetter('_f'), reverse=True)
            return t
        else:
            raise("Topological sort not possible. Graph is not acyclic.")
        return None

    def __topological_comparator(self, u, v):
        return u.get_f() - v.get_f()

    def is_Cyclic(self, g):
        if len(g.get_arestas()) > len(g.get_vertices()) - 1:
           return True
        else:
            return False
