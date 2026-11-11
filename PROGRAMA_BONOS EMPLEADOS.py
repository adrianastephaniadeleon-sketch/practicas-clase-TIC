#Programa para solicitar los requisitos del empleado
nombre=(input("Ingresa el nombre"))
pagohr=float(input("Ingresa el pago por hora"))
Hrstrabajadalmes=float(input("Ingresa horas trabajadas al mes"))
sueldo=pagohr*Hrstrabajadalmes
if sueldo>=100 and sueldo<=300:
    bono=500
    print("tu sueldo es", sueldo+bono)
elif sueldo>300 and sueldo<=1500:
     bono=1700
     print("tu sueldo es", sueldo+bono)
elif sueldo>1500 and sueldo<=3000:
    bono=3500
    print("tu sueldo es", sueldo+bono)
elif sueldo>3000 and sueldo<=3000:
     bono=8500
     print("tu sueldo es", sueldo+bono)
elif sueldo>8000:
    bono=10000
    print("tu sueldo es", sueldo+bono)

else:
    "No válido"