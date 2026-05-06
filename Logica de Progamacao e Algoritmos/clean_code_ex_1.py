numeros = []

for i in range(5):
    try:
        numeros.append(float(input(f"Digite {i+1} Número: ")))

        soma = sum(numeros)

    except ValueError:
        print("Erro: Insira um número válido!")

print("A Soma é: ",soma)