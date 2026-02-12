# Ler um número
numero = int(input("Digite um número: "))
inverso = 0
# pensamento computacional
while numero != 0:
    resto = numero % 10
    numero = numero // 10
    inverso = inverso * 10 + resto
    
# começo outro bloco
print(inverso)