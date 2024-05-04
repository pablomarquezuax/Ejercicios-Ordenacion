def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        low, high = 0, i - 1
        key = arr[i]

        # Búsqueda binaria para encontrar la posición de inserción
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        
        # Insertar el elemento en la posición correcta
        arr = arr[:high + 1] + [key] + arr[high + 1:i] + arr[i + 1:]

    return arr

# Entrada de usuario para el array
entrada = input("Ingresa los elementos del array separados por espacios: ")
tabla = [int(x) for x in entrada.split()]

print("Tabla original:", tabla)
tabla_ordenada = binary_insertion_sort(tabla)
print("Tabla ordenada:", tabla_ordenada)


'''
Explicacion del algoritmo de ordenación por inserción dicotómica:

Cómo Funciona:

El algoritmo recorre cada elemento del array uno por uno.
Para cada elemento, encuentra su posición correcta en el array ordenado anteriormente 
utilizando una técnica llamada búsqueda binaria. Una vez que encuentra la posición correcta, 
inserta el elemento en esa posición y mueve los elementos necesarios para hacer espacio para él.
Repite este proceso hasta que todos los elementos estén en su lugar correcto.


Lo Bueno:

La búsqueda binaria reduce el número de comparaciones necesarias para encontrar 
la posición correcta de inserción, haciéndolo más rápido que el método de inserción tradicional.
No requiere espacio adicional en memoria, ya que ordena el array directamente.


Lo Malo:

En el peor caso, cuando el array está en orden inverso, puede llevar mucho tiempo ya que 
cada nuevo elemento necesita ser insertado al principio del array ordenado, lo que requiere
desplazar todos los elementos anteriores. Aunque más eficiente que el método tradicional en ciertos casos, 
todavía puede ser lento para grandes conjuntos de datos.


Resumen:

El algoritmo de ordenación por inserción dicotómica es una forma inteligente de ordenar un array. 
Utiliza una técnica llamada búsqueda binaria para encontrar la posición de inserción de cada elemento, 
lo que lo hace más rápido que el método tradicional. Sin embargo, en casos extremos, puede ser lento. 
Aun así, es una buena opción cuando se busca un equilibrio entre simplicidad y eficiencia.

'''