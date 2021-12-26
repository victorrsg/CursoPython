numero1 = int(input("Dime el primer número: "))
numero2 = int(input("Dime el segundo número: "))

print("Dime que quieres hacer con tus números: ")
print("1. Suma de los dos números: ")
print("2. Resta: ")
print("3. Multiplicación: ")

opcion=int(input("¿Qué opción deseas?: "))

if opcion=="1":
    resultado = numero1+numero2
    print("la suma de los dos números es: ",resultado)
elif opcion=="2":
    resultado= numero1-numero2
    print("La resta de los dos números es: ",resultado)
elif opcion=="3":
    resultado=numero1*numero2
    print("El producto de los dos números es: ",resultado)
else:
    print("No ha elegido una opción correcta")


print("Fin del programa")
