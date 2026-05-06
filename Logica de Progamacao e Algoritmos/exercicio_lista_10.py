numeros = []

for i in range(6):
    numeros.append(int(input("Digite um número: ")))
    
for num in numeros:
    if(num %2 == 0):
        print(num)