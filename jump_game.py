def jump_game(array_data, indice):
    # Mientras no llegues al último índice
    while indice < len(array_data) - 1:
        number = array_data[indice]
        
        # Si el número es 0, no puedes avanzar más
        if number == 0:
            return False
        
        # Actualiza el índice sumando el salto
        indice = indice + number
        
        # Si el nuevo índice está fuera del rango, verifica si llegaste al final
        if indice >= len(array_data) - 1:
            return True
        
    return True


nums = [1, 2, 3, 1, 0, 4]
x = jump_game(nums, 0)
print(x)