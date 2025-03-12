a = [7,1,5,3,6,4]

def arra_two_numbers(array):
    if len(array) < 2:
        return -1  # Manejar listas pequeñas
    
    max_diferecia = -1
    min_actual = array[0]
    
    for index in range(1, len(array)):  # Comenzar desde índice 1
        if array[index] < min_actual:
            min_actual = array[index]
        else:
            diff = array[index] - min_actual
            if diff > max_diferecia:
                max_diferecia = diff
        
        print('max diff:', max_diferecia, 'min actual:', min_actual)
    
    return max_diferecia if max_diferecia != 0 else -1  # Retornar resultado

print(arra_two_numbers(a))  # Output: 2 ✅