#Ejercicio1
x = str(input("Ingrese un nombre: "))
alias = ("El Dios de Python")
print("Su nombre quedaría: ", x, alias)
#Ejercicio2
x = float(input("Ingrese un número: "))
y = float(input("Ingrese otro número: "))
print("La suma de los números es: ", x + y)
#Ejercicio3
x = float(input("Ingrese un número : "))
y = float(input("Ingrese otro número: "))
print("La suma de los números es ", x + y)
print("La resta de los números es ", x - y)
print("La multiplicación de los números es ", x * y)
print("La división de los números es ", x / y)
print("El residuo de los números es ", x % y)
#Ejercicio4
x = float(input("Ingrese un numero decimal: "))
parte_decimal, parte_entera = math.modf(x)
print("La parte entera del numero es {} y la parte decimal es {}".format(parte_entera, parte_decimal))
#Ejercicio 5
p1= 0.15
p2= 0.20
p3= 0.15
p4= 0.30
p5= 0.20
count = 1
while True:
    i = 0
    if count == 1:
            x = float(input("Ingrese la primera nota: "))
            i = x
    if count ==2:
            y =float(input("Ingrese la segunda nota: "))
            i = y
    if count == 3:
            z =float(input("Ingrese la tercera nota: "))
            i = z
    if count == 4:
            a =float(input("Ingrese la cuarta nota: "))
            i = a
    if count == 5:
            b =float(input("Ingrese la quinta nota: "))
            i = b
    if i > 0 and  i <= 5:
            count = count + 1
    if i>5:
            print("El valor ingresado es inválido, inténtelo de nuevo ")
    if count > 5:
            break
d =(x*p1) + (y*p2) + (z*p3) + (a*p4) + (b*p5)
#Ejericio6
compra = float(input("Ingrese el valor de la compra: "))
x = (compra * 0.19)
y = (compra * 1.19)
print("El valor original de la compra es de: ", compra)
print("El valor del IVA es de: ", x)
print("El valor de la compra con el IVA es de: ", y)
#Ejercicio7
x = float(input("Ingrese el radio de el círculo: "))
y = (2*3.14)*x
z = (3.14*(x**2))
print("El perimetro de su círuclo es equivalente a: ", y)
print("El área de su círculo es equivalente a: ",z)
#Ejercicio8
x= float(input("Ingrese el perímetro de el hexágono: "))
y= float(input("Ingrese el apotema de el hexágono: "))
print("El área de el hexágono es: ",(x*y)/2)
#Ejercicio9
x= float(input("Ingrese el primer número: "))
y= float(input("Ingrese el segundo número: "))
z= float(input("Ingrese el tercer número: "))
print("El promedio de los tres número es: ",(x+y+z)/3)
#Ejericio10
x = float(input("Ingrese el primer número: "))
y = float(input("Ingrese el segundo número: "))
print("El valor de x, antes del intercambio es: ",x,"El valor de y, antes del intercambio es: ",y)
print("El valor de x, después del intercambio es: ",y,"El valor de y, después del intercambio es: ",x)
#Ejericio11
altura = float(input("Ingrese la altura a la que será lanzado el objeto (metros): "))
print("El tiempo de caída del objeto es de", math.sqrt((2 * altura) / 10), "segundos")
#Ejercicio14
x= float(input("Ingrese la masa del objeto en kg: "))
y = 299792458000
print("La energía del objeto es de", x * y**2, "julios")
#Ejercicio15
x = float(input("¿Cúal es la coordenada 1?: "))
y = float(input("¿Cúal es la coordenada 2?: "))
z = float(input("¿Cúal es la coordenada 3?: "))
a = float(input("¿Cúal es la coordenada 4?: "))
print("La distancia entre los puntos es", math.sqrt((z - x)**2 + (a - y)**2))
# Ejercicio 16
x= float(input("Ingrese los segundos: "))
print(x, "segundos equivalen a", x / 3600, "horas")
#Ejercicio17
x = float(input("Ingrese los segundos: "))
print(x, "segundos equivalen a", x / 60, "minutos")
#Ejercicio18
x = float(input("Ingrese un tiempo en segundos: "))
y = x / 3600
z = x % 3600
a = z / 60
b = x % 60
print("la hora es:", int(y), int(a), b)
#Ejercicio19
cant = float(input("Ingrese una cantidad de dinero: "))
luca = round(cant / 1000)
if luca < 1:
    print("No tiene billetes de mil")
else:
    print("Tiene", luca, "billetes de mil")
dosk = round(cant / 2000)
if dosk < 1:
    print("No tiene billetes de dos mil")
else:
    print("Tiene", dosk, "billetes de dos mil")
cincok = round(cant / 5000)
if cincok < 1:
    print("No tiene billetes de cinco mil")
else:
    print("Tiene", cincok, "billetes de cinco mil")
diezk = round(cant / 10000)
if diezk < 1:
    print("No tiene billetes de diez mil")
else:
    print("Tiene", diezk, "billetes de diez mil")
veintek = round(cant / 20000)
if veintek < 1:
    print("No tiene billetes de veinte mil")
else:
    print("Tiene", veintek, "billetes de veinte mil")
cincuentak = round(cant / 50000)
if cincuentak < 1:
    print("No tiene billetes de cincuenta mil")
else:
    print("Tiene", cincuentak, "billetes de cincuenta mil")
cienk = round(cant / 100000)
if cienk < 1:
    print("No tiene billetes de cien mil")
else:
    print("Tiene", cienk, "billetes de cien mil")

#Ejercicio20
n= int(input("Ingrese un número (4 dígitos): "))
nreves = 0
while n > 0:
    res = n % 10
    nreves = (nreves*10)+res
    n = n // 10
print(f"El número reordenado inversamente es: {nreves}")
#Ejercicio21
n= int(input("Ingrese el número a comprobar si es par o no: "))
if n % 2 == 0:
    print("Es un número par")
else:
    print("Es un número impar")
#Ejercicio22
n = int(input("Ingrese el número para saber si es negativo o positivo: "))
if n  > 0:
    print("Es un número positivo")
else:
    print("Es un número negativo")
#Ejercicio23
n = int(input("Ingrese un número: "))
if n % 2 == 0:
    if n > 0:
        print("El número es par positivo.")
    else:
        print("El número es par negativo.")
else:
    if n > 0:
        print("El número es impar positivo.")
    else:
        print("El número es impar negativo.")
#Ejercicio24
c = float(input("Ingrese el valor de su compra, si es mayor a 150.000, se le aplica un descuento del 5%: "))
iva = c*0.19
total = c+iva
if c > 150000:
    d = total*0.5
    total = total-d
    print("El valor total de su compra con descuento, sumado el iva es:{}".format(total))
else:
    print("El valor total de su compra sin descuento, sumado el iva, es:{}".format(total))
#Ejercicio25
n= float(input("Ingrese un número: "))
if n >= 10:
    t = (n*3)
    print("El triple del número es: ", t)
#Ejercicio26
n1 = float(input("Ingrese la nota 1: "))
n2 = float(input("Ingrese la nota 2: "))
n3 = float(input("Ingrese la nota 3: "))
n4 = float(input("Ingrese la nota 4: "))
n5 = float(input("Ingrese la nota 5: "))
final = (n1 * 0.15) + (n2 * 0.20) + (n3 * 0.15) + (n4 * 0.30) + (n5 * 0.20)
if final < 2.0:
    print("No puede habilitar.")
if final < 3.0:
    print("Usted reprobó.")
if final >= 3.0:
    print("Usted aprobó.")
if final > 4.5:
    print("Excelente.")
#Ejercicio27
n1 = int(input("Ingrese un número entero: "))
n2 = int(input("Ingrese otro número: "))
print("El número mayor es:", max(n1, n2))
#Ejercicio28
n = int(input("Ingrese un número: "))
print("El número ingresado equivale a", float(n), "en decimal.")
#Ejercicio29
n1 = int(input("Ingrese un número entero: "))
n2 = int(input("Ingrese otro número entero: "))
n3 = int(input("Ingrese otro número entero: "))
print("El número mayor es", max(n1, n2, n3))
print( "y el menor es", min(n1, n2, n3))
#Ejercicio32
def bisiesto(x):
  if x%4==0 and (not(x%100==0) or x%400==0 ):
    t='es bisiesto'
  else:
    t='no es bisiesto.'
  return t
x=int(input('Introduzca un año:'))
print(x,bisiesto(x))
#Ejercicio34
usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")
if usuario.startswith("usuario") and contraseña.startswith("zxcvbnm123"):
    print("Inicio de sesión completado")
else:
    print("Inicio de sesión incorrecto, rectifique usuario o contraseña")
#Ejercicio36
n = int(input("Ingrese un número menor a 100000: "))
if n < 100000:
    print("El número", "", n, "", "tiene", len(str(n)), "dígitos")
else:
    print("Inválido el número es mayor a 100000")

