positivo = 0
negativo = 0

for i in range(10):
    num = int(input("Digite um número: "))

    if(num > 0):
        positivo = positivo + 1
    elif(num < 0):
        negativo = negativo + 1

print("Os numeros positivos são: ",positivo)
print("Os numeros negativos são: ",negativo)