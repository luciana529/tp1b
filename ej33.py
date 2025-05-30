# Pedir al usuario que ingrese una expresión matemática
expresion = input("Ingresa una expresión matemática (ej: 2 + 3 * 5): ")

try:
    # Evaluar la expresión
    resultado = eval(expresion)
    
    # Mostrar el resultado
    print(f"El resultado de {expresion} es: {resultado}")
    
except:
    print("Error: La expresión ingresada no es válida.")