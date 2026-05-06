programa {
   inclua biblioteca Util --> u
  funcao inicio() {
    inteiro contador=1

    enquanto(contador <=100){
      escreva(contador)
      escreva("\n")
      u.aguarde(500)
      contador = contador + 1
    }
  }
}
