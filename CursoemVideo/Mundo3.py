import random
import time
from datetime import datetime
from time import sleep
from operator import itemgetter   # ordenação de bibliotécas



c = ('\033[m', # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;45m' # 3 - roxo
    )


def ajuda(h):
    título(f'Acessando o comando "{h}"', 2)
    print(c[3], end="")
    print(help(h))
    print(c[0], end="")


def título(msg, cor = 0):
    print(c[cor], end="")
    tam = len(msg) + 4
    print("-" * tam)
    print(f"  {msg}")
    print("-" * tam)
    print(c[0], end="")


comando = ""
while True:
    título("Assistente PyHELP", 2)
    comando = input("Função ou Bibliotéca: ")
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
título("Tchau xD.", 1)

# - 106 ****


def notas(* nota, show = False):
    """
    -> Função para analisar a situação de vários alunos.
    :param nota: Uma ou mais notas de alunos [é possível inserir quantas quiser].
    :param show: [valor opcional] Indica se deve ser mostrada a situação da turma [caso não seja informado um valor é atribuído como False].
    :return: Retorna um dicionário com as informações da turma.
    """
    dicioNotas = {}
    total = 0
    maior = 0
    menor = 0
    contador = 0
    for v in nota:
        total += v
        contador += 1
        if contador == 1:
            maior = menor = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v
    quantidade = len(nota)
    dicioNotas["total de notas"] = contador
    dicioNotas["total de notas2"] = quantidade
    dicioNotas["maior"] = maior
    dicioNotas["menor"] = menor
    media = total / quantidade
    dicioNotas["média"] = media
    if show:
        if media < 6:
            dicioNotas["situação"] = "RUIM"
        elif media >= 6 and media < 7:
            dicioNotas["situação"] = "RAZOÁVEL"
        else:
            dicioNotas["situação"] = "BOA"
    return dicioNotas


resp = notas(8.5, 3.2, 6, show = True)
print(resp)
resp = notas(4.8, 6.7, 8.2, 8)
print(resp)
resp = notas(5.6, 9, show = True)
print(resp)
print(help(notas))

# - 105 ****


def leiaInt(msg):
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print("\033[0;31mERRO. Por favor digite um valor númerico inteiro válido.\033[m")
    return valor


n = leiaInt("Digite um número: ")
print(f"O número digitado foi {n}.")

# - 104 ****


def ficha(nome="<anônimo>", gols=0):
    if nome == "":
        nome = "<anônimo>"
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


no = input("Nome do jogador: ")
gol = input("Número de gols: ")
ficha(no, gol)


# Função Ficha, que receba 2 parâmetros opcionais(nome e gols). Mostrar a ficha do jogador - 103 ****


def fatorial(n=0, show="S"):
    global fat
    fat = 1
    num = n
    if n == 0:
        print("O fatorial de 0 é: 0")
    else:
        for c in range (0, n):
            fat *= num
            if show in "Ss" and num > 1:
                print(f"{num} x ", end="")
            if show in "Ss" and num == 1:
                print(f"1 = ", end="")
            num -= 1
        if show in "Ss":
            print(f"{fat}. ", end="")
        print(f"O resultado de {n} fatorial é: {fat}.")


fatorial(2, "N")
fatorial(4)
fatorial(5, "N")
fatorial(5)
fatorial(5, "S")
fatorial(0)
fatorial(1)
fatorial(13)

# Função de fatorial que receba um número e tenha um parâmetro opicional (chamado show) que define se será mostrado o processo de cálculo - 102 ****


def voto(a):
    global idade
    idade = datetime.now().year - a
    if idade < 16:
        return "NEGADO"
    elif idade >= 16 and idade < 18:
        return "OPCIONAL"
    elif idade >= 18 and idade < 65:
        return "OBRIGATÓRIO"
    else:
        return "OPICIONAL"


anon = int(input("Qual seu ano de nascimento: "))
resultado = voto(anon)
print(f"Você tem {idade} anos, portanto o voto é {resultado}.")

# - 101 ****


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("Digite um número: "))
if par(num):
    print("É par.")
else:
    print("Não é par.")


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s # O valor é atribuído a uma variável


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f"Meus cálculos deram {r1}, {r2} e {r3}.")

def teste(b):
    global a # Escopo global e escopo local (apenas dentro da função)
    a = 8
    b += 4
    c = 2
    print(f"A dentro vale {a}.")
    print(f"B dentro vale {b}.")
    print(f"C dentro vale {c}.")
a = 5
teste(a)
print(f"A fora vale {a}.")


def contador(i=0, f=0, p=1): # "p=1" -> Opcional. Se não for informado um valor para "p" ele recebe 1
    """ # 3 áspas duplas para adicionar uma descrição ao help da função
        -> Faz uma contagem e mostra na tela.
        :param i: início da contagem
        :param f: fim da contagem
        :param p: passa da contagem
        :return: sem retorno
        Função criada por Gustavo Monteiro Laperriere.
    """
    c = i
    while c <= f:
        print(f"{c}", end="..")
        c += p
    print("FIM!")


contador(0, 100, 10)
help(contador)
for _ in range(5):
    print('.', end='', flush=True)
    time.sleep(0.5)
print('Pronto!')


lista = []


def sorteia():
    print("O valores sorteados foram: ", end="")
    for c in range(0, 5):
        lista.append(random.randint(0, 9))
        print(f"{lista[c]}", end=" ")
    print("")


def somaPar():
    soma = 0
    print("A soma dos números pares foi: ", end="")
    for c in range(0, 5):
        if lista[c] % 2 == 0:
            soma += lista[c]
    print(f"{soma}")


sorteia()
somaPar()

# - 100 ****


def vmaior(* valores):
    print(f"Foram inseridos {len(valores)} números: ", end="")
    contador = maior = 0
    for v in valores:
        print(f"{v} ", end="")
        if contador == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        contador += 1
    print("")
    print(f"O maior valor inserido foi {maior}.")


vmaior(1, 0, 13, -2, 8, 5)
vmaior(-2, -3, -8, -44, -1)
vmaior(9, 5, 4, 12, 0)
vmaior(6)
vmaior()

# Usa uma função que mostre os valores inseridos, quantos valores foram informados e qual o maior número inteiro - 99 ****


def pulos(inicio, fim, passo):
    print(f"A contagem se inicia em {inicio:.1f}, termina em {fim:.1f} e tem um passo de {passo:.1f}:", end=" ")
    contador = 0
    if passo == 0:
        passo *= -1
    if passo < 0:
        passo = - passo
    if inicio < fim:
        num = 0
        while num + passo <= fim:
            if contador == 0:
                num = inicio
            else:
                num += passo
            print(f"{num:.1f}", end=" ")
            contador += 1
            sleep(0.3)
    else:
        num = fim + passo + 1
        while num - passo >= fim:
            if contador == 0:
                num = inicio
            else:
                num -= passo
            print(f"{num:.1f}", end=" ")
            contador += 1
            sleep(0.3)
    print("")


pulos(1, 10, 1)
pulos(10, 0, 2)
n1 = float(input("Digite o valor de início: "))
n2 = float(input("Digite o valor de fim: "))
passoo = float(input("Digite o valor dos pulos: "))
pulos(n1, n2, passoo)

# - 98 ****

def escreva(txt):
    print("-"*len(txt))
    print(txt)
    print("-"*len(txt))


escreva("Monotremados")
escreva("MACACO VAI CAÍ")
escreva("Seu Lobato, um cara muito foda, tinha um sítio; Yahh Yahh Ohhh.")

# - 97 ****

def área():
    l1 = float(input("Digite o comprimento do terreno(em metros): "))
    l2 = float(input("Digite a largura do terreno(em metros): "))
    area = l1 * l2
    print(f"A área do terreno é de {area:.2f}m^2.")


área()

# - 96 ****

def contador(* num): # cria uma tupla com os valores, portanto independe do número de variáveis
    tam = len(num)
    if tam == 1:
        print(f"Foi cadastrado {tam} número:", end=" ")
    else:
        print(f"Ao todo são {tam} números:", end=" ")
    for n in num:
        print(f"{n}", end=" ")
    print("FIM.")


contador(1, 2, 3, 4, 5, 6, 8)
contador(2, 55, 13, 90)
contador(666)


def soma(a, b):
    s = a + b
    print(f"A soma de A + B = {s}")


soma(4, 5)
soma(b=8, a=9)
soma(2, 1)


def lin(msg):
    print("-"*30)
    print(f'{msg:^30}')
    print("-" * 30)


# 2 linhas vazias
lin("Ronaldo")
lin("Ronaldinho")

#           FUNÇÕES

dados = {}
listadados = []
while True:
    dados["nome"] = input('Nome: ')
    dados["idade"] = int(input("Idade: "))
    dados["sexo"] = " "
    contador = 0
    while dados["sexo"] not in "MF":
        if contador == 0:
            dados["sexo"] = input("Sexo [M/F]: ").upper()[0] #[0] pega somente a primeira letra
            contador += 1
        else:
            dados["sexo"] = input("Por favor digite um valor válido para sexo [M/F]: ").upper()[0]
    listadados.append(dados.copy()) #.copy() = [:] /// sum(nomedalista) (soma os elementos de uma lista)
    dados.clear()
    continuar = " "
    while continuar not in "SsNn":
        continuar = input('Deseja continuar [S/N]: ')
    if continuar in "Nn":
        break
if len(listadados) == 1:
    print(f"Foi cadastrada {len(listadados)} pessoa.")
else:
    print((f"A- Foram cadastradas {len(listadados)} pessoas."))
totalid = 0
for n in range(0, len(listadados)):
    totalid += listadados[n]["idade"]
media = totalid / len(listadados)
print(f"B- A média de idade do grupo é de {media} anos.")
print(f"C- As mulheres do grupo são: ", end="")
for n in range(0, len(listadados)):
    if listadados[n]["sexo"] == "F":
        print(listadados[n]["nome"], end=" ")
print("")
print(f"D- As pessoas com idade acima da média são: ")
for n in range(0, len(listadados)):
    if listadados[n]["idade"] >= media:
        print(f'{listadados[n]["nome"]}, com {listadados[n]["idade"]} anos.')

# - 94 ****

dados = {}
dados["nome"] = input('Nome: ')
anonas = int(input('Ano de nascimento: '))
dados["idade"] = datetime.now().year - anonas
dados["ctps"] = int(input("Carteira de Trabalho (caso não tenha digite 0): "))
if dados["ctps"] != 0:
    dados["contratação"] = int(input("Digite o ano de contratação: "))
    dados["salário"] = float(input("Digite seu salário: "))
for c, v in dados.items():
    print(c, v)

# - 92 ****

jogadores = {'Jogador1': random.randint(1, 6), 'Jogador2': random.randint(1, 6), 'Jogador3': random.randint(1, 6), 'Jogador4': random.randint(1, 6)}
ranking = list()
for j, n in jogadores.items():
    print(f"{j} tirou {n} no dado.")
    time.sleep(0.8)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # itemgetter = 0 -> Ordena por keys | itemgetter = 1 -> Ordena por values
print(ranking)
for j, n in enumerate(ranking):
        print(f"{j + 1}° lugar: {n[0]}, com {n[1]}.")

# - 91 ****

dados = {}
dados["Nome"] = input("Nome: ")
dados["Média"] = float(input("Média: "))
if dados["Média"] >= 7:
    dados["Situação"] = "Aprovado"
elif 5 <= dados["Média"] < 7:
    dados["Situação"] = "Recuperação"
else:
    dados["Situação"] = "Reprovado"
print(f"Nome tem valor {dados['Nome']}.")
print(f"Média tem valor {dados['Média']}.")
print(f"Situação tem valor {dados['Situação']}.")

# Leia o nome e média de um aluno. Guarde a situação (aprovado caso média superios a 7/10) em um dicionário. Mostre o conteúdo da estrutura - 90 ****

brasil = []
estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1.copy()) #.copy funciona como o [:] em listas
brasil.append(estado2.copy())
for c in brasil:
    for u, s in c.items():
        print(f"{u} tem valor {s}.")
for c in brasil:
    contador = 0
    for u in c.values():
        contador += 1
        if contador % 2 == 0:
            print(f"{u}.")
        else:
            print(f"{u} tem a sigla", end=' ')


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 19, 'jooj': 'Ablublublé'}
del pessoas['jooj']
pessoas['nome'] = 'Débora'
pessoas['peso'] = 52
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f"{k} = {v}.")


#             DICIONÁRIOS

contador = 0
todasnotas = []
notas = []
while True:
    notas.append(input("Digite o nome do aluno: "))
    notas.append(float(input("Digite a primeira nota do aluno: ")))
    notas.append(float(input("Digite a segunda nota do aluno: ")))
    todasnotas.append(notas[:])
    notas.clear()
    contador += 1
    continuar = " "
    while continuar not in "SsNn":
        continuar = input("Deseja continuar [S/N]: ")
    if continuar in "Nn":
        break
print(f"{'Índice:':^7}|{'Alunos:':^20}|{'Média:':^20}")
for n in range(0, len(todasnotas)):
    print("-"*49)
    print(f"{n:^7}|{todasnotas[n][0].upper():^20}|{(todasnotas[n][1]+todasnotas[n][2])/2:^20.1f}")
while True:
    indice = int(input('''Digite o número do índice do aluno que deseja ver
as notas (999 para encerrar o programa): '''))
    if indice == 999:
        break
    elif indice > len(todasnotas) - 1 or indice < 0:
        print('Valor de índice inválido. Por favor insira um valor válido.')
    else:
        print(f"A primeira nota de {todasnotas[indice][0].upper()} foi {todasnotas[indice][1]}, a segunda nota foi {todasnotas[indice][2]}.")

# Leia o nome e 2 notas de vários alunos, Mostre um boletim com a média de cada um, Permita que mostra as notas de cada aluno - 89 ****

jogos = int(input('Quantos jogos você deseja gerar: '))
listam = []
lista = []
numero = 0
for c in range(0, jogos):
    lista.append(random.randint(0,60))
    for c in range(0, 5):
        numero = lista[0]
        while numero in lista:
            numero = random.randint(0, 60)
        lista.append(numero)
    listam.append(lista[:])
    lista.clear()
for c in range(0, jogos):
    print(f"{c + 1}° jogo: {listam[c]}")
    sleep(0.6)
print("-"*10,"Boa sorte :D.","-"*10)

# - 88 ****

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para linha {l}, coluna {c}: "))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^3}]", end='')
    print('')
soma = 0
for e in pares:
    soma += e
print(f"o valor da soma dos numeros pares é {soma}.")
soma = 0
for e in range(0, 3):
    soma += matriz[e][2]
print(f"A soma dos valores da terceira coluna é {soma}.")
maior = 0
for e in range(0, 3):
    if matriz[1][e] > maior:
        maior = matriz[1][e]
print(f"O maior valor da segunda linha é {maior}.")

# - 87 ****

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para linha {l}, coluna {c}: "))
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^3}]", end='')
    print('')

# matriz - 86 ****

impar = []
par = []
for c in range(0, 7):
    numero = int(input(f"Digite o {c+1}° número: "))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
par.sort()
impar.sort()
todos = [impar[:], par[:]]
print(f"Os números impares são: {todos[0]}")
print(f"Os números pares são: {todos[1]}")

# - 85 ****

nopeso = []
cadastro = []
while True:
    continuar = " "
    nome = input('Nome: ')
    idade = int(input('Peso: '))
    cadastro.append(nome)
    cadastro.append(idade)
    nopeso.append(cadastro[:])
    cadastro.clear()
    while continuar not in "SsNn":
        continuar = input('Deseja continuar [S/N]: ')
    if continuar in "Nn":
        break
maiorp = []
menorp = []
print(f'Ao todo foram cadastradas {len(nopeso)} pessoas.')
for c, t in enumerate(nopeso):
    if c == 0:
        maiorp.append(nopeso[0][1])
        menorp.append(nopeso[0][1])
        maiorp.append(nopeso[0][0])
        menorp.append(nopeso[0][0])
    else:
        if nopeso[c][1] > maiorp[0]:
            maiorp.clear()
            maiorp.append(nopeso[c][1])
            maiorp.append(nopeso[c][0])
        elif nopeso[c][1] == maiorp[0]:
            maiorp.append(nopeso[c][0])
        if nopeso[c][1] < menorp[0]:
            menorp.clear()
            menorp.append(nopeso[c][1])
            menorp.append(nopeso[c][0])
        elif nopeso[c][1] == menorp[0]:
            menorp.append(nopeso[c][0])
print(f'O maior peso foi de {maiorp[0]}kg. Peso de {maiorp[1:]}')
print(f'O menor peso foi de {menorp[0]}kg. Peso de {menorp[1:]}')

# - 84 ****

nomeid = list()
nomes = list()
nomeid.append('Gustavo')
nomeid.append(19)
nomes.append(nomeid[:])
nomeid[0] = 'Camila'
nomeid[1] = 27
nomes.append(nomeid[:])
print(nomeid)
print(nomes)
print(nomes[0][1], nomes[1][1])
for p in nomes:
    print(f'{p[0]} tem {p[1]} anos.')

# parte 2 de listas (listas dentro de listas)

valores = input('Digite uma expressão: ')
pilha = []
for s in valores:
    if s == "(":
        pilha.append("(")
    elif s == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print('A expressão é válida.')
else:
    print('A expressão NÃO é válida.')

# - 83 ****

todosv = []
imparv = []
imparv2 = []
parv = []
parv2 = []
while True:
    sn = ' '
    num = int(input('Digite um número: '))
    todosv.append(num)
    if num % 2 == 0:
        parv.append(num)
    else:
        imparv.append(num)
    while sn not in "NnSs":
        sn = input('Deseja continuar [S/N]: ')
    if sn in "Nn":
            break
print(todosv)
print(f'Os números pares são: {parv}')
print(f'Os números impares são: {imparv}')
for n in todosv:
    if n % 2 == 0:
        parv2.append(n)
    else:
        imparv2.append(n)
print(parv2)
print(imparv2)

# - 82 ****

lista = []
contador = 0
for v in range(0, 5):
    contador += 1
    num = int(input('Digite um valor: '))
    if contador == 1:
        lista.append(num)
    if contador == 2:
        if num >= lista[0]:
            lista.append(num)
        else:
            lista.insert(0, num)
    if contador == 3:
        if num <= lista[0]:
            lista.insert(0, num)
        else:
            if num <= lista[1]:
                lista.insert(1, num)
            else:
                lista.append(num)
    if contador == 4:
        if num <= lista[0]:
            lista.insert(0, num)
        else:
            if num <= lista[1]:
                lista.insert(1, num)
            else:
                if num <= lista[2]:
                    lista.insert(2, num)
                else:
                    lista.append(num)
    if contador == 5:
        if num <= lista[0]:
            lista.insert(0, num)
        else:
            if num <= lista[1]:
                lista.insert(1, num)
            else:
                if num <= lista[2]:
                    lista.insert(2, num)
                else:
                    if num <= lista[3]:
                        lista.insert(3, num)
                    else:
                        lista.append(num)
print(lista)

# - 80 ****

valores = []
while True:
    continuar = ' '
    valores.append(int(input('Digite um número: ')))
    if valores.count(valores[len(valores) - 1]) > 1:
        print('Valor inválido. Não é possivel adicionar o mesmo valor 2 ou mais vezes.')
        valores.pop()
    else:
        print('Valor adicionado com sucesso.')
    while continuar not in "sSnN":
        continuar = input('Deseja continuar [S/N]: ')
    if continuar in "Nn":
        break
valores.sort(reverse=True)
print(valores)
print(f'Você digitou os valores: {sorted(valores)}')

# - 79 ****

valores = []
p = 0
for c in range(0, 5):
    valores.append(int(input('Digite um número: ')))
print(f'O maior valor foi {max(valores)}, nas posições', end=' ')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i + 1}...', end='')
print('')
print(f'O menor valor foi {min(valores)}, na posição {valores.index(min(valores)) + 1}.')

# leia 5 valores. Mostre o maior e o menor, com suas respectivas posições - 78 ****

a = [2, 8, 3, 5]
b = a[:] # criar uma cópia dos valores de "a", mas sem manter uma conexão entre as listas
print(b)

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Final')

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True) # ordenar do maior para o menor
num.insert(2, 0)
if 4 in num:
    num.remove(4)
else:
    print('Não encontrei o número 4.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')


# LISTAS

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'suprassumo', 'nietzsche', 'schopenhauer', 'spinoza', 'niilismo', 'nihil')
for p in palavras:
    print(f'Na palavra "{p}" temos: ', end='')
    for letra in p: # as palavras são uma lista de letras
        if letra.lower() in 'aeiou':
            print(letra, end='')
    print('')

# - 77 ****

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}') #centralizar
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>8.2f}')
print('-' * 40)

# - 76 ****

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite outro número: '))
tupla = (n1, n2, n3, n4)
print(tupla)
n1 = 2
print(tupla) # O valor de n1 em tupla não é alterado

print(f'No total o número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O primeiro 3 foi inserido na posição {tupla.index(3) + 1}.') #mostrar posição
else:
    print('O número 3 não apareceu em nenhuma posição')
print('Os números pares são: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
print('')

# - 75 ****

tupla = (random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))
for c in tupla:
    print(c, end=' ')
print(f'\nO menor valor é {sorted(tupla)[0]}.') # max(tupla)
print(f'O maior valor é {sorted(tupla)[4]}.') # min(tupla)

# - 74 ****

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = -1
while numero < 0 or numero > 20:
    numero = int(input('Digite um número (entre 0 e 20): '))
print(f'Você digitou o número {tupla[numero]}.')

# - 72 ****

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5)) #número de aparições

lanches = ('hamburguer', 'suco', 'pizza', 'pudim')
for c in lanches:
    print(c)
for cont in range(0, len(lanches)): #tamanho
    print(lanches[cont])
print(sorted(lanches)) #ordena

# TUPLAS (são imutáveis)