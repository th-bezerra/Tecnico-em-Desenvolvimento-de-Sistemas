posicao_inicial = float(input("Digite a Posição Inicial: "))
posicao_final = float(input("Digite A Posição Final: "))
tempo_inicial = float(input("Digite o Tempo Inicial: "))
tempo_final = float(input("Digite o tempo final: "))

Vm = (posicao_final - posicao_inicial)/(tempo_final - tempo_inicial)

print("A Velocidade média é: ",Vm)