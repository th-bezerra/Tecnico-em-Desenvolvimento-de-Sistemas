lado1 = int(input("Digite o lado 1: "))
lado2 = int(input("Digite o 2 lado: "))
lado3 = int(input("Digite o 3 lado: "))

if((lado1+lado2)>lado3 and (lado1+lado3)> lado2 and (lado2 + lado3)>lado1):
    if(lado1 == lado2 and lado2 == lado3 and lado3 == lado1 ):
        print("Equilátero! ")
    elif(lado1 != lado2 and lado2 != lado3 and lado3 != lado1):
        print("Escaleno")
    else:
        print("Isósceles! ")
else:
    print("Triangulo não existe! ")