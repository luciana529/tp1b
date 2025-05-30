pies_str = input("Ingrese la distancia en pies: ")
pies = float(pies_str)            
total_pulgadas = pies * 12
total_centimetros = total_pulgadas * 2.54
print(f"{pies} pies son equivalentes a {total_centimetros:.2f} centímetros.")