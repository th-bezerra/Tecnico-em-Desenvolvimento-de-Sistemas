numeros = []
soma = 0
media = 0

for i in range(4) :
    num = int(input("Digite o número: "))
    numeros.append(num)

for numero in numeros : 
    soma = soma + numero

media = soma /4
print("A Média é: ",media)

if(media < 4):
    print("Reprovado! ")

elif(media >= 4 and media <= 7):
    print("Recuperação! ")
else:
    print("Aprovado! ")