import sys


def initialize_single_source_all(g):
    for v in g.get_vertices():
        v.set_distancia(sys.maxsize)
        v.set_f(sys.maxsize)
        v.set_anterior(None)
        v.unset_visitado()


def initialize_single_source(g, s1):
    for v in g.get_vertices():
        v.set_distancia(sys.maxsize)
        v.set_anterior(None)
        v.unset_visitado()
    for i in s1:
        g.get_vertice(s1).set_distancia(0)
        g.get_vertice(s1).set_anterior(None)


def initialize_single_source(g, s):
    for v in g.get_vertices():
        v.set_distancia(sys.maxsize)
        v.set_anterior(None)
        v.unset_visitado()

    g.get_vertice(s).set_distancia(0)
    g.get_vertice(s).set_anterior(None)


def computeGCD(x, y):
    while (y):
        x, y = y, x % y

    return x


def export_list(g):
    l = list()
    for i in g.get_vertices():
        for j in i.get_vertices_adjacentes():
            l.append([i.get_id(), j.get_id(), i.get_peso(j)])
    return l


def caminho_min(w):
    q = list()
    q.append(w.get_id())
    while w.get_anterior() != None:
        q.append(w.get_anterior().get_id())
        w = w.get_anterior()
    return q


def extract_min(Q):
    min = Q[0]
    for v in Q:
        if v.get_distancia() < min.get_distancia():
            min = v
    Q.remove(min)
    return min


def contador(v, time):
    v.set_distancia(time)


def contadorF(v, t):
    v.set_f(t)


def predecessor(v, u):
    v.set_anterior(u)


def uri(v, u, f, d):
    if v.get_id() == f:
        d.append(u.get_distancia() + u.get_peso(v))


def setBusca(v, u):
    v.set_distancia(u.get_distancia() + u.get_peso(v))
    v.set_anterior(u)


def relax(u, v):
    if v.get_distancia() > u.get_distancia() + u.get_peso(v):
        setBusca(v, u)


def caminho_minino(v, caminho):
    if v._anterior:
        caminho.append(v.get_anterior().get_id())
        caminho_minino(v.get_anterior(), caminho)
    return
