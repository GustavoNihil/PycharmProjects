import random
from time import sleep
from datetime import date



valor = int(input('Digite o valor que deseja sacar: '))
notas50 = 0
notas20 = 0
notas10 = 0
notas1 = 0
while valor != 0:
    if valor >= 50:
        valor -= 50
        notas50 += 1
    elif valor >= 20:
        valor -= 20
        notas20 += 1
    elif valor >= 10:
        valor -= 10
        notas10 += 1
    elif valor >= 1:
        valor -= 1
        notas1 += 1
if notas50 >= 1:
    print(f'Total de {notas50} cédula(s) de R$50,00.')
if notas20 >= 1:
    print(f'Total de {notas20} cédula(s) de R$20,00.')
if notas10 >= 1:
    print(f'Total de {notas10} cédula(s) de R$10,00.')
if notas1 >= 1:
    print(f'Total de {notas1} cédula(s) de R$1,00.')

# qual valor deseja ser sacado (inteiro). Informará quantas cédulas de cada valor serão entregues. 50, 20, 10, 1 - 71 ****

gasto = 0
mais1000 = 0
numpro = 0
barato = 0
valbarato = 0
while True:
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))
    numpro += 1
    gasto += valor
    if valor >= 1000:
        mais1000 += 1
    if numpro == 1:
        barato = nome
        valbarato = valor
    else:
        if valor < valbarato:
            barato = nome
            valbarato = valor
    continuar = ' '
    while continuar not in "SsNn":
        continuar = input('Deseja continuar [S/N]: ')
    if continuar in "Nn":
        break
print(f'O valor total da compra foi de R${gasto:.2f}.')
print(f'Ao todo foram comprados {mais1000} produtos que custam mais de R$1000,00.')
print(f'O produto mais barato comprado foi {barato}, por R${valbarato:.2f}.')

# leia o nome e o preço de vários produtos. Pergunta se quer continuar. No final mostre: Total gasto na compra; Quantos produtos custam mais de R$1000;
# Qual o nome do produto mais barato. - 70 ****

contidade = 0
conthomens = 0
contmulheres = 0
cadastrados = 0
while True:
    nome = input('Digite o nome do indivíduo: ')
    sexo = ""
    while sexo != "M" and sexo != "m" and sexo != "F" and sexo != "f":
        sexo = input('Qual o gênero biológico [M/F]: ')
    idade = int(input('Insira a idade: '))
    if idade >= 18:
        contidade += 1
    if sexo in "Mm":
        conthomens += 1
    if sexo in "Ff":
        if idade < 20:
            contmulheres += 1
    cadastrados += 1

    continuar = ""
    while continuar != "n" and continuar != "N" and continuar != "s" and continuar != "S":
        continuar = input('Deseja continuar [S/N]? ')
    if continuar in "Nn":
        break
print(f'Ao todo foram cadastradas {cadastrados} pessoas.')
print(f'Ao todo são {contidade} com mais de 18 anos.')
print(f'Foram cadastrados {conthomens} homens.')
print(f'O total de mulheres com mais de 20 anos é {contmulheres}.')

# leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada pergunta se quer continuar. No final mostre: Quantas pessoas tem mais de 18 anos;
# Quantos homens foram cadastrados; Quantas mulheres tem menos de 20 anos - 69 ****

nump = 0
vitorias = 0
while True:
    impar = ""
    numc = random.randint(0, 5)
    while impar != "impar" and impar != "par":
        impar = input('Escolha ímpar ou par: ')
        impar = impar.lower()
    nump = -1
    while nump < 0 or nump > 5:
        nump = int(input('Digite um número (entre 0 e 5): '))
    soma = nump + numc
    if impar == "impar":
        if soma % 2 == 0:
            print(f'Você perdeu, meu parceirinho. O computador escolheu {numc}. Total de {soma}, deu PAR.')
            break
        else:
            print(f'Você venceu, meu parceirinho. O computador escolheu {numc}. Total de {soma}, deu IMPAR.')
    if impar == "par":
        if soma % 2 == 0:
            print(f'Você venceu, meu parceirinho. O computador escolheu {numc}. Total de {soma}, deu PAR.')
        else:
            print(f'Você perdeu, meu parceirinho. O computador escolheu {numc}. Total de {soma}, deu IMPAR.')
            break
    vitorias += 1
    print('Vamos jogar novamente...')
print('Você teve um total de {} vitória(s) consecutiva(s).'.format(vitorias))

# jogue par ou ímpar. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou. - 68 ****

while True:
    num = int(input('Digite um número (digite um número negativo para encerrar): '))
    if num < 0:
        break
    for c in range(0, 10):
        print('{} X {} = {} '.format(c, num, num * c))
print('tchau.')

# mostre a tabuada de vários números, um de cada vez, de acordo com o valor inserido. O programa será interrompido quando o número solicitado for negativo - 67 ****

soma = 0
valores = 0
while True:
    num = float(input('Digite um número (para parar digite 999): '))
    if num == 999:
        break
    valores += 1
    soma += num
print(f'A soma dos {valores} números é igual a {soma:.2f}.')

# 66 ****

continuar = "S"
soma = 0
div = 0
maior = 0
menor = 0
while continuar in "sS":
    num = float(input('Digite um número: '))
    continuar = input('Deseja continuar[S/N}? ')
    div += 1
    soma += num
    if num >= maior:
        maior = num
    if div == 1:
        menor = num
    if num <= menor:
        menor = num

print('Foram digitados {} números, com uma média de valores de {:.2f}.'.format(div, soma/div))
print('O maior número digitado foi {:.2f} e o menor número digitado foi {:.2f}.'.format(maior, menor))

# leia vários números. No final mostre a média entre todos, o maior e o menor. Deve perguntar se ele quer continuar digitando valores - 65 ****

valor = int(input('Digite um número (para encerrar digite 999): '))
contador = 0
soma = 0
while valor != 999:
    contador += 1
    soma += valor
    valor = int(input('Digite um número (para encerrar digite 999): '))
print('No total foram digitados {} números, totalizando uma soma com valor de {}.'.format(contador, soma))

#999 - 64 ****

nf = int(input('Quantos elementos de uma sequência de fibonacci você deseja que sejam mostrados: '))
cont = 0
anterior = 0
atual = 1
while cont < nf:
    print('{}'.format(atual), end=' ')
    anterior += atual
    cont += 1
    if cont < nf:
            print('{}'.format(anterior), end=' ')

    atual += anterior
    cont += 1
print('')

# leia um número 'n' inteiro e mostre os 'n2' primeiros elementos de um sequência de fibonacci (Ex: 1, 1, 2, 3, 5, 8) - 63 ****

numI = int(input('Digite o valor inicial da PA: '))
razao = int(input('Digite o valor de progressão da PA: '))
print('Os primeiros 10 números dessa PA são: ', end='')
for c in range (1, 10):
    if c == 1:
        print('{} {} '.format(numI, numI + razao), end='')
    else:
        print('{} '.format(numI + razao * c), end='')
print('')
rep = 1
contador = 0
vezes = 0
while rep > 0:
    rep = int(input('Mais quantos números você deseja que sejam mostrados, meu parceirinho? '))
    repnum = rep
    if repnum >= 1:
        if contador == 0:
            vezes = 0
        else:
            vezes += repnum
        for c in range(1, repnum + 1):
            print('{} '.format(numI + (razao * (9 + vezes)) + razao * c), end='')
    contador += 1
print('Tchau.')


# mostre os primeiros 10n de uma PA e depois pergunte mais quantos números desejam ser mostrados (encerrra quando for dito 0) - 62 ****

num = int(input('Digite um número: '))
cont = num
contador2 = 1
fatorial = 1
while cont > 2:
    if contador2 == 1:
        cont = num - 1
    else:
        cont = cont - 1
    if contador2 == 1:
        fatorial = num * cont * fatorial
    else:
        fatorial = cont * fatorial
    contador2 += 1

if num == 1:
    print('O valor do fatorial de 1 é 1.')
elif num == 2:
    print('O valor do fatorial de 2 é 2.')
else:
    print('O valor do fatorial de {} é {}.'.format(num, fatorial))

# leia um número qualquer e mostre o seu fatorial. Ex: 5! - 60 ****

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um segundo número: '))
menu = 0
contador = 1
while menu != 5:
    if contador != 1:
        sleep(2)
    print('''[1] Somar;
[2] Multiplicar;
[3] Maior;
[4] Novos números;
[5] Sair do programa.''')
    menu = int(input('Digite o número da opção desejada: '))
    if menu == 1:
        print('A soma entre {} e {} é {}.'.format(n1, n2, n1+n2))
    elif menu == 2:
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, n1*n2))
    elif menu == 3:
        if n1 == n2:
            print('Os 2 valores digitados são iguais.')
        elif n1 > n2:
            print('O número {} é maior do que {}.'.format(n1, n2))
        else:
            print('O número {} é maior do que {}.'.format(n2, n1))
    elif menu == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite um segundo número: '))
    contador += 1
print('Tchau. Volte sempre xD.')

# leia 2 valores. Apareça um menu com as opções: 1- somar, 2- multiplicar, 3- maior, 4- novos números, 5- sair do programa (menu reaparece) - 59 ****

nump = int(input('Tente acertar o número inteiro escolhido pelo computador (entre 0 e 10): '))
numc = random.randint(0, 10)
contagem = 1
while nump != numc:
    print('Você errou, o número escolhido pelo computador foi {}.'.format(numc))
    nump = int(input('Tente novamente, meu parceirinho: '))
    contagem += 1
    numc = random.randint(1, 10)
if contagem == 1:
    print('Parabéns, você acertou de primeira!!!')
else:
    print('Parabéns, você acertou na {}° tentativa.'.format(contagem))

# tentar acertar o número escolhido pelo computador. No final mostrar qual foi o número de tentativas - 58 ****

s = input('Digite seu gênero biológico, por favor [F/M]: ')
while s != 'F' and s != 'f' and s != 'M' and s != 'm':
    s = input('Digite um valor válido para seu gênero biológico, por favor [F/M]:')
if s in 'Ff':
    print('Gênero biológico definido como feminino.')
else:
    print('Gênero biológico definido como masculino.')

# - 57 ****

par = 0
impar = 0
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('No total foram digitados {} múmeros impares e {} números pares.'.format(impar, par))

r = 'S'
while r in 'Ss':
    n = int(input('Digite um número: '))
    r = input('Você quer continuar? [S/N] ')
print('Fim.')

c = 1
while c < 10:
    print(c)
    c += 1

#                        **** ESTRUTURA DE REPETIÇÃO "WHILE" ****

ini = 1
totid = 0
maxid = 0
nvelho = ''
cmulher = 0
for c in range(1, 5):
    print('----- {}° PESSOA -----'.format(ini))
    ini += 1
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Gênero Biológico [M/F]: ')
    totid += idade
    if idade > maxid:
        maxid = idade
        nvelho = nome
    if sexo in 'Ff': # in ao invés de == para atribuir o 'f' tbm
        if idade < 20:
            cmulher += 1

medid = totid/4
print('A média de idade do grupo é de {} anos.'.format(medid))
print('{} é a pessoa mais velha, com {} anos.'.format(nvelho, maxid))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cmulher))

# leia o nome, idade e sexo de 4 pessoas. No final mostra a média de idade do grupo; qual o nome do homem mais velho; quantas mulheres têm menos de 20 anos - 56 ****

pmax = 0
pmin = 0
pessoa = 1
for c in range(0, 5):
    peso = float(input('Digite o {}° peso: '.format(pessoa)))
    pessoa += 1
    if c == 0:
        pmax = peso
        pmin = peso
    if peso > pmax:
        pmax = peso
    if peso < pmin:
        pmin = peso
print('O maior peso foi {}(uni.) e o menor peso foi {}(uni.).'. format(pmax, pmin))

# leia 5 pesos e diga qual o maior e qual o menor - 55 ****

first = 1
atual = date.today().year
mai = 0
for ver in range(0, 7):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(first)))
    first += 1
    if atual - ano >= 21:
        mai += 1
print('Temos então {} maiores de idade e {} menores.'. format(mai, 7 - mai))

# leia o ano de nascimento de 7 pessoas e mostra quantas pessoas ainda não atingiram a maioridade (21 anos) e quantas atingiram - 54 ****

cesp = input('Digite uma frase: ')
sesp = cesp.strip()
sesp = sesp.split()
sesp = ''.join(sesp)
sesp = sesp.lower()
print(sesp)
inverso = ''
tam = len(sesp)
for letra in range(tam - 1, -1, -1):
    inverso += sesp[letra]
print(inverso)
if sesp == inverso:
    print('A frase supracitada é um palíndromo.')
else:
    print('A frase supracitada não é um palíndromo.')

# leia uma frase e diga se ela é um palíndromo (pode-se ler de trás para a frente e tem o mesmo sentido), desconsiderando os espaços - 53 ****

num = int(input('Digite um número: '))
totd = 0
for c in range(1, num + 1):
    div = num % c
    if div == 0:
        print('\033[33m', end='')
        totd += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\033[m')
if totd > 2:
    print('O número {} não é primo, pois possuí {} divisores.'.format(num, totd))
else:
    print('O número {} é primo, pois só possuí {} divisores.'.format(num, totd))

# leia e diga se um número é primo ou não - 52 ****

t1 = float(input('Digite o termo inicial da PA: '))
ra = float(input('Digite a razão da PA: '))
for c in range(0, 10):
    t1 = t1 + ra
    print(t1, end=' ')

# leia o primeiro termo e a razão de uma PA. Mostre os 10 primeiros termos dessa progressão - 51 ****

soma = 0
for c in range(0, 6):
    nfor = int(input('Digite um número: '))
    if nfor % 2 == 0:
        soma += nfor
print('A soma dos números pares é {}.'.format(soma))

# leia seis números inteiros e mostre apenas a soma dos pares - 50 ****

somac = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        somac += c
print(somac)
print(cont)

# soma de todos os números ímpares, multiplos de 3, no intervalo de 1 ate 500 - 48 ****

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')

# mostre todos os números pares no intervalo de 1 a 50 - 47 ****


i = int(input('Início: '))           # 'end''' -> faz com que o próximo print seja executado na mesma linha
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)

for c in range(0, 6): #ignora o último número
    print(c)
print(c) # A variável mantem a última atribuição
for c in range(6, 0, -1):
    print(c)
for c in range(0, 7, 2):
    print(c)

#         ****ESTRUTURAS DE REPETIÇÃO****
itens = ('s', 'Pedra', 'Papel', 'Tesoura')
escolha = input('Escolha entre "pedra", "papel" e "tesoura": ')
print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PO!!!')
if escolha == "pedra":
    nj = 1
elif escolha == "papel":
    nj = 2
elif escolha == "tesoura":
    nj = 3
else:
    print('Por favor insira um valor válido.')
nm = random.randint(1,3)
if nj == nm and nj != 0:
    print('Empate, ambos escolheram {}.'.format(escolha))
elif nj == 1:
    if nm == 2:
        print('Você perdeu, a máquina escolheu papel.')
    else:
        print('Você ganhou, a máquinha escolheu tesoura.')
elif nj == 2:
    if nm == 1:
        print('Você ganhou, a máquina escolheu pedra.')
    else:
        print('Você perdeu, a máquina escolheu tesoura.')
else:
    if nm == 1:
        print('Você perdeu, a máquina escolheu pedra.')
    else:
        print('Você ganhou, a máquina escolheu papel.')
print('O computador escolheu {}.'.format(itens[nm]))

#jokenpô - 45 ****

l1 = float(input('Digite o valor do 1° lado do triângulo: '))
l2 = float(input('Digite o valor do 2° lado do triângulo: '))
l3 = float(input('Digite o valor do 3° lado do triângulo: '))
if l1 >= l2 + l3 or l2 >= l1 + l3 or l3 >= l1 + l2:
    print('valores inválidos, não há como formar um triângulo com os dados fornecidos.')
elif l1 == l2 and l2 == l3:
    print('O triângulo é equilátero.')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('O triângulo é isóceles.')
else:
    print('O triângulo é escaleno.')

#trinângulos (equi, isó e esc) - 42 ****

idade = int(input('Digite sua idade: '))
if idade == 18:
    print('Está na hora de se alistar, meu parceirinho.')
elif idade < 18:
    print('Você terá que se alistar daqui {} ano(s).'.format(18-idade))
else:
    print("Você se alistou há {} ano(s).".format(idade-18))

#alistamento - 39 ****

num = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[1] conversão para BINÁRIO
[2] conversão para OCTAL
[3] conversão para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O número {} convertido para binário é {}.'.format(num, bin(num) [2:]))
elif opção == 2:
    print('O número {} em binário é {}.'.format(num, oct(num) [2:]))
elif opção == 3:
    print('O número {} em hexadecimal é {}.'.format(num, hex(num) [2:]))
else:
    print('Opção inválida.')

#conversam de um número para as bases numéricas: binária, octal e hexadecimal. - 37 ****

casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite seu salário mensal: '))
anos = int(input('Digite em quantos anos você deseja pagar: '))
meses = anos * 12
vlm = casa/meses
if sal*3/10 < vlm:
    print('Seu empréstimo foi negado.')
else:
    print('Seu empréstimo foi aprovado. Seu valor mensal será de {:.2f}'.format(vlm))

#emprestimo: parcelas não podem exceder 30% do salário - 36 ****

nome = input('Digite seu nome: ')
if nome == 'Gustavo':
    print('Que nome lindo.')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular.')
elif nome == '':
    nome = 'fantasma'
    print(f'Olá {nome}.')
else:
    print("Seu nome é bem normal.")
print('Tenha um bom dia, {}.'.format(nome))

#estrutura de condições


