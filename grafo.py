from vertice import vertice


class grafo:

    def __init__(self, direcionado=False):
        self._vertices = {}
        self.direcionado = direcionado
        self.carga_t = 0
        self.carga_a = 0
        self.distancia = 0

    def isDirecionado(self):
        return self.direcionado

    def inserir_vertice(self, id, initial=False, final=True, capital=True):
        v = vertice(id, initial, final, capital)
        self._vertices[id] = v
        return v

    def inserir_aresta(self, de, para, peso=0):
        if de not in self._vertices:
            self.inserir_vertice(de)
        if para not in self._vertices:
            self.inserir_vertice(para)
        self._vertices[de].inserir_vertice_adjacente(self._vertices[para], peso)
        if not self.direcionado:
            self._vertices[para].inserir_vertice_adjacente(self._vertices[de], peso)

    def get_vertices(self):
        return [v for k, v in self._vertices.items()]

    def get_aresta(self, id, id1):
        if id in self._vertices:
            t = self._vertices[id]
            n = list(t.get_vertices_adjacentes())
            for i in n:
                if id1 == i.get_id():
                    return True
                else:
                    return False
        else:
            return False

    def get_vertice(self, id):
        if id in self._vertices:
            return self._vertices[id]
        else:
            return None

    def get_arestas(self):
        arestas = set()
        for id, v in self._vertices.items():
            for a in v._vertices_adjacentes:
                arestas.add((v, a))
        return arestas

    def __iter__(self):
        return iter(self._vertices.values())
