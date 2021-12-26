numeros=[1,3,6,9]

while True:
    num=int(input("Dime un número del 0 al 9: "))
    if num>=0 and num<=9:
        break

if num in numeros:
    print("El número ",num," se encuentra en la lista")
else:
    print("El número ",num," no se encuentra en la lista")