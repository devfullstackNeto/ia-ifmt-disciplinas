# Ler um número e saber se é primo e/ou perfeito
numero = int(input("Digite um número"))

contador = 0            # para achar o primo
soma = 0                # para achar o perfeito
divisor = 1
while divisor <= numero:
    if numero % divisor == 0:
        contador = contador + 1             # para achar primos
        soma = soma + divisor               # para achar perfeito
    divisor = divisor + 1

# Definir se é primo
if (divisor == 2):
    print("Numero é primo")
else:
    print("Número não é primo")
    
# Definir se é perfeito
if (soma-numero == numero):
    print("Número é perfeito")
else:
    print("Número é imperfeito")