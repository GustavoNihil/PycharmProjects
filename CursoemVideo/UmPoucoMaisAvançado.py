import math
import random
import pygame
import datetime
print('Você está no \033[36mano de {}\033[m, \033[36mdia {}\033[m do \033[36mmês {}\033[m'.format(datetime.date.today().year,datetime.date.today().day,datetime.date.today().month))
#data atual



print('\033[0;31;40mteste de cores\033[m')

r1=float(input('Digite o valor (em cm) do comprimento da primeira reta: '))
r2=float(input('Digite o segundo valor: '))
r3=float(input('Digite o terceiro valor: '))
if r1 > r2:
    if r1 > r3:
        if r1 < r2 + r3:
            print('As circustâncias de formação de um triângulo foram cumpridas')
        else:
            print('As circustâncias de formação de um triângulo NÃO foram cumpridas')
    else:
        if r3 < r1 + r2:
            print('As circustâncias de formação de um triângulo foram cumpridas')
        else:
            print('As circustâncias de formação de um triângulo NÃO foram cumpridas')
else:
    if r2 > r3:
        if r2 < r1 + r3:
            print('As circustâncias de formação de um triângulo foram cumpridas')
        else:
            print('As circustâncias de formação de um triângulo NÃO foram cumpridas')
    else:
        if r3 < r1 + r2:
            print('As circustâncias de formação de um triângulo foram cumpridas')
        else:
            print('As circustâncias de formação de um triângulo NÃO foram cumpridas')

#formação de triângulo (35)!

salario=float(input('Digite o seu salário: '))
if salario <= 1250:
    print('Seu aumento será de R${:.2f}, totalizando R${:.2f}'.format(salario*0.15,salario+salario*0.15))
else:
    print('Seu aumento será de R${:.2f}, totalizando R${:.2f}'.format(salario*0.10,salario+salario*0.10))
#aumento salário (34)!

n1=int(input('Digite um número: '))
n2=int(input('Digite um segundo número: '))
n3=int(input('Digite um terceiro número: '))

if n1 > n2:
    if n1 > n3:
        print('O maior número é {}'.format(n1))
    else:
        print('O maior número é {}'.format(n3))
else:
    if n2 > n3:
        print('O maior número é {}'.format(n2))
    else:
        print('O maior número é {}'.format(n3))
           #maior
if n1 < n2:
    if n1 < n3:
        print('O menor número é {}'.format(n1))
    else:
        print('O menor número é {}'.format(n3))
else:
    if n2 < n3:
        print('O menor número é {}'.format(n2))
    else:
        print('O menor número é {}'.format(n3))
            #menor
            #outra forma: (comando "and")
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
else:
    if n3 < n1 and n3 < n2:
        menor = n3
#programa que mostre 3 n° e diga o maior e menor (33)!

ano = int(input('Digite um ano (digite "0" para atribuir o ano atual): '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano {} é bissexto'.format(ano))
        else:
            print('O ano {} NÃO é bissexto'.format(ano))

    else:
        print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} NÃO é bissexto'.format(ano))
# ano bissexto (32)!

km=int(input('Digite a quilometragem do percurso: '))
if km <= 200:
    print('O preço de uma viagem de {:.0f}km será de R${:.2f}'.format(km,km*0.5))
else:
    print('O preço de uma viagem de {:.0f}km será de R${:.2f}'.format(km,km*0.45))
#preço passagem (31)!

vpi=int(input('Digite um número: '))
if (vpi % 2) != 0:
    print('O número {} é ímpar'.format(vpi))
else:
    print('O número {} é par'.format(vpi))

#par ou impar (30)!

velocidade=float(input('Digite a velocidade do carro: '))
if velocidade <= 80:
    print('Tudo certo, você não foi multado')
else:
    print('Você foi multado no valor de R${:.2f}'.format(7*(velocidade-80)))

#velocidade carro (29)!

nlista=[0,1,2,3,4,5]
nesc=int(input('O computador escolheu um número inteiro aleatório entre 0 e 5, tente adivinhar qual foi: '))
nale=random.choice(nlista)
print('O número escolhido pelo computador foi {}'.format(nale))
if nesc == nale:
    print('Parabéns, você acertou!\nSua chance de acerto era de {:.2f}%'.format(1/6*100))
else:
    print('Não foi dessa vez, você errou!\nTente novamente, em cada tentativa sua chance de acerto se mantem em {:.2f}%'.format(1/6*100))
#random (28)!

nome=str(input('Digite seu nome: '))
nomeup=nome.upper()
if nomeup == 'GUSTAVO':
    print('Que nome lindo')
else:
    print('Que nome mediocre')
print('Seja bem vindo, {}!'.format(nome))
#nome lindo

idadec=float(input('Quantos anos tem seu carro? '))
if idadec<=3:
    print('Seu carro está novinho! :D')
else:
    print('Seu carro está velho! :c')
#condição

nome=input('Digite seu nome: ')
nome=nome.split()
contagem=len(nome)
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[contagem-1]))
#primeiro e ulktimo nome(27)!

qualquer=input('Digite algo: ')
qualquer=qualquer.strip().upper()
contagem=qualquer.count('A')
print('A frase inserida possuí {} aparições da letra "A"'.format(contagem))
print('Sua primeira aparição é na posição {}'.format(qualquer.find('A')+1))
print('Sua ultima aparição foi na posição {}'.format(qualquer.rfind('A')+1))
#26!

nome=input('Digite seu nome: ')
nome=nome.upper()
print('Seu nome tem "Silva": {}'.format('SILVA' in nome))
#25!

cidade=input('Digite o nome da sua cidade: ')
cidade=cidade.upper().split()
print('Sua cidade começa com "Santo": {}'.format('SANTO'in cidade[0]))
#24!

numero=int(input('Digite um número: '))
u=(numero%10)/1
d=(numero%100-u)/10
c=(numero%1000-d*10-u)/100
m=(numero%10000-c*100-d*10-u)/1000
print('Analisando o número {}'.format(numero))
print('Unidade:{:.0f}'.format(u))
print('Decimais: {:.0f}'.format(d))
print('Centenas: {:.0f}'.format(c))
print('Milhares: {:.0f}'.format(m))
#23!

nome=str(input('Digite seu nome completo: '))
print('Em maiusculo: {}'.format(nome.upper()))
print('Em minusculo: {}'.format(nome.lower()))
nome=nome.split()
print('Seu nome tem {} letras'.format(len(''.join(nome))))
print('Seu primeiro nome tem {} letras'.format(len(nome[0])))
#22!

#Manipulação de cadeia de texto (fatiamento de str)

pygame.init()
pygame.mixer.music.load('Hey Jude.mp3')
pygame.mixer.music.play()
print('Agora tocará Hey Jude xD')
 #pygame.event.wait()
#tocar musiquinha xD (21)

a1=input('Digite um nome para atribuí-lo à uma sequência: ')
a2=input('Digite o segundo nome: ')
a3=input('digite o terceiro nome: ')
a4=input('Digite o quarto nome: ')
lista = [a1,a2,a3,a4]
print('A ordem será:',lista)
ordem = random.shuffle(lista)
print('A ordem será:',lista)
#ordenar (20)!

a1=input("Didite o nome do 1° aluno: ")
a2=input('Agora digite o nome do 2°: ')
a3=input('3°: ')
a4=input('4°: ')
lista = [a1,a2,a3,a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
#sorteio alunos (19)!

ang=int(input('Digite o ângulo que deseja: '))
#          é necessário converter de graus para pi rad.
rad=math.radians(ang)
sen=math.sin(rad)
co=math.cos(rad)
tg=math.tan(rad)
print('{:.2f}° são {:.2f}pi rad., tendo seno = {:.2f},coseno = {:.2f} e tangente = {:.2f}'.format(ang,rad,sen,co,tg))
#sen cos e tg (18)!

catO=int(input('Digite o valor do cateto oposto de um triângulo retangulo: '))
catA=int(input('Digite o valor do cateto adjacente do mesmo triângulo: '))
hip=(catA**2)+(catO**2)
print('Com base nos valores {} e {} sua hipotenusa é {:.0f}'.format(catO,catA,hip**(1/2)))
print(9**2,9**(1/2))
#Hipotenusa(17)!

num=int(input('Digite um número para saber sua raíz: '))
raiz=math.sqrt(num)
print('A raíz quadrada de {} é {}'.format(num, math.ceil(raiz)))

numAle1=random.random()
#              Número entre 0 e 1
numAle2=random.randint(1, 10)
print(numAle1)
print(numAle2)







