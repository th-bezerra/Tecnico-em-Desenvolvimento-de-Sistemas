palavras_com_a = []

for i in range(5):
    palavra = input("Digite uma palavra: ")
    palavras_com_a.append(palavra)
    if(palavra == "a" or palavra == "A"):
        palavras_com_a.append(palavra)

for fah in palavras_com_a:
   print(fah)