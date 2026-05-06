programa {
  funcao inicio() {
  inteiro idade

  escreva("Digite sua idade: ")
  leia(idade)

  se(idade>= 0 e idade<=12){
    escreva("Você é criança")
  }  

  senao se(idade >= 13 e idade<=17 ){
    escreva("Você é adolescente")
  }
  senao se(idade>=18 e idade<=59){
    escreva("Você é Adulto")
  }
  senao se(idade >= 60){
    escreva("Você é idoso")
  }

  }
}
