# Solicitar al usuario que ingrese un valor
entrada = input("Ingresa un valor: ")

# Intentar interpretarlo como diferentes tipos
try:
    # Usar literal_eval que es más seguro que eval
    #evalúa de forma segura expresiones literales de Python. Básicamente, convierte una cadena de texto que representa un literal de Python a su valor correspondiente.
    from ast import literal_eval
    valor = literal_eval(entrada)
except:
    # Si falla, mantenerlo como string
    valor = entrada

# Mostrar el tipo
print(f"El valor ingresado es de tipo: {type(valor).__name__}")
print(f"Valor: {valor}")