def lista_a_numero(lista):
    numero = 0
    for i, digito in enumerate(lista):
        numero += digito * (10 ** i)
    return numero

def numero_a_lista(numero):
    return [int(digito) for digito in str(numero)[::-1]]

def sumar_listas(l1, l2):
    # Convertir las listas en números
    num1 = lista_a_numero(l1)
    num2 = lista_a_numero(l2)
    
    # Sumar los números
    suma = num1 + num2
    
    # Convertir el resultado en una lista en orden inverso
    return numero_a_lista(suma)

# resultados
print(sumar_listas([2, 4, 3], [5, 6, 4]))  # Output: [7, 0, 8]
print(sumar_listas([0], [0]))              # Output: [0]
print(sumar_listas([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))  # Output: [8, 9, 9, 9, 0, 0, 0, 1]