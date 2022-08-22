def notas(* n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAVOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(2, 7, 10, sit=True)
print(resp)