def binary_insertion_sort_with_additional_table(t):
    # Crear una tabla adicional vacía del mismo tamaño que la tabla original
    r = [None] * len(t)
    
    # Iterar sobre cada elemento en la tabla original t
    for i in range(len(t)):
        key = t[i]  # Elemento actual que se va a insertar en r
        low, high = 0, i - 1  # Inicializar los índices para la búsqueda binaria
        
        # Búsqueda binaria para encontrar la posición de inserción en r
        while low <= high:
            mid = (low + high) // 2  # Calcular el índice medio
            if key < r[mid]:
                high = mid - 1  # El elemento debe ser insertado antes del índice medio
            else:
                low = mid + 1  # El elemento debe ser insertado después del índice medio
        
        # Insertar una copia del elemento en su posición correcta en r
        for j in range(i, high, -1):  # Desplazar elementos para hacer espacio
            r[j] = r[j - 1]
        r[high + 1] = key  # Insertar el elemento en la posición correcta
        
    return r

# Entrada de usuario para el array
entrada = input("Ingresa los elementos del array separados por espacios: ")
t = [int(x) for x in entrada.split()]

# Llamada a la función de ordenación
r_ordenada = binary_insertion_sort_with_additional_table(t)

# Impresión del resultado
print("Array original:", t)
print("Array ordenado:", r_ordenada)
