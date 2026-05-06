palavra = input("Digite uma palavra: ")


vogais = "aeiouáàãâéêíóôúAEIOUÁÃÀÂÉÈÊÍÌÎÓÒÕÔÚÙÛ"


contador = 0

for letra in palavra:
    if letra in vogais:
        contador += 1

print("A palavra possui vogais: ",contador)
