cantidad=(int(input("Digite la cantidad de números: ")))
total=0
for variable in range(cantidad):
    n=int(input("Digite un número: "))
    total+=n
    print("El total de la suma es: ",total)