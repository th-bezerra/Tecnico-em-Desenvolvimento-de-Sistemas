#Criando uma variavel númerica 
numero = 10

#Criando uma variavel textual
nome = "Gabriel"

#Usuario inserir um texto
nome_completo = input("Digite seu nome: ")

#Usuario inserir um numero inteiro
idade = int(input("Digite sua idade: "))

#Usuario inserir um numero decimal
salario = float(input("Digite seu salario: "))

#Estruturas condicionais - IF
if(salario > 1500 and idade >= 18):
    print("Pode tirar carta! ")
elif(salario < 1500 or idade < 18):
    print("Não pode tirar carta! ")
else:
    print("Invalido! ")

#Estruturas condicionais exemplo 2
turno = input("Digite seu turno (M/V/N): ")

if(turno == "M"): #Utilize dois iguais para comparar
    print("Bom dia ☀️")
elif(turno == "V"):
    print("Boa Tarde ☕")
elif(turno == "N"):
    print("Boa noite 🌒 ")
else:
    print("Inválido 🫥")

#Estrutura de repetição
#0 -> 10
for i in range(11): #Sempre coloque +1
    print(i)

# 1 -> 15
for i in range(1,16): #Vai de 1 até 15
    print(i)

# 5 -> 65 (Aumentando de 5 em 5)
for i in range(5,66,+5):
    print(i)

# 122 -> 0 (tirando de 2 em 2)
for i in range(122,-1,-2):
    print(i)

#Usuario escolhe inicio e fim
#inicio -> fim
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))

for i in range(inicio, fim+1):
    print(i)

#Vetores 
nomes = []

#Sempre utilizar  pra preencher o vetor
for i in range(5):
    nomes.append(input("Digite um nome: "))

#Sempre utilizar para exibur o vetor
for nome in nomes:
    print(nome)