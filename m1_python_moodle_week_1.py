# =====================================================================
# 1. Solicitar el nombre (string)
# =====================================================================
nombre_producto = input("Ingrese el nombre del producto: ")

# =====================================================================
# 2. Solicitar Precio (float) y Cantidad (int) con validación
# =====================================================================

while True:
    try:
        # Usamos float() para el precio, permitiendo decimales.
        precio_unitario = float(input("Ingrese el precio unitario: "))

        # Criterio de aceptación: Los valores deben ser positivos
        if precio_unitario >= 0:
            break  # Salir del bucle si ambos son válidos
        else:
            print(" Error: El precio y la cantidad deben ser números positivos. Intente de nuevo.")
      
    except ValueError:
        # Tarea 2: Si el usuario ingresa un valor inválido, muestra un mensaje y vuelve a pedirlo.
        print(" Error: Por favor, ingrese un valor numérico válido para el precio y la cantidad. Intente de nuevo.")

while True: 
    try:
        # Usamos int() para la cantidad, asumiendo que son unidades enteras.
        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad >= 0:
            break  # Salir del bucle si ambos son válidos
        else:
            print(" Error: El precio y la cantidad deben ser números positivos. Intente de nuevo.")
    except ValueError:
        # Tarea 2: Si el usuario ingresa un valor inválido, muestra un mensaje y vuelve a pedirlo.
        print(" Error: Por favor, ingrese un valor numérico válido para la cantidad. Intente de nuevo.")

# =====================================================================
# TAREA 3: Operación matemática (costo total)
# =====================================================================

# Crear la variable costo_total para almacenar el resultado de la multiplicación.
# Asegurarse de que la operación se realice después de validar los datos de entrada (ya lo hicimos).
costo_total = precio_unitario * cantidad

# =====================================================================
# TAREA 4: Mostrar resultados
# =====================================================================

# Usar la función print() para mostrar un mensaje claro con los datos requeridos.
print("\n--- RESUMEN DE LA TRANSACCIÓN ---")
print(f"Nombre del producto: {nombre_producto}")
print(f"Precio unitario: {precio_unitario}")
print(f"Cantidad: {cantidad}")
print(f"Costo total calculado: {costo_total}")

# Mostrar el formato de mensaje solicitado para el criterio de la actividad.
print("\n--- FORMATO REQUERIDO ---")
print(f"Producto: {nombre_producto} | Precio: {precio_unitario} | Cantidad: {cantidad} | Total: {costo_total}")

# =====================================================================
# TAREA 5: Comentario general explicando qué hace el programa completo.
# =====================================================================

"""Este programa en Python solicita el nombre, precio y cantidad de un producto.
Luego, valida que el precio y la cantidad sean números positivos.
Finalmente, calcula el costo total y muestra un resumen de la transacción en la consola.
El código cumple con las tres fases: entrada (input), procesamiento (cálculo), y salida (print)."""