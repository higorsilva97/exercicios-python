from datetime import datetime

def voto(a):
    anoatual = datetime.now().year
    idade = anoatual - a
    if 18 <= idade <= 70:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO ')
    elif 16 <= idade <= 17:
        return print(f'Com {idade} anos: VOTO OPICIONAL ')
    elif idade < 16:
        return print(f'Com {idade} anos: NÃO VOTA ')
    elif idade > 70:
        return print(f'Com {idade} anos: VOTO OPICIONAL ')






ano = int(input('Em que ano voce nasceu? '))
voto(ano)