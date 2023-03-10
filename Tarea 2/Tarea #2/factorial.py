#Escriba un programa en el que dado un número por el usuario,
# imprima el factorial (!) de dicho numero
# f = Factorial 
# x = while

n = int(input("Numero:"))
if n >= 0:
    x=1
    f=1 
    while x <= n:
        f = f * x
        x += 1
        print ("Factorial de ",n," es: ",f)
else:
    print ("Error")
