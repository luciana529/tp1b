peso_str = float (input( "Ingrese su peso (kg): "))
altura_str = float ( input( "Ingrese su altura en metros (m): "))
imc = peso_str / (altura_str * 2)
print(f"\nSu Índice de Masa Corporal (IMC) es: {imc:.1f}")