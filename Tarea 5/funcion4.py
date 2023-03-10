#Crear una funcion que elimine todas las apariciones de una palabra en una lista
#def eliminar_elementos(list):
#    res = []
#    eliminar = 200
#    eliminar = "mercedez"
#    for item in list:
#        if item not in res:
#            res.append(item)
#        if item == eliminar:
#            res.remove(item)
#    return res
#print(eliminar_elementos([6, 21, 200, 200, 1, 0])) # ⇒ eliminar 200
#print(eliminar_elementos(["toyota", "mercedez", "hyundai", "mercedez"] )) # ⇒ "mercedez"

frutas = ['sandia', 'melon', 'mango', 'manzana', 'piña']
#ropa = ['camisa', 'sueter', 'gorro', 'guantes']
def eliminar_elementos(s):
    return s.ispop(2)
print(list(filter(eliminar_elementos, frutas)))
#La funcion elimina elementos de una lista
#Se crea una lista
#Se selecciona el elemento a eliminar
#Se imprime la lista sin el elemento eliminado