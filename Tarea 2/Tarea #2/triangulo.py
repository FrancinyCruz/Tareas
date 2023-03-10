#Escriba un programa que reciba un número del usuario y
#despliegue en pantalla el siguiente patrón de números llegando hasta el
#número elegido:

n = int(input("Numero:"))

if n == 0:
    print("Error")


for a in range(1,n+1):
    for b in range(1,a+1):
        print(b , end=" ")
    print("")
