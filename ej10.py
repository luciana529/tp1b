def realizar_operacion(num1, num2, operacion):
    """Realiza la operación especificada entre dos números."""
    if operacion == '+':
        return num1 + num2
    elif operacion == '-':
        return num1 - num2
    elif operacion == '*':
        return num1 * num2
    elif operacion == '/':
        if num2 == 0:
            return "¡Error! No se puede dividir por cero."
        return num1 / num2
    else:
        return "¡Error! Operación no válida."

def calculadora():
    """Función principal de la calculadora."""
    while True:
        try:
            num1_str = input("Ingresa el primer número: ")
            num1 = float(num1_str)
            break
        except ValueError:
            print("¡Error! El primer valor no es un número válido. Intenta de nuevo.")

    while True:
        operacion = input("Ingresa la operación (+, -, *, /): ")
        if operacion in ['+', '-', '*', '/']:
            break
        else:
            print("¡Error! Operación no válida. Por favor, ingresa +, -, *, o /.")

    while True:
        try:
            num2_str = input("Ingresa el segundo número: ")
            num2 = float(num2_str)
            break
        except ValueError:
            print("¡Error! El segundo valor no es un número válido. Intenta de nuevo.")

    resultado = realizar_operacion(num1, num2, operacion)
    print(f"\nEl resultado de {num1} {operacion} {num2} es: {resultado}")

if __name__ == "__main__":
    calculadora()
    print("¡Calculadora finalizada!")