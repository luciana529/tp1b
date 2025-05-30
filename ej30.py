# Pedir al usuario un número
numero = input("Ingresa un número (positivo o negativo): ")

try:
    # Convertir la entrada a un número flotante
    numero = float(numero)
    
    # Calcular el valor absoluto
    valor_absoluto = abs(numero)
    
    # Mostrar el resultado
    print(f"El valor absoluto de {numero} es: {valor_absoluto}")
    
except ValueError:
    print("Error: Por favor ingresa un número válido.")