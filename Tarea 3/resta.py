def resta():
    n1 = int(input("Ingrese el primer numero: "   ))
    n2 = int(input("Ingrese el segundo numero: "  ))
    resultado = 0
    if n1 >= n2 or n1 <= n2:
        resultado = n1-n2
        print(resultado)
        return resultado
resta()