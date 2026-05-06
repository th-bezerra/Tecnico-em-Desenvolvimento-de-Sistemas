valorCompra = float(input("Digite o valor da compra: "))
cupom = input("Você possui cupom? ")

if(valorCompra >= 200 or cupom == "Sim"):
    print("Você ganhou um desconto de 15%! ")
else:
    print("Você não tem direito ao desconto neste momento! ")