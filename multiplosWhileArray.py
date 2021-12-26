numero=int(input("Dime un número del 1 al 9: "))

while numero<1 or numero>9:
    numero=int(input("Dime un número del 1 al 9: "))
    
print("Has elegido el número: ",numero)

multiplos= []
multiplos= list(range(0,101,numero))
print(multiplos)
