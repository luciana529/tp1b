#Escriba un programa que pida una distancia en pulgadas y que escriba esa distancia
#en centímetros.
#Se recuerda que una pulgada son 2,54 cm.

pulgadas_str = input("Ingrese la distancia en pulgadas: ")
pulgadas = float(pulgadas_str)
total_centimetros = pulgadas * 2.54
print(f"{pulgadas} pulgadas son equivalentes a {total_centimetros:.2f} centímetros.")