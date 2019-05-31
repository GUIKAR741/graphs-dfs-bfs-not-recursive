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


def dfs(g: dict, vi=None, conexo=False):
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
    tabela = {i: vertice(0, 0, 0) for i in g.keys()}
    if vi is None:
        grau = list(
            map(lambda x: x[0],
                sorted(map(lambda x: (x[0], len(x[1])), g.items()),
                       key=lambda x: x[1], reverse=True)))
    else:
        grau = vi
    r = grau.pop(0)
    t = 0
    while len(grau) > 0 or not (r is None):
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
                    grau.pop(grau.index(i))
                    tabela[i].ti = t = t+1
                    cont += 1
                    break
            if cont == 0:
                tabela[u].cor = 2
                tabela[u].tf = t = t+1
                p.pop()
        if len(grau) > 0:
            r = grau.pop(0)
        else:
            r = None
    if not conexo:
        ordTop = list(map(lambda x: x[0],
                          sorted(tabela.items(), key=lambda x: x[-1].tf, reverse=True)))
        print(tabela)
        print("Ordenação Topologica:", ' '.join(ordTop))
        conexos = dfs(gt(g), vi=ordTop, conexo=True)
        gr = list(sorted(map(lambda x: (x[0], x[1].ti), conexos.items()),
                         key=lambda x: x[1]))
        x = [[gr[0]]]
        for i in gr[1:]:
            if x[-1][-1][-1] == i[-1]-1:
                x[-1].append(i)
            else:
                x.append([])
                x[-1].append(i)
        x = list(map(lambda y: list(map(lambda z: z[0], y)), x))
        print(f'Componentes Conexas: {len(x)} componentes.', '; '.join([str(i) for i in x]))
    else:
        return tabela


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
                print('-'.join(filter(lambda x: not (x is None), l[::-1])), end='')
            print()
        print()


def gt(g: dict) -> dict:
    """."""
    gt = {i: [] for i in g.keys()}
    for i, j in g.items():
        for k in j:
            gt[k].append(i)
    return gt

v, e, g = CriaGrafo()
dfs(g)
bfs(g)
