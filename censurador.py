print ("Este es un censurador de frases")
frase = input("Escribe tu frase: ")
palabra_prohibida = input("Escribe la palabra que quisieras censurar: ")
nueva_palabra = input("Escribe la palabra por la que quisieras reemplazarla: ")
nueva_frase = frase.replace(palabra_prohibida, nueva_palabra)
print ("Tu nueva frase censurada es: ", nueva_frase)
