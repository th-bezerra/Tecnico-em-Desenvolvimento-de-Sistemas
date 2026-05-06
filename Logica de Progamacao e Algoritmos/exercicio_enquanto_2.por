programa {
   inclua biblioteca Util --> u
  funcao inicio() {
    inteiro contador =10

    enquanto(contador >= 0){
      escreva(contador)
      escreva("\n")
      u.aguarde(1000)
      contador = contador -1
    }
  }
}