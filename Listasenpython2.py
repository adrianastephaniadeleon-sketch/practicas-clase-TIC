numeros=[]
i=0
while i<10:
    num=int(input("Ingresa un número:"))
    numeros.appened(num)
    i=i+1
print("Números pares.")
for num in numeros:
    if num%2==0:
        print(num)
#EXTRA: Crea una lista llamada numPares y agrega los que son pares.