cantidad= int(input("Ingrese una cantidad entera: "))
gruesas = cantidad // 144  # 1 gruesa = 12 docenas = 144 unidades
resto_despues_gruesas = cantidad % 144
docenas = resto_despues_gruesas // 12
unidades = resto_despues_gruesas % 12
print(f"{cantidad} unidades son equivalentes a:")
print(f"{gruesas} gruesas")
print(f"{docenas} docenas")
print(f"{unidades} unidades")