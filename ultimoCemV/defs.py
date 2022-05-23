def linha(tam=42):
    return "-" * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    opc = "opc"
    while True:
        try:
            opc = int(input("\033[32mSua opção: \033[m"))
            break
        except:
            print("\033[0;31m[ERRO] Por favor digite um número inteiro válido.\033[m")
    return opc


def leiaInt(input2):
    valor = " "
    while True:
        try:
            valor = int(input(input2))
        except:
            print("ERRO. Por favor digite um valor válido.")
        else:
            return valor
            break

