#def division():
#    n1 = int(input("Ingrese primer digito: "))
#    n2 = int(input("Ingrese segundo digito: "))
#    resultado = 0
#    if n1 >= n2 or n1 <= n2:
#        resultado = n1/n2
#        print(resultado)
#    return resultado
#division()

list1 = [10, 20, 5]
list2 = [2, 3, 2]
#list1 = [60,100,30]
#list2 = [3,5,2]
result = map(lambda x, y: x / y, list1, list2)
print(list(result))
#La funcion se basa en la division de dos numeros
#Se crean 2 listas y la division seria la lista 1 dividido entre la lista 2