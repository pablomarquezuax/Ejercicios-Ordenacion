def esta_explorado(t, inicio, fin):
    """
    Verifica si un segmento en una tabla t ha sido explorado correctamente,
    siguiendo ciertos pasos específicos.

    Parámetros:
        t (list): La tabla de componentes.
        inicio (int): El índice de inicio del segmento.
        fin (int): El índice de fin del segmento.

    Retorna:
        bool: True si el segmento ha sido explorado correctamente, False de lo contrario.
    """

    # Verificar si los índices son válidos
    if inicio < 0 or fin >= len(t) or inicio > fin:
        return False
    
    # Realizar una copia de seguridad del máximo del segmento
    m = t[inicio]
    
    # Desplazar los elementos una celda hacia la izquierda
    for i in range(inicio, fin):
        t[i] = t[i + 1]
    
    # Colocar el elemento más grande en la posición 'fin'
    t[fin] = m
    
    return True

# Ejemplo de uso
t = [10, 8, 15, 18, 12, 7, 18, 14, 9, 18, 21, 3]
inicio = 5
fin = 9

explorado = esta_explorado(t, inicio, fin)
print("El segmento ha sido explorado correctamente:", explorado)
print("Tabla actualizada:", t)
