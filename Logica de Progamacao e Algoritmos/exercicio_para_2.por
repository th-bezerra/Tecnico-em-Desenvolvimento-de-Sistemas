programa {
  funcao inicio() {
    inteiro inicio, fim, soma = 0

    escreva("Digite o número inicial: ")
    leia(inicio)

    escreva("Digite o número Final: ")
    leia(fim)

    para(inteiro i=inicio; i<=fim;i++){
      se(i%2 == 0){
        soma = soma + i
      }
    }
    escreva("A soma dos pares é: ",soma)
  }
}
