num=int(input("Cuantos números quiere introducir: "))
suma=0
for i in range(num):
    suma+=float(input("dime un número: "))
    

print("La suama de todos los números es: ",suma," y su media aritmética es: ",suma/num)
