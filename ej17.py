#Escriba un programa que pida una distancia en pies y pulgadas y que escriba esa
#distancia en centímetros.
#Se recuerda que un pie son doce pulgadas y una pulgada son 2,54 cm.

pies_str = input("Ingrese la distancia en pies: ")
pies = float(pies_str)
pulgadas_str = input("Ingrese la distancia adicional en pulgadas: ")
pulgadas = float(pulgadas_str)
total_pulgadas = (pies * 12) + pulgadas
total_centimetros = total_pulgadas * 2.54
print(f"\n{pies} pies y {pulgadas} pulgadas son equivalentes a {total_centimetros:.2f} centímetros.")
