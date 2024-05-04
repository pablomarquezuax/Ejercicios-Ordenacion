def ordenacion_tareas_con_restricciones(n, restricciones):
    # Crear un diccionario para almacenar las tareas y sus precedentes
    precedentes = {}
    
    # Inicializar el diccionario con listas vacías para cada tarea
    for tarea in range(1, n + 1):
        precedentes[tarea] = []
    
    # Llenar el diccionario con las restricciones de precedencia
    for i, j in restricciones:
        if j not in precedentes:
            precedentes[j] = []
        precedentes[j].append(i)
    
    # Función auxiliar para recorrer las tareas en profundidad (DFS)
    def dfs(tarea, visitadas):
        if tarea not in visitadas:
            visitadas.add(tarea)
            for precedente in precedentes.get(tarea, []):
                dfs(precedente, visitadas)
            orden.append(tarea)
    
    # Lista para almacenar el orden de las tareas
    orden = []
    
    # Recorrer cada tarea y aplicar DFS
    visitadas = set()
    for tarea in range(1, n + 1):
        dfs(tarea, visitadas)
    
    # Devolver el orden inverso, ya que la lista se llena en orden inverso
    return orden[::-1]

# Entrada de usuario para el número total de tareas
n = int(input("Ingrese el número total de tareas: "))

# Entrada de usuario para las restricciones de precedencia
restricciones = []
print("Ingrese las restricciones de precedencia en formato 'i j'.")
print("Ingrese '0 0' para terminar.")
while True:
    entrada = input("Restricción: ")
    if entrada == '0 0':
        break
    i, j = map(int, entrada.split())
    restricciones.append((i, j))

# Calcular el orden de las tareas con las restricciones dadas
orden = ordenacion_tareas_con_restricciones(n, restricciones)
print("Orden de las tareas:", orden)
