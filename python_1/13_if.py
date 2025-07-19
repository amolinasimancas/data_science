# Condicional: if
temp = input("Introduzca la temperatura medida: ")
tliq = 1513
sph = int(temp) - tliq

if sph < 20:
    print(f"SpH = {sph} aumente el flujo de acero cambiando a una buza de mayor diámetro o subiendo el nivel del distribuidor, riesgo de acero frío")
elif sph >=20 and sph <=40:
    print(f"SpH = {sph} condición estable!")
else:
    print(f"SpH = {sph} disminuya el flujo de aceo cambiando a una buza de menor diámetro o bajando el nivel del distribuidor, riesgo de perforación")