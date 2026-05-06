#Revisão vetores - 1
#Solicitar ao usuário a quantidade de números
#Preencher o vetor
#Percorrer o vetor e calcular a soma dos números 
#Exibir a soma
# ----------------------------------------------------------------

vetor = []
soma = 0
quantidade = int(input("Digite a quantidade de números: "))

for i in range(quantidade):
    vetor.append(int(input("Digite um número: ")))

for num in vetor:
    soma += num


print("A soma é: ",soma)