#Definimos la matriz  a usar
def matrix_sum(matrix):
    # Obtenemos el tamaño de la matriz (n x n)
    n = len(matrix)
    
    # Inicializamos la Variable para guardar la mejor suma encontrada
    max_total = 0

    # Función recursiva (backtracking)
    def backtrack(row, used_columns, current_sum):
        nonlocal max_total  # Permite modificar la variable externa
        
        # Caso base: si ya recorrimos todas las filas
        if row == n:
            # Actualizamos el máximo si encontramos una suma mayor
            max_total = max(max_total, current_sum)
            return
        
        # Recorremos todas las columnas de la fila actual
        for col in range(n):
            # Verificamos si la columna ya fue usada
            if col not in used_columns:
                
                # Marcamos la columna como usada
                used_columns.add(col)
                
                # Sumamos el valor actual y avanzamos a la siguiente fila
                backtrack(
                    row + 1,  # siguiente fila
                    used_columns,
                    current_sum + matrix[row][col]
                )
                
                # "Deshacemos" la elección (backtracking)
                used_columns.remove(col)

    # Llamamos a la función empezando desde la fila 0
    backtrack(0, set(), 0)
    
    # Retornamos el mejor resultado encontrado
    return max_total

# Matriz de prueba
matrix = [
    [7, 53, 183, 439, 863],
    [497, 383, 563, 79, 973],
    [287, 63, 343, 169, 583],
    [627, 343, 773, 959, 943],
    [767, 473, 103, 699, 303]
]

# Llamamos la función e imprimimos el resultado
print(matrix_sum(matrix))