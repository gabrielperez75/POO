from controlador_cuentas import *
from controlador_transacciones import *
from menu_opciones import Menu

if __name__ == '__main__':
    menu_principal ={'0': 'finalizar', '1': 'Cargar Cuentas', '2': 'Cargar Transacciones', '3': 'Buscar datos del cliente', 
                     '4': 'Modificar tasa de interés', '5': 'Ver saldo de CVU', '6': 'Actualizar Saldos', '7': 'guardar datos' }
    
    menu = Menu()
    continuar = True
    controladorC = controladorCuenta()
    controladorT = ControladorTransaccion()
    
    while continuar:
        menu.mostrarMenu(menu_principal)
        opcion = input('ingrese la opción deseada: ')
        
        if opcion == '0':
            print('\nGracias por usar Perito software!')
            continuar = False
            
        elif opcion == '1':
            controladorC.cargaArchivo()
            
        elif opcion == '2':
            
            controladorT.cargarTransaccion()
            
            
        elif opcion == '3': 
            dni = controladorC.validarDni(input('Ingrese el dni a buscar: '))
            
            if dni == False:
                print('El dni no correponde a un cliente')
                
            else:
                cuenta = controladorC.buscarDatosCliente(dni)
                print(cuenta)
                
        
        elif opcion == '4':
            controladorC.cambiarPorcentaje(int(input('ingrese nuevo porcentaje: ')))
            
        
        elif opcion == '5':
            cvu = input('Ingrese la CVU a buscar: ')
            dato = controladorT.buscarDatosPorCvu(cvu, controladorC)
            if dato == False:
                print('El CVU no se encontró')
                
            else:
                print(dato)
                controladorT.actualizarDatos(controladorC)
                print('Volví de actualizar los datos')
                dato_1 = controladorT.buscarDatosPorCvu(cvu, controladorC)
                print(dato_1)
                
                
        elif opcion == '6':
            controladorC.actualizarSaldos()
                        
            
        
        
            
            
    
    