from utils import initialize_single_source, extract_min, relax


class minimo:

    def __init__(self):
        super().__init__()

    def dijkstra(self, g, s):
        initialize_single_source(g, s)
        S = []
        Q = [v for v in g.get_vertices()]
        while len(Q):
            u = extract_min(Q)
            u.set_visitado()
            S.append(u)
            for v in u.get_vertices_adjacentes():
                if v.get_visitado():
                    continue
                relax(u, v)

    def bellman_ford(self, g, s):
        initialize_single_source(g, s)
        for u in g.get_vertices():
            for u, v in g.get_arestas():
                if v.get_visitado():
                    continue
                relax(u, v)

        for u, v in g.get_arestas():
            if v.get_distancia() > u.get_distancia() + u.get_peso(v):
                return False

        return True
