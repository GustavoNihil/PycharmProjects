




km=int(input('Digite o total de Km rodados com o carro: '))
dias=int(input('Insira a quantidade de dias pelos quais ele foi alugado: '))
print('O valor total a pagar será de R${:.2f}'.format(km*0.15+dias*60))
#aluguelCarro

cel=int(input('Digite um valor em graus Celsius para ser convertido em Fahrenheit: '))
print('{:.1f}°C são equivalentes à {:.1f}°F'.format(cel,(cel*9/5)+32))
#temperatura
real=int(input('Quantos reais vc tem em sua conta? '))
print('Convertendo para dolar isso dá um total de U${:.2f}'.format(real/5.16))
#dolares
n40=int(input('digite um número: '))
print('Seu número é {}'.format(n40))
n40=int(input('Digite outro valor: '))
print('Seu número é {}'.format(n40))
#troca de valor de variável


t=int(input('Digite um número para ver sua tabuada: '))
print('_'*11,'\n{} X 0 = {}\n{} X 1 = {}\n{} X 2 = {}\n{} X 3 = {}\n{} X 4 = {}\n{} X 5 = {}\n{} X 6 = {}\n{} X 7 = {}\n{} X 8 = {}\n{} X 9 = {}'.format(t,t*0,t,t*1,t,t*2,t,t*3,t,t*4,t,t*5,t,t*6,t,t*7,t,t*8,t,t*9),'\n___________')
#tabuada!
valorI=int(input('Digite o preço do produto: '))
print('O valor do produto com 5% de desconto será R${:.2f}'.format(valorI-(valorI*0.05)))
print('O valor do produto com 5% de desconto será R${:.2f}'.format(valorI*0.95))
#desconto5%!
altura=int(input('Digite a altura da sua parede em metros: '))
largura=int(input('Digite a largura da sua parede em métros: '))
area=altura*largura
print('Sua parede tem uma área de {}m^2, portanto serão necessários {} litros de tinta.'.format(area,area/2))
#pintor!
metro=int(input('Digite o valor em métros que deseja converter: '))
print('{}m são {}cm e {}mm'.format(metro,metro*10**2,metro*10**3))
#Metros!
prova1=int(input('Digite o resultado da primeira prova: '))
prova2=int(input('Digite o resultado da segunda prova: '))
print('A sua média foi de {}'.format((prova1+prova2)/2))
#Média!
n1=int(input('Digite um número'))
print('O dobro de {} é {}, seu triplo é {}, já sua raiz quadrada é {:.0f}'.format(n1,n1*2,n1*3,n1**(1/2)))
#Raiz!
n1=int(input('Digite um número'))
print('O sucessor do número {} é {}\nO antecessor é {}'.format(n1,n1+1,n1-1))
#Sucessor!


print('Olá humano')
nome=input('Qual seu nome?')
print('Seja bem vindo {}'.format(nome))
n1=int(input('Digite um número:'))
n2=int(input('Digite um segundo número:'))
s=n1+n2
print('A soma entre {} e {} é:{}'.format(n1,n2,s))
#soma!
print(type(s),type(nome))
valor=input('Digite algo')
print('O formato está em: {}'.format(type(valor)))
print('O valor digitado é numérico: {}'.format(valor.isnumeric()))
print('O valor digitado é alfabético: {}'.format(valor.isalpha()))
#amostragem de valor!