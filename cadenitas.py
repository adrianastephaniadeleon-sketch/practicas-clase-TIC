nombre="Fany"
frase="El cielo es hermoso"
print(nombre)
print(frase)
#Mostrar el nombre en mayus
print(nombre.upper())
print(frase.upper())
#Mostrar en minusculas
print(frase.lower())
#Obtener un carácter en una posición
letra=frase[4]
print(letra)
frase2="El mundo es bonito"
print(frase2.split("-"))
nombreC="Fany de león Colmenero"
print(nombreC.split("-"))
#Dos primeras letras del nombre
letras1=nombreC[0:2]
print(letras1)
nuevaF=frase.replace("hermoso", "maravilloso")
print(nuevaF)
#Numero de caracteres de la cadena: largo
largoCadena=len(nuevaF)
print(largoCadena)