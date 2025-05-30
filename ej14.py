def saludar_segun_hora():
    while True:
        try:
            hora_str = input("Ingrese la hora actual (en formato 24h, por ejemplo, 14): ")
            hora = int(hora_str)
            if 0 <= hora <= 23:
                break
            else:
                print("¡Error! La hora debe estar entre 0 y 23. Intente de nuevo.")
        except ValueError:
            print("¡Error! El valor ingresado no es una hora válida. Intente de nuevo.")

    if hora < 12:
        print("Buenos días")
    elif 12 <= hora < 19:  # Consideramos hasta las 18 inclusive para "buenas tardes"
        print("Buenas tardes")
    else:
        print("Buenas noches")

if __name__ == "__main__":
    saludar_segun_hora()
    print("¡Programa finalizado!")