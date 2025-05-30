total_segundos_str = int(input("Ingrese la cantidad de segundos: "))
horas = total_segundos_str // 3600  # División entera para obtener la cantidad de horas
segundos_restantes_despues_horas = total_segundos_str % 3600
minutos = segundos_restantes_despues_horas // 60  # División entera para obtener la cantidad de minutos
segundos_restantes = segundos_restantes_despues_horas % 60  # Módulo para obtener los segundos restantes
print(f"{total_segundos_str} segundos son equivalentes a {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")
