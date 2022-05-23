import defs
from arquivo import*


arq = "ListaNomes.txt"

if arquivoExiste(arq):
    print("Arquivo encontrado com sucesso.")
else:
    print("Arquivo não encontrado.")
    criarArquivo(arq)

while True:
    resposta = defs.menu(["Lista de pessoas cadastradas", "Cadastrar pessoa", "Sair do sitema"])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        defs.cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = defs.leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        defs.cabeçalho("Saindo do sistema... Até logo.")
        break
    else:
        defs.cabeçalho("\033[0;31m[ERRO] Por favor digite um valor válido.\033[m")



