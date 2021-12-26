#Bucle anidado

lista=[1,2,3],[4,5,6]

for i,filas in enumerate(lista):
    for j,columnas in enumerate(filas):
        if lista[i][j]%2==0:
            lista[i][j]=0
        else:
            lista[i][j]=1
print(lista)