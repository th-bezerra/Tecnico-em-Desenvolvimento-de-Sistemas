maiores = 0
menores = 0

for i in range(6):
 
    idade = int(input("Digite uma idade: "))
    
  
    if (idade >= 18):
        maiores += 1
    else:
        menores += 1

print("Total de maiores de idade: ",maiores)
print("Total de menores de idade: ",menores)
