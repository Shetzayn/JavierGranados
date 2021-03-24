n=int(input("Digite el número: "))
f=1
if n!=0:
    for x in range(1,n+1):
        f=f*x
print("El factorial es: ",f)