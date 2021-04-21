datos = []
for i in range(1,7):
    nuevoDato = int( input( "Dime el dato número {}: ".format(i) ))
    datos.append(nuevoDato)
print ("Los datos al revés son: ")
for i in range(6,0,-1):
    print ( datos[i-1] )
