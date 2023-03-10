#def potencia():
#    n1 = int(input("Ingrese primer digito: "))
#    n2 = int(input("Ingrese segundo digito: "))
#    resultado = 0
#    if n1 <= n2 or n1 >= n2:
#        resultado = n1**n2
#        print(resultado)
#    return resultado
#potencia()

def potencia(elemento=0):
    return elemento ** elemento
lista = [1,2,3,4,5]
#lista = [6,10,12,9]
resultado = list( map( lambda elemento : elemento ** elemento , lista) )
print(resultado)

#La funcion potencia se basa en la potencia de numeros.
#Se recive una lista con numeros y dichos numeros se elevan a la potencia
#Se elevan a sus mismos digitos