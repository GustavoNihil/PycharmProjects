def formata(res=0):
    return f"R${res:.2f}".replace(".", ",")


def aumentar(preço=0, taxa=0):
    res = preço + (preço * taxa / 100)
    return formata(res)


def diminuir(preço=0, taxa=0):
    res = preço - (preço * taxa / 100)
    return formata(res)


def dobro(preço=0):
    res = preço * 2
    return formata(res)


def metade(preço=0):
    res = preço / 2
    return formata(res)


