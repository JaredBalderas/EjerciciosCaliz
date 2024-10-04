# Descripción del ejercicio: Manejo de listas en Python
# Nombre completo: Jared Maximliano Balderas Dominguez
# Fecha de creación: 03 de octubre de 2024
# Tema: Fundamentos de Python - Manejo de listas

# Salto de línea
print()

# Crear una lista con compañeros
nombres = ['Jared', 'Ruben', 'Beni', 'Fernando']
# Hay que imprimir el tamaño de la lista
print(f"El tamano de la lista es {len(nombres)}")

# Imprimi el contenido de la lista
print(f"El contenido de la lista es {nombres}")

# Cambio el segundo elemento de la lista
nombres[1] = 'Josue'
print(nombres)

# Agregare un nuevo nombre a la lista
nombres.append('Luis Miguel')
print(nombres)

# Eliminar el tercer elemento de la lista
del nombres[2]
print(nombres)

# Desplegar la lista en orden inverso y separada por '*'
print('*'.join(nombres[::-1]))
