# Ler um número
numero = int(input("Digite um número: "))
auxiliar = numero
expoente = 0
narcisista = 0
# pensamento computacional
while numero != 0:
    numero = numero // 10
    expoente = expoente + 1

print (expoente)

while auxiliar != 0:
    digito = auxiliar % 10
    narcisista = digito ** expoente + narcisista
    auxiliar = auxiliar // 10
    
if (numero == narcisista):
    print("É narcisista")