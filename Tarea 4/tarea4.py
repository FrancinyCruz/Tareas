#Funcion 1:

# Crear una funcion que cuente y imprima todos los numeros, 
# letras y caracteres especiales en una string

#def contar_caracteres(str):
#    str = "P@yn26at^&i5ve"
#    str = "la2mU&t55o"
#    str = "@mp21E"
#    str = "H2n8$vYqp86"
#    str = "/21?hDs+M"
#    letras = 0
#    numeros = 0
#    caracteres = 0
#    for x in str:
#        if x.isalpha():
#            letras += 1
#        elif x.isnumeric():
#            numeros += 1
#        else:
#            caracteres += 1
#    print("Letters: ", letras)
#    print("Numeros: ", numeros)
#    print("Caracteres: ", caracteres)
#contar_caracteres(str)



#Funcion 2:

#Crear una funcion que cuente todas las apariciones del caracter en una string,
#la string debe recibirse como parametro, debe ser impreso en diccionario.

#def contar_caracteres_string(str):
#    str = "papaya"
#    str = "fresa"
#    str = "panaderia"
#    str = "juego"
#    str = "lunch"
#    conteo = {}
#    for letra in str.lower():
#        if letra not in conteo:
#            conteo[letra] = 1
#        else:
#            conteo[letra] += 1
#    for clave, valor in conteo.items():
#            print("{}: {}".format(clave, valor))
#contar_caracteres_string(str)



#Funcion 3:

#Crear una funcion que elimine todas las apariciones de una palabra en una lista
#def eliminar_elementos(list):
#    res = []
#    eliminar = 20
#    eliminar = 200
#    eliminar = 2003
#    eliminar = "apple"
#    eliminar = "mercedez"
#    eliminar = "gato"
#    for item in list:
#        if item not in res:
#            res.append(item)
#        if item == eliminar:
#            res.remove(item)
#    return res
#print(eliminar_elementos([20, 30, 40, 20, 5, 100, 5, 20])) # ⇒ eliminar 20
#print(eliminar_elementos(["perro", "gato", "sombrero", "gato", "zanahoria"] )) # ⇒ "gato"
#print(eliminar_elementos([6, 21, 200, 200, 1, 0])) # ⇒ eliminar 200
#print(eliminar_elementos(["apple", "apple", "cherry", "carrot"] )) # ⇒ "apple"
#print(eliminar_elementos([9, 2003, 8, 21, 2003, 2003])) # ⇒ 2003
#print(eliminar_elementos(["toyota", "mercedez", "hyundai", "mercedez"] )) # ⇒ "mercedez"



#Funcion 4:

#Crear una función que reciba una secuencia de números separados por coma
#por parte del usuario e imprima una lista y una tupla que contengan dichos
#valores. El usuario debe ingresar un único input con los valores separados
#por comas.

#def recibir_secuencia_numeros():
#    num = input("Ingrese secuecia de numeros separados por coma \n")
#    list = []
#    tuple = (num)
#    for x in range(1):
#        list.append(num)
#    for x in range(1):
#        print("Lista: ", list)
#        print("Tupla: ", tuple)
#recibir_secuencia_numeros()