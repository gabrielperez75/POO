

def Menu(opciones):
    print('\n')
    for clave, valor in opciones.items():
        print(f'{clave}: {valor}')
    print('\n')
    
    
def validar_opcion(opcion, opciones):
    if opcion not in opciones:
        resultado = False
    else:
        resultado = True
        
    return resultado


def pedir_elementos_del_pedido(encontrado, instanciaP):
        
        
        id_pedido = input('Ingrese el ID pedido: ')
        comidas = [input('Ingrese las comidas, separadas por coma (,): ')]
        tpo_estimado = int(input('ingrese el tiempo estimado de entrega:  '))
        tpo_real = int(input('ingrese el tiempo real de entrega:  '))
        importe = float(input('Ingrese el importe total del pedido: '))
        instanciaP.agregar_pedido_manual(encontrado, id_pedido, comidas, tpo_estimado, importe, tpo_real)
        

 
        