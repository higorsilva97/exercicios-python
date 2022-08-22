
def notas(* n, sit=True):
    """
    Função para analisar notas e situações de varios alunos
    :param n: notas para serem analisadas
    :param sit: situação do aluno
    :return: dicionario com toda a situação do aluno
    """
    maior = menor = soma = media = 0
    dicionario = dict()
    qtd = len(n)
    dicionario['Quantidade'] = qtd

    for i in enumerate(n):
        soma += i[1]
        if maior < i[1]:
            maior = i[1]
    dicionario['Maior'] = maior

    menor = maior
    for i in enumerate(n):
        if menor > i[1]:
            menor = i[1]
    dicionario['Menor'] = menor

    media = soma/qtd
    dicionario['Media'] = media

    if sit:
        if media > 9:
            dicionario['Situação'] = 'Boa'
        elif 6 < media <= 8:
            dicionario['Situação'] = 'Razoavel'
        elif media < 6:
            dicionario['Situação'] = 'Ruim'

    return dicionario


resp = notas(2, 7, 10, sit=True)
print(resp)

