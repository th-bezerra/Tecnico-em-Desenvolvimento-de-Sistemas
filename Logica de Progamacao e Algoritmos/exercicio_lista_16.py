numeros = []

for i in range(6):
    num = int(input("Digite um número: "))

    if(num < 0):
        numeros.append(1)

    else:
        numeros.append(num)

print(numeros)