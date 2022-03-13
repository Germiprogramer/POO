def moveralaizquierda(tabla, max, min):
    for i in range(min, (max-1)):
      tabla[i] = tabla[i+1]
    return tabla
print(moveralaizquierda([1,2,5,3,2,1,4,7], 5, 2))



