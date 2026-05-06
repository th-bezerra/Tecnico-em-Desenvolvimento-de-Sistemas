matriz1 = []
matriz2 = []
matriz_soma = []

# Preencher matriz (repetir sempre que preencher matriz)
for i in range(3):
    linha = []
    for j in range(3):
        matriz1.append(int(input(f"Matriz 1[{i}][{j}] = "))) 
    matriz1.append(linha)

# Preencher matriz (repetir sempre que preencher matriz)
for i in range(3):
    linha = []
    for j in range(3):
        matriz2.append(int(input(f"Matriz 2[{i}][{j}] = "))) 
    matriz2.append(linha)

# Preencher matriz (repetir sempre que preencher matriz)
for i in range(3):
    linha = []
    for j in range(3):
        matriz1.append(matriz1[i][j] + matriz2[i][j]) 
    matriz_soma.append(linha)
 
 # Repetir matriz (repetir sempre que exibir matriz)
print("Matriz soma: ")
for linha in matriz_soma:
    print(linha)