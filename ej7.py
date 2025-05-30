
# Pedir al usuario que ingrese un número
try:
    numero_str = input("Por favor, introduce un número: ")
    numero = float(numero_str)  # Intentamos convertir la entrada a un número decimal
    doble = numero * 2
    print(f"El doble de {numero} es: {doble}")
except ValueError:
    print("¡Eso no parece un número válido! Por favor, intenta de nuevo.")