def contar_subcadenas_validas(s):
    n = len(s)
    count = 0
    left = 0
    # Diccionario para contar las ocurrencias de 'a', 'b' y 'c'
    ocurrencias = {'a': 0, 'b': 0, 'c': 0}
    
    for right in range(n):
        # Actualiza el conteo de caracteres
        ocurrencias[s[right]] += 1
        
        # Mueve left para contraer la ventana
        while all(ocurrencias[char] > 0 for char in ocurrencias):
            # Cuenta las subcadenas válidas
            count += n - right
            ocurrencias[s[left]] -= 1
            left += 1
    
    return count

s = "abcabc"
print(contar_subcadenas_validas(s))