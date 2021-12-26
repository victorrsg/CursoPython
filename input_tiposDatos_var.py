# Completa el ejercicio
nombre = input("Dime tu nombre ")
apellido = input("Dime tu apellido ")
edad = input("Dime tu edad ")
edad=int(edad)
numero_magico = input("Dime un número con decimales ")
numero_magico=float(numero_magico)

cadena_final=(nombre + " "+ apellido + " Tu número de la suerte es " + str(edad*numero_magico))
print(cadena_final)