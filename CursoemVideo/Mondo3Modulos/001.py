import uteis # impotão de defs criadas
# Caso fosse usado "from uteis import fatorial, dobro" não haveria a necessidade do "uteis."

num = int(input("Digite um valor: "))
fat = uteis.fatorial(num)
print(f"O fatorial de {num} é {fat}.")
print(f"O dobro de {num} é {uteis.dobro(num)}.")
