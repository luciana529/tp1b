total_segundos_str = int(input ("Ingrese la cantidad de segundos: "))
minutos = total_segundos_str// 60  # División entera para obtener la cantidad de minutos
segundos_restantes = total_segundos_str % 60  # Módulo para obtener los segundos restantes
print(f"{total_segundos_str} segundos son equivalentes a {minutos} minutos y {segundos_restantes} segundos.")
