ainicio=int(input("Ingrese un año: "))
afin=int(input("Ingrese otro año "))
for a in range(ainicio,afin+1):
    if not a%10==0:
        continue
    if not a%4==0:
        continue
    if a%100!=0 or a%400==0:
        print(a)