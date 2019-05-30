"""."""
from math import floor


def CriaGrafo() -> (int, int, dict):
    """."""
    v, e = [int(i) for i in input().split()]
    grafo = dict()
    ent = []
    for i in range(e):
        ent.append(input().split())
        grafo[ent[-1][0]] = []
        grafo[ent[-1][1]] = []
    for v1, v2 in ent:
        grafo[v1].append(v2)
    return v, e, grafo


def dfs(g: dict):
    """.

    cor: 0=branco, 1=cinza, 2=preto
    """
    class vertice:
        """."""

        def __init__(self, cor, ti, tf):
            """."""
            self.cor = cor
            self.ti = ti
            self.tf = tf

        def __repr__(self):
            """."""
            return f"vertice(cor={self.cor}, ti={self.ti}, tf={self.tf})"
    chaves = [*g.keys()]
    tabela = {i: vertice(0, 0, 0) for i in g.keys()}
    grau = list(map(len, g.values()))
    r = chaves[grau.index(max(grau))]
    t = 0
    tabela[r].cor = 1
    tabela[r].ti = t = t+1
    p = [r]
    while len(p) > 0:
        u = p[-1]
        cont = 0
        for i in sorted(g[u]):
            if tabela[i].cor == 0:
                tabela[i].cor = 1
                p.append(i)
                tabela[i].ti = t = t+1
                cont += 1
                break
        if cont == 0:
            tabela[u].cor = 2
            tabela[u].tf = t = t+1
            p.pop()
    print(tabela)


def bfs(g: dict):
    """.

    cor: 0=branco, 1=cinza, 2=preto
    """
    class vertice:
        """."""

        def __init__(self, cor, d, p):
            """."""
            self.cor = cor
            self.d = d
            self.p = p

        def __repr__(self):
            """."""
            return f"vertice(cor={self.cor}, d={self.d}, p={self.p})"
    chaves = [*g.keys()]
    print('bfs:')
    for s in sorted(chaves):
        tabela = {i: vertice(0, None, None) for i in g.keys()}
        # s = chaves[floor(len(chaves)/2)]
        tabela[s].cor = 1
        tabela[s].d = 0
        q = [s]
        while len(q) > 0:
            u = q.pop(0)
            for v in g[u]:
                if tabela[v].cor == 0:
                    tabela[v].cor = 1
                    tabela[v].d = tabela[u].d+1
                    tabela[v].p = u
                    q.append(v)
            tabela[u].cor = 2
        c = 'inf'
        for i in sorted(tabela.items(), key=lambda x: x[0]):
            print(f"{i[0]}: {i[1].d if not (i[1].d is None) else c} -> ", end='')
            if i[1].p is None:
                print('null', end='')
            else:
                l = [i[0]]
                while not (l[-1] is None):
                    l.append(tabela[l[-1]].p)
                print('-'.join(filter(lambda x: not (x is None), l)), end='')
            print()
        print()

v, e, g = CriaGrafo()
dfs(g)
bfs(g)
