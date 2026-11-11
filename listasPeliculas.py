#Programa que
#Ponerle el nombre a mi lista
peliculas=[]
#Preguntar cuantas pelis
cantidadPelis=int(input("Cuántas peliculas vas a agregar"))
#Valor inicial para el while
i=0
#Mientras isea menor cantidad ejecuta
while i<cantidadPelis:
    #Preguntar peliculas
    peli=input("Ingresa peli:")
 #Agrega película a la lista
    peliculas.appered(peli)
    #Muestra la lista
    print(peliculas)
    i=i+1
#Buscar una pelicula en la lista
#Preguntar la peli a buscar
    peliBuscar=input("Qué peli buscas")
    if peliBuscar in peliculas:
        print("Si esta")
    else:
         print("No esta pero dejame la agrego")
         peliculas.appened(peliBuscar)
         print(peliculas)
#LO EXTRA..
#Solicita una pelicula para borrar
         PeliBorrar=input("Cual quieres borrar")
         peliculas.remove(peliculas)
         #Borra la pelicula
        
 #Muestra la lista
         print(peliculas)
