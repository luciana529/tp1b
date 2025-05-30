#Escriba un programa que pida una temperatura en grados Celsius y que escriba esa
#temperatura en grados Fahrenheit.
#Se recuerda que la relación entre grados Celsius (C) y grados Fahrenheit (F) es la
#siguiente: F = 1,8 * C + 32
celsius_str = input("Ingrese la temperatura en grados Celsius (°C): ")
celsius = float(celsius_str)
fahrenheit = 1.8 * celsius + 32
print(f"{celsius:.2f} grados Celsius son equivalentes a {fahrenheit:.2f} grados Fahrenheit.")