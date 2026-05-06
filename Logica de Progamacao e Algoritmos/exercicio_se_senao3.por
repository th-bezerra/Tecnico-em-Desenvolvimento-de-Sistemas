programa {
  funcao inicio() {
    inteiro lado1, lado2, lado3

    escreva("Digite o 1 lado: ")
    leia(lado1)

    escreva("Digite o 2 Lado: ")
    leia(lado2)

    escreva("Digite o 3 lado: ")
    leia(lado3)

    se(lado1 == lado2 ou lado2 == lado3 ou lado3==lado1){
      escreva("Seu triangulo é um triangulo Isósceles")
    }

    senao se(lado1 == lado2  e lado2 == lado3 e lado3 == lado1){
      escreva("Seu triangulo é um triangulo equilátero")
    }
    senao se(lado1 != lado2 e lado2 != lado3 e lado3 != lado1)
      escreva("Seu triangulo é um triangulo Escaleno")
    }
  }
}
