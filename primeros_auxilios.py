responde_estimulos = input('¿Responde a los estímulos? (Ingrese solo si / no)\n').lower()

if responde_estimulos == 'no':
    print('\nAbrir la vía aérea\n')
    respira = input('¿Respira?\n').lower()
    if respira == 'no':
        print('\nAdministrar 5 Ventilaciones y llamar a la ambulancia\n') 
        def signos():           
            while True:
                signos_vida = input('\n¿Signos de vida?\n').lower()
                if signos_vida == 'si':
                    print('\nReevaluar a la espera de la Ambulancia\n')
                    llego_ambulancia = input('¿Llegó la ambulancia?\n').lower()
                    if llego_ambulancia == 'si':
                        break
                elif signos_vida == 'no':
                    print('\nAdministrar Compresiones Torácicas hasta que llegue la ambulancia\n')
                    llego_ambulancia = input('¿Llegó la ambulancia?\n').lower() 
                    if llego_ambulancia == 'si':
                        break
                else:
                    print('\nIngrese una opcion valida (Si o No)\n')
        signos()
    elif respira == 'si':
        print('\nPermitirle posición de suficiente ventilación\n')
    else:
        print('\nIngrese una opcion valida (Si o No)\n')
elif responde_estimulos == 'si':
    print('\nValorar la necesidad de llevarlo al hospital más cercano\n')
else:
    print('\nIngrese una opcion valida (Si o No)\n')