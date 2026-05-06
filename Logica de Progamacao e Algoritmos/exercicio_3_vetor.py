numeros = []
soma = 0
media = 0

for i in range(4):
    num = int(input("Digite a nota: "))
    numeros.append(num)

for nota in numeros :
    soma = soma + numeros

 media = soma /4

if(nota <= 4 ):
    print("Reprovado! ")
elif(nota >= 4 and <= 7):
    print("Recuperação! ")
else:
    print("Aprocado")
