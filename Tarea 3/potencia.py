def potencia():
    n1 = int(input("Ingrese primer digito: "))
    n2 = int(input("Ingrese segundo digito: "))
    resultado = 0
    if n1 <= n2 or n1 >= n2:
        resultado = n1**n2
        print(resultado)
    return resultado
potencia()