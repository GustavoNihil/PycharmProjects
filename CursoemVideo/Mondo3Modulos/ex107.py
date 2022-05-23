import moeda


def resumo(valor=0, au=0, dim=0):
    print(f"Um investimento de {moeda.formata(valor)} acrescido de 10% é igual a: {moeda.aumentar(valor, au)}")
    print(f"Um produto que custa {moeda.formata(valor)} com 15% de desconta sai pelo valor de: {moeda.diminuir(valor, dim)}")
    print(f"O dobro de {moeda.formata(valor)} é: {moeda.dobro(valor)}")
    print(f"A metade de {moeda.formata(valor)} é: {moeda.metade(valor)}")


def dado(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if "," in entrada:
            entrada = entrada.replace(",", ".")
        if entrada.isalpha() or entrada.strip() == "":
            print(f'\033[0;31mERRO, "{entrada}" não é um valor válido.\033[m')
        else:
            try:
                entrada = float(entrada)
            except:
                print("\033[0;31m[ERRO]Houve um erro com o valor incerido.\033[m")
            else:
                valido = True
                try:
                    return entrada
                except:
                    print("Programa finalizado devido a um erro.")
