class vertice:

    def __init__(self, id):
        self._capital = False
        self._id = id
        self._vertices_adjacentes = {}
        self._distancia = 0
        self.f = 0
        self._visitado = False
        self._anterior = None
        self._pre = -1
        self._low = 0
        self._initial = False
        self._final = False
        self._ouro_t = 0

    def __init__(self, id, initial=False, final=False, capital=False):
        self._id = id
        self._capital = capital
        self._vertices_adjacentes = {}
        self._distancia = 0
        self.f = 0
        self._visitado = False
        self._anterior = None
        self._pre = -1
        self._low = 0
        self._initial = False
        self._final = False
        self._ouro_t = 0

    def set_ouro(self, ouro):
        self._ouro_t = ouro

    def get_ouro(self):
        return self._ouro_t

    def get_final(self):
        return self._final

    def get_id(self):
        return self._id

    def is_capital(self):
        return self._capital

    def get_pre(self):
        return self._pre

    def set_pre(self, pre):
        self._pre = pre

    def get_low(self):
        return self._low

    def set_low(self, low):
        self._low = low

    def inserir_vertice_adjacente(self, para=None, peso=0):
        self._vertices_adjacentes[para] = peso

    def get_vertices_adjacentes(self):
        return self._vertices_adjacentes.keys()

    def get_distancia(self):
        return self._distancia

    def set_distancia(self, distancia):
        self._distancia = distancia

    def get_f(self):
        return self._f

    def set_f(self, f):
        self._f = f

    def set_visitado(self):
        self._visitado = True

    def unset_visitado(self):
        self._visitado = False

    def get_visitado(self):
        return self._visitado

    def set_peso(self, para, peso):
        self._vertices_adjacentes[para] = peso

    def get_peso(self, para):
        return self._vertices_adjacentes[para]

    def set_anterior(self, anterior):
        self._anterior = anterior

    def get_anterior(self):
        return self._anterior

    def __str__(self):
        return str(self._id)
