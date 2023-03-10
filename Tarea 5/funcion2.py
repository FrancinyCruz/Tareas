#def resta():
#    n1 = int(input("Ingrese el primer numero: "   ))
#    n2 = int(input("Ingrese el segundo numero: "  ))
#    resultado = 0
#    if n1 >= n2 or n1 <= n2:
#        resultado = n1-n2
#        print(resultado)
#        return resultado
#resta()

numbers1 = [4, 5, 6]
numbers2 = [1, 2, 3]
#numbers1 = [20,14,68]
#numbers2 = [8,4,46]
result = map(lambda x, y: x - y, numbers1, numbers2)
print(list(result))
#La funcion se basa en la suma de dos numeros
#Se crean dos listas 
#La funcion hace que ambas listas se resten entre si
#La lista 2 resta a la lista 1