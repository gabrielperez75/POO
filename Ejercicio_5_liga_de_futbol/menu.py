def Menu(opciones):
    print('\n')
    print('**Menú de Opciones**')
    print('\n')
    for item, valor in opciones.items():
        print(f'{item}: {valor}')
    print('\n')
        
        
def validar_opcion(listado, opcion):
    resultado = False
    if opcion in listado:
        resultado = opcion
    
    return resultado
    