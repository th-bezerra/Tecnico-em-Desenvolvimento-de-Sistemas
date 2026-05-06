programa {
  funcao inicio() {
    inteiro num1, num2

    escreva("digite o 1 numero: ")
    leia(num1)

    escreva("digite o 2 numero: ")
    leia(num2)

    se(num1 > num2){
    escreva("O ",num1, " maior")
    }

    senao se(num2 > num1){
    escreva("O ",num2," maior")
    }

    senao se(num1 == num2){
    escreva("os numeros são iguais")
   
    }  
  }
}
