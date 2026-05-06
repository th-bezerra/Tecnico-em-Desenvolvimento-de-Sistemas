num1 = int(input("Digite o 1 número: "))
num2 = int(input("Digite o 2 número: "))
operacao = input("Digite a operação (+, -,*,/): ")

if(operacao == "+"):
    resultado = num1+num2
elif(operacao == "-"):
    resultado = num1-num2
elif(operacao == "*"):
    resultado = num1*num2
elif(operacao == "/" and num2 != 0):
    resultado = num1/num2
else:
    resultado = "ERRO"
print("O resultado é: ",resultado)