from defs import*


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("ERRO ao ler o arquivo.")
    else:
        cabeçalho("PESSOAS CADFASTRADAS")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<34}{dado[1]:>3} anos')
    finally:
        a.close()

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um ERRO com a criação do arquivo.")
    else:
        print(f"Arquivo {nome} criado com sucesso.")


def cadastrar(arq, nome="desconhecido", idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um ERRO na abertura do arquivo.")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print("Houve um ERRO ao criar o cadastro.")
        else:
            print(f"Novo registro de {nome} efetuado com sucesso.")
    a.close()