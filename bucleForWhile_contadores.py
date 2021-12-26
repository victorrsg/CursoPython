lista=[1,2,3,4,5,6,7,8,9,10]
i=0

while i<len(lista):
    print (lista[i])
    i+=1

print("Fin del programa")

#----------------------------------
for valor in lista:
    print(valor)
print("Fin del programa")

#-----------------------------------
i=0
lista=[1,2,3,4,5,6,7,8,9,10]
for valor in lista:
    lista[i]*=10
    i+=1
print(lista)

print("Fin del programa")
#------------------------------
cadena="Hola mundo"

for caracter in cadena:
    print(caracter)

print("Fin del programa")

#for in range

print("10 primeros números: ")
for i in range(10):
    print(i)