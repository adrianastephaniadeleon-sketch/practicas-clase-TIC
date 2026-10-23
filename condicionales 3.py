#Programa que me diga si puedo sacar cartilla militar
sex=float(input("Dame tu sexo"))
edad=float(input("Dame tu edad"))
if sex=="hombre" and edad>=18:
    print("Puedes sacar tu cartilla militar")
else:
    print("No puedes")
