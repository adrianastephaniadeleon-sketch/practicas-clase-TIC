#Programa apoyo a la familia
sexo=input("Ingresa el sexo de la persona")
edad=input("Ingresa la edad")
estcivil=input("Ingresa tu estado civil")
hijos=float(input("Ingresa la cantidad hijos"))
if sexo=="mujer" and hijos==1 and edad<18:
    print("Eres mujer tienes un hijo y eres menor de edad entonces tu apoyo sera de 800")
elif sexo=="mujer" and hijos==1 and edad>=18:
    print("Eres mujer,tienes un hijo y eres mayor de dad entonces el apoyo será de 300")
elif sexo=="mujer" and hijos>1 and edad<18:
    print("Eres mujer, tienes más de un hijo y eres menor de edad entonces el apoyo es de 1500")
elif sexo=="mujer" and hijos>1 and edad>=18: 
    print("Eres ,mujer, tienes más de un hijo y ya eres mayor de edad entonceas el apoyo es de 500")
elif sexo=="hombre" and hijos=>1 and estadocivil=="soltero"
    print("Eres hombrey tienes hijos el apoyo es de 780")
else:
     print("No válido")
