import sys

valor_supera = int(sys.argv[1])

ventas = {
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,
}

#valor_supera = float(input('Ingrese monto a comparar: '))
superan = {
}

for mes, monto in ventas.items():
    if monto > valor_supera:
        superan[mes] = monto

print(f'Los meses en los que las ventas superan el monto de {valor_supera} son: {superan}')


print('---------------------------------------------------')

# Comprehesion

superan = {mes: monto for mes, monto in ventas.items() if monto > valor_supera}
print(f'Los meses en los que las ventas superan el monto de {valor_supera} son: {superan}')
