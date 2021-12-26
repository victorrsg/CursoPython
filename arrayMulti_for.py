matriz= [1,2,3,4],[5,6,7,8]

# Primero recorremos todas las filas de la matriz con un for
# Necesitamos usar un enumerador para poder guardar su índice de fila
for i, fila in enumerate(matriz):
    # Dentro de cada fila recorremos cada columna con otro for
    # Necesitamos usar un enumerador para poder guardar su índice de columna
    for j, columna in enumerate(fila):
        # A partir de ambos índices podemos comprobar la celda actual
        # Si es par asignamos a la celda un 0
        if matriz[i][j] % 2 == 0:
            matriz[i][j] = 0
        # En caso contrario, si es impar, le asignamos un 1
        else:
            matriz[i][j] = 1
print(matriz)

print("fin")




arraym=[12,11,13,14],[20,21,22,22]

for i,fil in enumerate(arraym):
    for j,col in enumerate(fil):
        if arraym[i][j] %2 == 0:
            arraym[i][j]=0
        else:
            arraym[i][j]=1

print(arraym)
