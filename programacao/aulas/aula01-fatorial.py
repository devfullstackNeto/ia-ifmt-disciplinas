# 6 = 6x5x4x3x2x1 = 720

numero = int(input("Digite um número: "))
fatorial = 1
while(numero >= 1):
    fatorial = fatorial * numero
    print (numero ," x ")
    numero = numero - 1
    
print(fatorial)