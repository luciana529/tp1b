 #Escriba un programa que pida dos números y que escriba su media aritmética.
#Se recuerda que la media aritmética de dos números es la suma de ambos números
#dividida por 2.
 
num1_str =float( input("Ingrese el primer número: "))
num2_str = float(input("Ingrese el segundo número: "))
 

media = (num1_str + num2_str) / 2
print(f"\nLa media aritmética de {num1_str} y {num2_str} es: {media}")
