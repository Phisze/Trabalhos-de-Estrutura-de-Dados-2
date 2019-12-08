import sys
from collections import deque

import numpy as np

from utils import initialize_single_source_all, predecessor, contador, initialize_single_source, setBusca, contadorF, \
    uri


class caminho():

    def __init__(self):
        super().__init__()

    def allBrigdges(self, g):
        initialize_single_source_all(g)
        l = list()
        w = list()
        for vertex in g.get_vertices():
            if not vertex.get_visitado():
                l.append(vertex.get_id())
                self.__brigdes(g, vertex, 0, 0, 0, w)

        q = list()
        for i in l:
            for j in w:
                if i == j[0]:
                    q.append(j)

        for i in q:
            w.remove(i)
        return len(l) + len(w)

    def __brigdes(self, g, vertex, time, cnt, bcnt, lista):
        time += 1
        cnt += 1
        vertex.set_pre(cnt)
        vertex.set_low(vertex.get_pre())
        vertex.set_distancia(time)
        vertex.set_visitado()

        for adjacentVertex in vertex.get_vertices_adjacentes():
            if not adjacentVertex.get_visitado():
                adjacentVertex.set_anterior(vertex)
                self.__brigdes(g, adjacentVertex, time, cnt, bcnt, lista)
                if vertex.get_low() > adjacentVertex.get_low():
                    vertex.set_low(adjacentVertex.get_low())
                if adjacentVertex.get_low() == adjacentVertex.get_pre():
                    bcnt += 1
                    lista.append([str(vertex.get_id()), str(adjacentVertex.get_id())])
            elif adjacentVertex != vertex.get_anterior() and vertex.get_low() > adjacentVertex.get_low():
                vertex.set_low(adjacentVertex.get_pre())
        time += 1
        vertex.set_f(time)

    def DFS(self, g):
        initialize_single_source_all(g)
        for vertex in g.get_vertices():
            if not vertex.get_visitado():
                v = self.__DFS_VISIT(g, vertex, 0)
        return v

    def DFS_VISIT(self, g, vertex, time, vertexif, final, inicial):
        time += 1
        vertex.set_distancia(time)
        vertex.set_visitado()
        for adjacentVertex in vertex.get_vertices_adjacentes():
            if adjacentVertex.get_id() == vertexif[1]:
                final = True

            if final and adjacentVertex.get_id() == vertexif[0]:
                inicial = True

            if inicial and final:
                return True

            if not adjacentVertex.get_visitado():
                adjacentVertex.set_anterior(vertex)
                return self.__DFS_VISIT1(g, adjacentVertex, time, final, inicial)

        time += 1
        vertex.set_f(time)

    def DFS_Bomba(self, g, vertexi, vertexf, time, tempo):
        time += 1

        vertexi.set_distancia(time)
        vertexi.set_visitado()
        if vertexi.get_id() == vertexf:
            return tempo
        if tempo == sys.getrecursionlimit() - 15:
            return '*'
        for adjacentVertex in vertexi.get_vertices_adjacentes():
            if tempo % 3 == 0:
                if vertexi.get_peso(adjacentVertex) == 1 or vertexi.get_peso(adjacentVertex) == 2:
                    # if not adjacentVertex.get_visitado():
                    adjacentVertex.set_anterior(vertexi)
                    tempo += 1
                    return self.DFS_Bomba(g, adjacentVertex, vertexf, time, tempo)
            else:
                if vertexi.get_peso(adjacentVertex) == 0 or vertexi.get_peso(adjacentVertex) == 2:
                    # if not adjacentVertex.get_visitado():
                    adjacentVertex.set_anterior(vertexi)
                    tempo += 1
                    return self.DFS_Bomba(g, adjacentVertex, vertexf, time, tempo)
        time += 1
        vertexi.set_f(time)

    def DFS_VISIT1(self, g, vertex, time):
        time += 1
        vertex.set_distancia(time)
        vertex.set_visitado()

        for adjacentVertex in vertex.get_vertices_adjacentes():
            if not adjacentVertex.get_visitado():
                adjacentVertex.set_anterior(vertex)
                self.DFS_VISIT1(g, adjacentVertex, time)

        time += 1
        vertex.set_f(time)

    def DFS_VISITDengue(self, g, vertex, time, distancia):
        time += 1
        vertex.set_distancia(time)
        vertex.set_visitado()

        for adjacentVertex in vertex.get_vertices_adjacentes():
            if not adjacentVertex.get_visitado():
                distancia += 2 * (vertex.get_peso(adjacentVertex))
                adjacentVertex.set_anterior(vertex)
                self.DFS_VISITDengue(g, adjacentVertex, time, distancia)

        time += 1
        vertex.set_f(time)
        return distancia

    def DFS_VISIT_Dinheros(self, g, vertex, time):
        time += 1
        vertex.set_distancia(time)
        vertex.set_visitado()

        for adjacentVertex in vertex.get_vertices_adjacentes():
            if not adjacentVertex.get_visitado():
                while adjacentVertex.get_ouro() != 0:
                    g.distancia += vertex.get_peso(adjacentVertex)
                    adjacentVertex.set_anterior(vertex)
                    self.DFS_VISIT_Dinheros(g, adjacentVertex, time)
                    g.distancia += vertex.get_peso(adjacentVertex)
                    if g.carga_a > 0:
                        vertex.set_ouro(vertex.get_ouro() + g.carga_a)
                        g.carga_a = 0

        d = vertex.get_ouro() - g.carga_t
        if vertex.get_ouro() >= g.carga_t:
            g.carga_a = g.carga_t
        else:
            g.carga_a = vertex.get_ouro()
        if d >= 0:
            vertex.set_ouro(d)
        else:
            vertex.set_ouro(0)
        time += 1
        vertex.set_f(time)

    def __DFS_VISIT(self, g, vertex, time):
        time += 1
        vertex.set_distancia(time)
        vertex.set_visitado()

        for adjacentVertex in vertex.get_vertices_adjacentes():
            if not adjacentVertex.get_visitado():
                adjacentVertex.set_anterior(vertex)
                self.__DFS_VISIT(g, adjacentVertex, time)

            if adjacentVertex.get_visitado():
                return True

        time += 1
        vertex.set_f(time)
        return False

    def BFSS(self, g, start):
        initialize_single_source(g, start)
        start = g.get_vertice(start)
        Q = list()
        Q.append(start)
        while len(Q):
            u = Q[0]
            u.set_visitado()
            Q.remove(u)
            for v in u.get_vertices_adjacentes():
                if not v.get_visitado():
                    setBusca(v, u)
                    Q.append(v)

    def BFS_Distancia(self, g, start, final):
        maior = sys.maxsize * -1
        initialize_single_source(g, start)
        start = g.get_vertice(start)
        l = list()
        Q = list()
        Q.append(start)
        # if len(start.get_vertices_adjacentes()) > 1:
        while len(Q):
            u = Q[0]
            u.set_visitado()
            Q.remove(u)
            for v in u.get_vertices_adjacentes():
                # uri(v, u, final, l)
                peso = u.get_peso(v)
                if peso > maior:
                    maior = peso
                if not v.get_visitado():
                    setBusca(v, u)
                    Q.append(v)
                    if v.get_id() == final:
                        return maior

    def BFS(self, g, start, final):
        initialize_single_source(g, start)
        start = g.get_vertice(start)
        l = list()
        Q = list()
        Q.append(start)
        # if len(start.get_vertices_adjacentes()) > 1:
        while len(Q):
            u = Q[0]
            u.set_visitado()
            Q.remove(u)
            for v in u.get_vertices_adjacentes():
                # uri(v, u, final, l)
                if not v.get_visitado():
                    setBusca(v, u)
                    Q.append(v)
                    if v.get_id() == final:
                        return True

        # else:
        #    l.append(-1)
        return False

    def BFS2(self, g, start, final, final2):
        initialize_single_source(g, start)
        start = g.get_vertice(start)
        l = list()
        Q = list()
        Q.append(start)
        # if len(start.get_vertices_adjacentes()) > 1:
        while len(Q):
            u = Q[0]
            u.set_visitado()
            Q.remove(u)
            for v in u.get_vertices_adjacentes():
                # uri(v, u, final, l)
                if not v.get_visitado():
                    setBusca(v, u)
                    Q.append(v)
                    if v.get_id() == final or v.get_id() == final2:
                        return True

        # else:
        #    l.append(-1)
        return False

    def BFS_Proibido(self, g, start, final, p):
        initialize_single_source(g, start)
        start = g.get_vertice(start)
        l = list()
        Q = list()
        Q.append(start)
        # if len(start.get_vertices_adjacentes()) > 1:
        while len(Q):
            u = Q[0]
            u.set_visitado()
            Q.remove(u)
            for v in u.get_vertices_adjacentes():
                # uri(v, u, final, l)
                if not v.get_visitado():
                    setBusca(v, u)
                    Q.append(v)
                    if v.get_id() == final:
                        return v.get_distancia()
