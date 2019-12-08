import sys
from collections import defaultdict

# Part of Cosmos by OpenGenus Foundation
from grafo import grafo
from utils import export_list


class AGM():

    def __init__(self) -> None:
        super().__init__()

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMSTDistancia(self, g, j):
        result = []
        total = 0
        i, e = 0, 0
        graph = export_list(g)
        graph = sorted(graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in g.get_vertices():
            parent.append(int(node.get_id()))
            rank.append(0)
        while e < len(g.get_vertices()) - 1:
            u, v, w = graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                j.inserir_aresta(u, v, w)
                t = j.get_vertice(u)
                total += w
                if t.is_capital():
                    for zzz in t.get_vertices_adjacentes():
                        if zzz.get_id() != v:
                            t.set_peso(zzz, sys.maxsize)

                t = j.get_vertice(v)
                if t.is_capital():
                    for zzz in t.get_vertices_adjacentes():
                        if zzz.get_id() != u:
                            zzz.set_peso(i, sys.maxsize)

                self.union(parent, rank, x, y)
        # print("Constructed MST :")
        # print("Vertex A    Vertex B  Weight")
        # for u, v, weight in result:
        #    print("    %d          %d        %d" % (u, v, weight))
        return t

    def KruskalMSTT(self, g, j):
        result = []
        i, e = 0, 0
        total = 0
        graph = export_list(g)
        graph = sorted(graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in g.get_vertices():
            parent.append(int(node.get_id()))
            rank.append(0)
        while e < len(g.get_vertices()) - 1:
            u, v, w = graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                if not j.get_aresta(u, v):
                    total += g.get_vertice(u).get_peso(g.get_vertice(v))
                j.inserir_aresta(u, v, w)
                self.union(parent, rank, x, y)
        # print("Constructed MST :")
        # print("Vertex A    Vertex B  Weight")
        # for u, v, weight in result:
        #    print("    %d          %d        %d" % (u, v, weight))
        return j, total

    def KruskalMST(self, g, j):
        result = []
        i, e = 0, 0
        graph = export_list(g)
        graph = sorted(graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in g.get_vertices():
            parent.append(int(node.get_id()))
            rank.append(0)
        while e < len(g.get_vertices()) - 1:
            u, v, w = graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                j.inserir_aresta(u, v, w)
                self.union(parent, rank, x, y)
        # print("Constructed MST :")
        # print("Vertex A    Vertex B  Weight")
        # for u, v, weight in result:
        #    print("    %d          %d        %d" % (u, v, weight))
        return j

    def KruskalMST(self, g):
        total = 0
        result = []
        i, e = 0, 0
        graph = export_list(g)
        graph = sorted(graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in g.get_vertices():
            parent.append(int(node.get_id()))
            rank.append(0)
        while e < len(g.get_vertices()) - 1:
            u, v, w = graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                total += w
                self.union(parent, rank, x, y)
        return total

    def KruskalMSTCampus(self, g):
        total = 0
        vertices_atingidos = set()
        result = []
        i, e = 0, 0
        graph = export_list(g)
        graph = sorted(graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in g.get_vertices():
            parent.append(int(node.get_id()))
            rank.append(0)
        while e < len(g.get_vertices()) - 1:
            if len(graph) - 1 != i:
                u, v, w = graph[i]
                i = i + 1
                x = self.find(parent, u)
                y = self.find(parent, v)
                if x != y:
                    e = e + 1
                    result.append([u, v, w])
                    total += w
                    vertices_atingidos.add(u)
                    vertices_atingidos.add(v)
                    self.union(parent, rank, x, y)
            else:
                break
        return vertices_atingidos, total
